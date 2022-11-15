from . import db
from flask_login import UserMixin

# create database model here

# models the courses model

class Course(db.Model, UserMixin):
    idcourses = db.Column(db.Integer, primary_key=True)
    courseTitle = db.Column(db.String(25))
    courseQues = db.Column(db.String(150))
    courseLink = db.Column(db.String(150))
    courseFeedback = db.Column(db.String(150))
    courseTime = db.Column(db.String(30))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', name='fk_user'))
    employees = db.relationship('Employee_Course')

# models the junction-table for employees and courses

class Employee_Course(db.Model, UserMixin):
    employee_id = db.Column(db.Integer, db.ForeignKey('user.id', name='fk_employee'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.idcourses', name='fk_course'), primary_key=True)
    manager_id = db.Column(db.Integer, db.ForeignKey('user.id', name='fk_course1'), primary_key=True)
    answer = db.Column(db.String(150))
    feedback = db.Column(db.String(150))

# models the users table

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstname = db.Column(db.String(150))
    lastname = db.Column(db.String(150))
    isManager = db.Column(db.String(1))
    isSupManager = db.Column(db.String(1))
    manager_id = db.Column(db.Integer, db.ForeignKey('user.id', name='fk_mngr'))
    employees = db.relationship('User')
    courses = db.relationship('Course')
    manager_courses = db.relationship('Employee_Course', foreign_keys='Employee_Course.manager_id')
    employee_courses = db.relationship('Employee_Course', foreign_keys='Employee_Course.employee_id')