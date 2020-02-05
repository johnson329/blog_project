from app.extenstion import models

user_group_table = models.Table('user_group',models.metadata,
                                models.Column('user_id', models.Integer, models.ForeignKey('user.id')),
                                models.Column('group_id', models.Integer, models.ForeignKey('group.id')))


class User(models.Model):
    __tablename__ = 'user'
    id = models.Column(models.Integer, primary_key=True)
    nickname = models.Column(models.String(20))
    # post=models.relationship('Post',backref='user',primaryjoin='foreign(Post.user_id) == remote(User.id)',uselist=False)
    # 没有uselist是一对多，关系写在1，obj_id写在多
    post = models.relationship('Post', backref='user', primaryjoin='foreign(Post.user_id) == remote(User.id)')
    # group = models.relationship('Group',
    #                             secondary=user_group_table,
    #                             primaryjoin='user.id==user_group.user_id',
    #                             secondaryjoin='group.id==user_group.group_id',
    #                             backref='user')
    group=models.relationship('Group',secondary=user_group_table,backref='user')


    def save(self):
        models.session.add(self)
        models.session.commit()


# 一对多关系,没有真实的外键
class Post(models.Model):
    __tablename__ = 'post'
    id = models.Column(models.Integer, primary_key=True)
    title = models.Column(models.String(128))
    # user_id = models.Column(models.Integer,models.ForeignKey('user.id'))
    user_id = models.Column(models.Integer)

    def save(self):
        # 懒得继承了，就这么写吧，父类的__tablename__属性是abstract
        models.session.add(self)
        models.session.commit()


class Group(models.Model):
    __tablename__ = 'group'
    id = models.Column(models.Integer, primary_key=True)
    name = models.Column(models.String(128))

    def save(self):
        # 懒得继承了，就这么写吧，父类的__tablename__属性是abstract
        models.session.add(self)
        models.session.commit()
