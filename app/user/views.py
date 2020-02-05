import json

from alipay import AliPay
from flask import Blueprint, redirect, url_for, request, abort
from flask import render_template
from flask.views import MethodView
from sqlalchemy import text

from app.config.settings import appid
from app.user.models import models, User, Post, Group

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
    'page-1可能为负数'
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 2, type=int)
    # order_by在offset之前
    user = User.query.order_by(text('-id')).offset(per_page * (page - 1)).limit(per_page)
    print(user)
    return render_template('user/pagination.html', users=user)


@user_bp.route('/pagenation_obj/')
def pagination_obj():
    user_pagination = User.query.paginate()
    endpoint = 'user.pagination_obj'

    return render_template('user/pagination_obj.html', endpoint=endpoint, user_pagination=user_pagination)


@user_bp.route('/pay/')
def go_to_pay():
    # 传入订单id，检查订单id是否存在
    # 检查订单状态，已支付 未支付，取消等等

    a_p_key = r'C:\Users\jiangsheng\PycharmProjects\blog_project\app\config\app_private_key.pem'
    alipay_pub = r'C:\Users\jiangsheng\PycharmProjects\blog_project\app\config\alipay_public.pem'
    with open(a_p_key) as f:
        app_private_key_string = f.read()
    with open(alipay_pub) as f:
        alipay_public_key_string = f.read()

    alipay = AliPay(
        appid=appid,
        app_notify_url=None,  # the default notify path
        app_private_key_string=app_private_key_string,
        # alipay public key, do not use your own public key!
        alipay_public_key_string=alipay_public_key_string,
        sign_type="RSA2",  # RSA or RSA2
        debug=False  # False by default,开发者模式
    )

    order_string = alipay.api_alipay_trade_page_pay(
        out_trade_no=781,  # 订单id
        total_amount=str(11),  # 订单实付款
        subject='测试页面',  # 订单标题
        return_url='http://127.0.0.1:5000/check',
        notify_url=None  # 可选, 不填则使用默认notify url
    )
    pay_url = 'https://openapi.alipaydev.com/gateway.do?' + order_string
    return render_template('user/pay.html', pay_url=pay_url)


# 登录才可以调用
@user_bp.route('/check')
def get_return_params():
    '''
    订单状态修改为已支付
    :return:
    '''
    print(request.args)
    order_id = request.args.get('out_trade_no')
    a_p_key = r'C:\Users\jiangsheng\PycharmProjects\blog_project\app\config\app_private_key.pem'
    alipay_pub = r'C:\Users\jiangsheng\PycharmProjects\blog_project\app\config\alipay_public.pem'
    with open(a_p_key) as f:
        app_private_key_string = f.read()
    with open(alipay_pub) as f:
        alipay_public_key_string = f.read()
    print(alipay_public_key_string)
    print(app_private_key_string)
    alipay = AliPay(
        appid=appid,  # 应用APPID
        app_notify_url=None,  # 默认回调url
        app_private_key_string=app_private_key_string,  # 应用私钥文件路径
        # 支付宝的公钥文件，验证支付宝回传消息使用，不是你自己的公钥,
        alipay_public_key_string=alipay_public_key_string,
        sign_type="RSA2",  # RSA 或者 RSA2
        debug=True  # 默认False，False代表线上环境，True代表沙箱环境
    )
    # alipay = AliPay(
    #     appid=appid,
    #     app_notify_url=None,  # the default notify path
    #     app_private_key_string=app_private_key_string,
    #     # alipay public key, do not use your own public key!
    #     alipay_public_key_string=alipay_public_key_string,
    #     sign_type="RSA2",  # RSA or RSA2
    #     debug=False  # False by default,开发者模式
    # )
    response = alipay.api_alipay_trade_query(out_trade_no=order_id)
    print(response.json())
    return '回调成功'


class PostView(MethodView):
    def get(self):
        print(User.post)
        return render_template('user/post.html')

    def post(self):
        form_obj = request.form
        user_obj = User.query.filter_by(nickname='8').one()
        print(user_obj.post)
        title = form_obj.get('posts')
        post_obj = Post()
        post_obj.user = user_obj
        post_obj.title = title
        post_obj.save()

        return redirect(url_for('user.hello_world'))


class RegisterView(MethodView):
    def get(self):
        group_obj = Group.query.filter_by(id=2).one()
        print(group_obj.user)
        return '123'

    def post(self):
        data = request.data.decode()
        data=json.loads(data)
        print(data)
        group_obj = Group.query.filter_by(name='admin').one()
        print(group_obj)
        nickname = data.get('nickname')
        user_obj = User()
        user_obj.nickname = nickname
        user_obj.group = [group_obj]
        user_obj.save()
        return 'aa'


user_bp.add_url_rule('/register', view_func=RegisterView.as_view('register'))
user_bp.add_url_rule('/posts', view_func=PostView.as_view('posts'))
