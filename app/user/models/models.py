from app.extenstion import models


class User(models.Model):
    __tablename__ = 'user'
    id = models.Column(models.Integer, primary_key=True)
    nickname = models.Column(models.String(20))
    access_token=models.Column(models.String(200))
    post = models.relationship('Post',
                               backref='user',
                               primaryjoin='User.id==Post.user_id',
                               foreign_keys='Post.user_id')

    def save(self):
        models.session.add(self)
        models.session.commit()


# 一对多关系,没有真实的外键
class Post(models.Model):
    __tablename__ = 'post'
    id = models.Column(models.Integer, primary_key=True)
    title = models.Column(models.String(128))
    user_id = models.Column(models.Integer,models.ForeignKey('user.id'))

    def save(self):
        # 懒得继承了，就这么写吧，父类的__tablename__属性是abstract
        models.session.add(self)
        models.session.commit()

