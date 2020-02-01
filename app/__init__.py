from flask import Flask

from app.extenstion import init_ext
from app.user import init_view


def create_app():
    app = Flask(__name__)
    # 虚拟机数据库你还能把我怎么的

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:js@192.168.116.132:3306/test'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    #toordebug需要
    app.config['SECRET_KEY']='SSSSSSSSSSSSSS'
    app.debug=True
    app.config['DEBUG_TB_PROFILER_ENABLED']=True

    # 执行先后顺序无关
    init_view(app=app)
    init_ext(app=app)
    return app


app = create_app()
