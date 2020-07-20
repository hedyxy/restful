from flask import make_response,jsonify,Flask,abort,request
from flask_restful import Resource,Api
from flask_httpauth import HTTPBasicAuth
app = Flask(__name__)
api = Api(app=app)
auth = HTTPBasicAuth()


@auth.get_password
def get_password(name):
    if name=='hedy':
        return 'admin'
@auth.error_handler
def authoorized():
    return make_response(jsonify({'msg':'请认证'}),401)

# #必须带错误具体的参数这个参数
@app.errorhandler(404)
def not_found(error):#必须带error这个参数
    return make_response(jsonify({
        'msg':'this page is not found'
    }),404)


books=[
    {'id':1,'author':'hedy','name':'python学习','done':True},
{'id':2,'author':'hedy1','name':'python学习2','done':False},
]

@app.route('/v1/api/books',methods=['get'])
# @auth.login_required  #方法添加鉴权的方式
def get_books():
    return jsonify(books)

@app.route('/v1/api/books',methods=['POST'])
def create_books():
    if not request.json:
        abort(400)
    else:
        book={
            'id':books[-1]['id']+1,
            'author':request.json.get('author'),
            'name':request.json.get('name'),
            'done':True
        }
        books.append(book)
        return jsonify({'msg':'create ok'},201)


@app.route('/v1/api/book/<int:book_id>',methods=['GET'])
def get_book(book_id):
    book = list(filter(lambda t:t['id']==book_id,books))
    print(book)
    if len(book)==0:
        abort(404)
    else:
        return jsonify({'status':0,'msg':'ok','datas':book})
    return jsonify({'msg':'ok'})

@app.route('/v1/api/book/<int:book_id>',methods=['DELETE'])
def delete_book(book_id):
    book = list(filter(lambda t:t['id']==book_id,books))
    if len(book)==0:
        abort(404)
    else:
        books.remove(book[0])
        return jsonify({'status':1001,'msg':'书籍的信息已经删除成功'})


@app.route('/v1/api/book/<int:book_id>',methods=['PUT'])
def updata_book(book_id):
    book = list(filter(lambda t: t['id'] == book_id, books))
    if len(book)==0:
        abort(404)
    elif not request.json:
        abort(400)
    elif 'author'   not in request.json and 'name' not in request.json:
        abort(400)
    elif 'done' not in request.json and type(request.json['done']) is not  bool:
        abort(400)
    else:
        book[0]['author']=request.json.get('author',book[0]['author'])
        book[0]['name'] = request.json.get('name', book[0]['name'])
        book[0]['done'] = request.json.get('done', book[0]['done'])
        return jsonify({'status':1002,'msg':'更新图书信息成功','data':book[0]})


if __name__ == '__main__':
    app.run(debug=True)