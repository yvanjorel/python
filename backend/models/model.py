from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(100), nullable=False)
    course_id = db.Column(db.String(20), unique=True, nullable=False)
    hours_taught = db.Column(db.Integer, default=0, nullable=False)

    def __repr__(self):
        return f"Course(id={self.id}, course_name='{self.course_name}', course_id='{self.course_id}', hours_taught={self.hours_taught})"

class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(100), nullable=False)
    courses = db.relationship('Course', secondary='class_course_association', backref=db.backref('classes', lazy='dynamic'))
    course_hours = db.relationship('CourseHour', backref='class_hours', lazy='dynamic')

class CourseHour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    hours_taught = db.Column(db.Integer, default=0, nullable=False)
