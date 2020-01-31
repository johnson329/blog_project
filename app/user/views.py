from flask import Blueprint
from flask import render_template

from app.user.models import models, User

user_bp = Blueprint('user', __name__)


@user_bp.route('/')
def hello_world():
    #Flask有个template_folder属性，默认是app所在脚本的templates目录，render_template会去这个位置找index.html
    #可以通过设置template_folder属性修改templates位置，static_folder同理
    return render_template('user/index.html',hello='hello,world')

@user_bp.route('/create/')
def create_model():
    models.create_all()
    return '创建成功'

@user_bp.route('/adduser')
def add_user():
    user=User()
    user.nickname='asdfaf'
    user.save()
    return '创建用户成功'
