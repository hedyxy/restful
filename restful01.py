from flask import make_response,jsonify,Flask
from flask_restful import Resource,Api,reqparse
from flask_httpauth import HTTPBasicAuth

app=Flask(__name__)
api = Api(app=app)
auth = HTTPBasicAuth()#实例化处理

#认证通过
@auth.get_password
def get_password(username):
    if username=='hedy':#用户名是hedy,返回的密码是 admin,代表程序通过
        return 'admin'
#认证不通过
@auth.error_handler
def authorized():
    return make_response(jsonify({'msg':'您好，请认证'}),401)


#返回的错误页面有一些美化/友好的处理
@app.errorhandler(404)#必须带错误具体的参数这个参数
def not_found(error):#必须带error这个参数
    return make_response(jsonify({
        'error':'this page is not found'
    }),404)


#返回的错误页面有一些美化/友好的处理
@app.errorhandler(405)#必须带错误具体的参数这个参数
def not_found(error):#必须带error这个参数
    return make_response(jsonify({
        'error':'该方法只支持get请求'
    }),405)

#返回的错误页面有一些美化/友好的处理
@app.errorhandler(500)#必须带错误具体的参数这个参数
def not_found(error):#必须带error这个参数
    return make_response(jsonify({
        'error':'请耐心等待，服务器在休息'
    }),500)

@app.route('/index')
@auth.login_required
def index():
    return jsonify({'status':0,'msg':'ok','data':{'userID':1001,'name':'hedy','age':18}})


# @app.route('/login',methods=['POST'])
# def login():
#     parser = reqparse.RequestParser()#实例化
#
#     # 设置请求参数，type：数据类型；help：报错返回的信息required参数必填
#     parser.add_argument('username',type=str,help='账户不能为空',required = True)
#     parser.add_argument('password',type=str,help='密码不能为空')
#     parser.add_argument('age',type=int,help='年龄必须是整形')
#     # return jsonify({'stastus':0,'msg':'ok','data':parser.parse_args()})
#     return parser.parse_args()
#
# # 以类的方式编写;传入不同的请求方式，就可以自行判断是get还是post
# class LoginView(Resource):
#     def get(self):
#         return jsonify({'stastus':0,'msg':'ok','data':''})
#
#     def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('username',type=str,help='账户不能为空',required=True)
#         parser.add_argument('password', type=str, help='密码不能为空')
#         parser.add_argument('age', type=int, help='年龄必须是整形')
#         # return jsonify(parser.parse_args())
#         return jsonify({'status':0,'msg':'ok','data':parser.parse_args()})
# #     添加请求地址
# api.add_resource(LoginView, '/login1', endpoint="login1")
#

if __name__ == '__main__':
    app.run(debug=True)