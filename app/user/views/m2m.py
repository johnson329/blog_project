import json

from flask import Blueprint, request
from flask.views import MethodView

from app.user.models.m2m import *

m2m_bp = Blueprint('m2m', __name__)


class RegisterView(MethodView):
    def get(self):
        child_obj = Child.query.filter_by(id=1).one()
        print(child_obj.parents)
        return '123'

    def post(self):
        data = request.data.decode()
        data=json.loads(data)
        print(data)
        child_obj = Child.query.filter_by(id=1).one()
        print(child_obj)
        p=Parent()
        p.children = [child_obj]
        print(p.children)
        models.session.add(p)
        models.session.commit()
        return 'aa'


# m2m_bp.add_url_rule('/register', view_func=RegisterView.as_view('register'))
