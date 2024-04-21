from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class CourseModel(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    course_id = Column(String(50), unique=True)
    course_name = Column(String(100))

    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

# Define a function to create a database session
def create_session(db_uri):
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

# Usage example:
if __name__ == "__main__":
    # Example usage to add a course to the database
    db_uri = 'mysql://root:85213@localhost/teacherss'
    session = create_session(db_uri)

    # Create a new course instance
    new_course = CourseModel(course_id='CS101', course_name='Introduction to Computer Science')

    # Add the course to the database
    session.add(new_course)
    session.commit()

    # Close the session
    session.close()
