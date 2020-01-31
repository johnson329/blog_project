# from manage import app
# 回到init_route的方式，manage 引入view来init_route，而view又引用了model，model又引用了manage
# 还是会有循环引用的问题，如果app不是传进来的方式，例如类似init_model这种传进来的方式
from flask_sqlalchemy import SQLAlchemy




# 解决办法
#不引入app,app通过函数传入进来构建sqlalchemy
models = SQLAlchemy()


def init_model(app):
    #这样写又会造成下面的user模型无法获取model对象,
    # 又不能把user类定义在函数里面，否则view无法获取
    # 所以通过一种懒加载的方式，先先创建对象
    #后通过app加载
    # models = SQLAlchemy()

    #概括起来就是app不通过函数传进来会有循环引用的问题，通过函数传进来，下面定义的模型无法获取model
    #解决办法就是懒加载
    models.init_app(app=app)


class User(models.Model):
    id = models.Column(models.Integer, primary_key=True)
    nickname = models.Column(models.String(20))
