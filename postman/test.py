# str='()'
# list = []
# count=0
# for i in range(len(str)):
#     if str[i]=='(':
#         list.append(str[i])
#
#     elif str[i] == ')' and len(list) > 0:
#         list.pop(len(list)-1)
#         count+=1
#
# # for j in range(len(str)):
# #
# #     if str[j]==')' and len(list)>0:
# #         list.pop(len(list)-1)
# #         count+=1
#
#
#
# print(count)

# for i in range(5):
#     print(i)
# list=[1,2]
# for i  in range(len(list)):
#     print(i)

# data=lambda **kwargs : dict(sorted(kwargs.items(),key=lambda item:item[0]))
# print(data(name='admin',age=18,addr='bj'))

# list1=[1,2,3,4,5]
# def f():
#     list2=[]
#     for i in list1:
#         i+=100
#         list2.append(i)
#     print(list2)

# def f(a):
#     return a+100
#
# print(list(map(f,list1)))
# print(list(map(lambda a:a+100,list1)))


# list1=[1,2,3,4,5]
# list2=[]
# def f():
#     list2=[]
#     for i in list1:
#         if i>1:
#             list2.append(i)
#     print(list2)
# f()
#
# print(list(filter(lambda a:a>1,list1)))


# def f():
#     print('hello')
#
# def f2(a):
#     return a
#
# def login(username='hedy',password='admin'):
#     if username=='hedy' and password=='admin':
#         return 'sdfaskj'
#     else:
#         return '登陆账号错误'
# def profile(token):
#     if token=='sdfaskj':
#         return '欢迎进入hedy个人主页'
#     else:
#         return '请登陆系统'
#
# # print(profile(login()))
#
# def f3():
#     def f4():
#         return 'hello'
#     return f4()
#
# print(f3())

# def getInfo(func):
#     def inner():
#         print('公共部分')
#         func()
#     return inner
#
# @getInfo
# def f1():
#     print('hedy1')
#
#
#
# def f2():
#     print('hedy2')
#
# f1()

# def login(username='hedy',password='admin'):
#     if username == 'hedy' and password == 'admin':
#         return 'sdfaskj'
#     else:
#         return '登陆账号错误'


# def login(func):
#     def inner(token='sjkdfj'):
#         if token=='sjkdfj':
#
#             return func(token)
#         else:
#             return '请登陆系统'
#     return inner
#
#
# @login
# def profile(token):
#     return '您的主页信息'
#
# print(profile('sjkdfj'))
#
#
#
# def outer(func):
#     def inner(*args,**kwargs):
#         print(args,kwargs)
#         func()
#     return inner
def inOut():
    username = input('请输入账号')
    password = input('请输入密码')
    return username,password

def register():
    '''实现账户的注册功能'''
    username,password=inOut()
    temp=username+'|'+password
    with open('login.md','w') as f:
        f.write(temp)

def login():

    with open('login.md','r') as f:
        info=f.read()
        info=info.split('|')
    username, password = inOut()
    if username==info[0] and password==info[1]:
        return True
    else:
        return False

def getNick(func):
    with open('login.md','r') as f:
        info = f.read()
    info=info.split('|')
    if func:  #if func==Ture
        print( '{0}您好，欢迎您访问系统'.format(info[0]))
    else:
        print('请登陆系统')


if __name__ == '__main__':
    while(True):
        t=int(input('1,注册 2，登陆  3，推出系统\n'))
        if t==1:
            register()
        elif t==2:

            getNick(login())
        elif t==3:
            import sys
            sys.exit(1)
        else:
            print('输入不合法')




















