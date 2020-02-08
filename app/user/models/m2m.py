from app.extenstion import models

# stu_course_table = models.Table('stu_course',models.metadata,
#                                 models.Column('stu_id', models.Integer, primary_key=True,),
#                                 models.Column('course_id', models.Integer, primary_key=True))
#
# class Student(models.Model):
#     __tablename__ = 'student'
#     id = models.Column(models.Integer, primary_key=True)
#     name = models.Column(models.String(16))
#     course=models.relationship('Course',
#                                secondary=stu_course_table,
#                                primaryjoin='student.id==stu_course.stu_id',
#                                secondaryjoin='course.id==stu_course.course_id',
#                                backref='student')
#
#
# class Course(models.Model):
#     __tablename__ = 'course'
#     id = models.Column(models.Integer, primary_key=True)
#     name = models.Column(models.String(16))
association_table = models.Table('association', models.metadata,

    models.Column('left_id', models.Integer, models.ForeignKey('left.id')),
    models.Column('right_id', models.Integer, models.ForeignKey('right.id'))
)

class Parent(models.Model):
    __tablename__ = 'left'
    id = models.Column(models.Integer, primary_key=True)
    children = models.relationship(
        "Child",
        # secondary=association_table,
        backref='parents')
    # children = models.relationship(
    #     "Child",
    #     secondary=association_table,
    #     primaryjoin='left.id == association.left_id',
    #     secondaryjoin='right.id == association.right_id',
    #     backref='parents')

class Child(models.Model):
    __tablename__ = 'right'
    id = models.Column(models.Integer, primary_key=True)
    parents = models.relationship("Middle", back_populates="child")
