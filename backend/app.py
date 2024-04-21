from flask import Flask, request, jsonify
from flask import jsonify
from models.model import Class, Course, CourseHour
from models.model import db
from flask_sqlalchemy import SQLAlchemy

from models.ClassModel import ClassModel
from models.CourseModel import CourseModel
from models.TeacherModel import TeacherModel
from models.SessionModel import SessionModel


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:85213@localhost/app'  # Replace with your MySQL database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define your database models here

if __name__ == '__main__':
    app.run(debug=True)


app = Flask(__name__)

classes = []  
courses = []  
teachers = []  
sessions = []  
Class = []
CourseHour = []
Course = []

# Controller routes
@app.route('/add_class', methods=['POST'])
def add_class():
    data = request.get_json()
    new_class = Class(id=data['id'], class_name=data['class_name'])
    classes.append(new_class)
    return jsonify({"message": "Class added successfully"})

@app.route('/add_course', methods=['POST'])
def add_course():
    data = request.get_json()
    new_course = CourseModel(course_id=data['course_id'], course_name=data['course_name'])
    courses.append(new_course)
    return jsonify({"message": "Course added successfully"})

@app.route('/add_teacher', methods=['POST'])
def add_teacher():
    data = request.get_json()
    new_teacher = TeacherModel(teacher_id=data['teacher_id'], teacher_name=data['teacher_name'])
    teachers.append(new_teacher)
    return jsonify({"message": "Teacher added successfully"})

@app.route('/schedule_session', methods=['POST'])
def schedule_session():
    data = request.get_json()
    new_session = SessionModel(
        session_id=data['session_id'],
        class_id=data['class_id'],
        course_id=data['course_id'],
        teacher_id=data['teacher_id'],
        date=data['date'],
        duration_hours=data['duration_hours']
    )
    sessions.append(new_session)
    return jsonify({"message": "Session scheduled successfully"})

@app.route('/teach_hours', methods=['POST'])
def teach_hours():
    data = request.get_json()
    teacher_id = data['teacher_id']
    hours_taught = data['hours_taught']
    for teacher in teachers:
        if teacher.teacher_id == teacher_id:
            teacher.hours_taught += hours_taught
            return jsonify({"message": "Teaching hours updated successfully"})
    return jsonify({"message": "Teacher not found"})

# Get all classes
@app.route('/classes', methods=['GET'])
def get_classes():
    classes = Class.query.all()
    output = [{'id': c.id, 'class_name': c.class_name} for c in classes]
    return jsonify({'classes': output})

# Get courses for a specific class
@app.route('/classes/<int:class_id>/courses', methods=['GET'])
def get_courses_for_class(class_id):
    _class = Class.query.get_or_404(class_id)
    courses = _class.courses
    output = [{'id': c.id, 'course_name': c.course_name} for c in courses]
    return jsonify({'courses': output})

# Increment hours for a particular course in a specific class
@app.route('/classes/<int:class_id>/courses/<int:course_id>/increment-hours', methods=['POST'])
def increment_hours(class_id, course_id):
    course_hour = CourseHour.query.filter_by(class_id=class_id, course_id=course_id).first()
    if not course_hour:
        course_hour = CourseHour(class_id=class_id, course_id=course_id)
        db.session.add(course_hour)
    course_hour.hours_taught += 1
    db.session.commit()
    return jsonify({'message': 'Hours incremented successfully'})


if __name__ == '__main__':
    app.run(debug=True)
