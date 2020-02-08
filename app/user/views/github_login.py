from pprint import pprint

from flask import Blueprint, session, flash, redirect, url_for, render_template, g
from app.extenstion import github
from app.user.models.models import User

github_bp=Blueprint('github',__name__)



@github_bp.route('/index')
def index():
    if g.user:
        is_login = True if g.user else False  # 判断用户登录状态
        response = github.get('user')
        avatar = response['avatar_url']
        username = response['name']
        url = response['html_url']
        return render_template('github/index.html', is_login=is_login, avatar=avatar, username=username, url=url)
    is_login=False
    return render_template('github/index.html', is_login=is_login)


@github_bp.route('/github_login')
def github_login():
    if not session.get('user_id',None):
        return github.authorize(scope='repo')
    flash('already login in')
    return redirect(url_for('user.hello_world'))

@github_bp.route('/callback/github')
@github.authorized_handler
def authorized(access_token):
    print(access_token)
    if access_token is None:

        flash('Login failed.')

        return redirect(url_for('github.git_err'))
    # 下面会进行创建新用户，保存访问令牌，登入用户等操作，具体见后面
    response = github.get('user', access_token=access_token)

    user_obj=User(nickname=response.get('login'),access_token=access_token)
    user_obj.save()
    session['user_id'] = user_obj.id
    return redirect(url_for('github.index'))

@github_bp.route('/err')
def git_err():
    return 'git error'

@github.access_token_getter
def token_getter():
    user = g.user
    if user is not None:
        return user.access_token
