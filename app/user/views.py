from flask import Blueprint, redirect, url_for, request, abort
from flask import render_template

from app.user.models import models, User

user_bp = Blueprint('user', __name__)


@user_bp.route('/')
def hello_world():
    # Flask有个template_folder属性，默认是app所在脚本的templates目录，render_template会去这个位置找index.html
    # 可以通过设置template_folder属性修改templates位置，static_folder同理

    # 获取文件，或者post表单
    print(request.files)
    print(request.form)
    return render_template('user/index.html', hello='hello,world')


@user_bp.route('/create/')
def create_model():
    models.create_all()
    return '创建成功'


@user_bp.route('/adduser')
def add_user():
    user = User()
    user.nickname = 'asdfaf'
    # 自定义save方法
    user.save()
    return '创建用户成功'


@user_bp.route('/dropdb')
def drop_all():
    models.drop_all()
    return '删库，跑路'


# 默认字符串不匹配/
# @user_bp.route('/name/<name>')
# @user_bp.route('/name/<int:name>')
@user_bp.route('/name/<path:name>')
def get_name(name):
    print(type(name))
    return name


# 加数字不行
# 多个路由对应一个视图函数
# 还有一个uuid不写了
@user_bp.route('/any/<any(a,werqwer):xxxx>/')
def get_any(xxxx):
    print(type(xxxx))
    # 重定向到hello_world视图
    # return 'hello' + str(xxxx)

    # return redirect('/')
    # 根据视图函数的endpoint生成url,endpoint默认为函数名字，可以通过endpoint属性修改
    # return redirect(url_for('user.hello_world'))

    # 还可以传参数
    # 蓝图名字.endpoint
    return redirect(url_for('user.get_name', name='a'))


# 异常处理与异常处理
@user_bp.route('/exception')
def exception_handler():
    abort(401)


@user_bp.route('/template')
def myrender_template():
    mylist = list(range(10))
    return render_template('user/test.html', mylist=mylist)


@user_bp.errorhandler(401)
def handle_401(e):
    print(e)
    print(type(e))
    return '401'


@user_bp.route('/bootstrap')
def bootstrap_test():
    return render_template('mybootstrap/index.html')


@user_bp.route('/static_test')
def static_test():
    return render_template('user/test.html')


# 分页器
@user_bp.route("/paginate/")
def pagi_nate():
    'http://127.0.0.1:5000/paginate/?page=1&per_page=2'
    '存在问题，没有的页数返回404,通过全局异常给返回到首页，或者返回到第一页'
    '限制一页显示的数目'
    user = User.query.paginate().items
    print(user)
    return render_template('user/pagination.html', users=user)
