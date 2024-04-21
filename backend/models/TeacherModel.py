from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class TeacherModel(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    teacher_id = Column(String(50), unique=True)
    teacher_name = Column(String(100))
    hours_taught = Column(Integer, default=0)

    def __init__(self, teacher_id, teacher_name):
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name
        self.hours_taught = 0

# Define a function to create a database session
def create_session(db_uri):
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

# Usage example:
if __name__ == "__main__":
    # Example usage to add a teacher to the database
    db_uri = 'mysql://root:85213@localhost/teacherss'
    session = create_session(db_uri)

    # Create a new teacher instance
    new_teacher = TeacherModel(teacher_id='T001', teacher_name='John Doe')

    # Add the teacher to the database
    session.add(new_teacher)
    session.commit()

    # Close the session
    session.close()
