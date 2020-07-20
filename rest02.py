from flask import make_response,jsonify,Flask,abort,request
from flask_restful import Resource,Api
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS

app = Flask(__name__)
api = Api(app=app)
auth = HTTPBasicAuth()
CORS(app)



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



class Books(Resource):
    # decorators = [auth.login_required]#添加鉴权
    # decorators = [jwt_required()]
    #查看所有书
    def get(self):
        return jsonify({'status':0,'msg':'ok','datas':books})

    #创建书
    def post(self):
        if not request.json:
            return jsonify({'status':1001,'msg':'请求参数不是json的数据，请检查，谢谢！！'})
        else:
            book = {
                'id': books[-1]['id'] + 1,
                'author': request.json.get('author'),
                'name': request.json.get('name'),
                'done': True
            }
            books.append(book)
            return jsonify({'status':1002,'msg': '添加书籍成功','datas':book}, 201)


class Book(Resource):
    # decorators = [auth.login_required]  # 类添加鉴权的方式
    # 查看某id的书
    def get(self,book_id):
        book = list(filter(lambda t: t['id'] == book_id, books))
        print(book)
        if len(book) == 0:
            return jsonify({'status': 1003, 'msg': '很抱歉，您查询的书的信息不存在'})
        else:
            return jsonify({'status': 0, 'msg': 'ok', 'datas': book})
        return jsonify({'msg': 'ok'})
    # 修改某id的书
    def put(self,book_id):
        book = list(filter(lambda t: t['id'] == book_id, books))
        if len(book) == 0:
            return jsonify({'status': 1003, 'msg': '很抱歉，您查询的书的信息不存在'})
        elif not request.json:
            return jsonify({'status': 1001, 'msg': '请求参数不是json的数据，请检查，谢谢！！'})
        elif 'author' not in request.json :
            return jsonify({'status': 1004, 'msg': '请求参数author不能为空'})
        elif 'name' not in request.json:
            return jsonify({'status': 1005, 'msg': '请求参数name不能为空'})
        elif 'done' not in request.json :
            return jsonify({'status': 1006, 'msg': '请求参数done不能为空'})
        elif type(request.json['done']) is not bool:
            return jsonify({'status': 1007, 'msg': '请求参数done必须是bool类型'})
        else:
            book[0]['author'] = request.json.get('author', book[0]['author'])
            book[0]['name'] = request.json.get('name', book[0]['name'])
            book[0]['done'] = request.json.get('done', book[0]['done'])
            return jsonify({'status': 1008, 'msg': '更新图书信息成功', 'data': book[0]})
    # 删除某id书
    def delete(self,book_id):
        book = list(filter(lambda t: t['id'] == book_id, books))
        if len(book) == 0:
            return jsonify({'status': 1003, 'msg': '很抱歉，您查询的书的信息不存在'})
        else:
            books.remove(book[0])
            return jsonify({'status': 1009, 'msg': '书籍的信息已经删除成功'})

api.add_resource(Books,'/v1/api/books')
api.add_resource(Book,'/v1/api/book/<int:book_id>')


if __name__ == '__main__':
    # app.run(host='0, 0, 0, 0',debug=True)
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)