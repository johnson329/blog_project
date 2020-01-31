from flask import Blueprint
from flask import render_template
user_bp = Blueprint('user', __name__)


@user_bp.route('/')
def hello_world():
    #Flask有个template_folder属性，默认是app所在脚本的templates目录，render_template会去这个位置找index.html
    #可以通过设置template_folder属性修改templates位置，static_folder同理
    return render_template('user/index.html',hello='hello,world')
