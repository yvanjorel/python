from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class SessionModel(Base):
    __tablename__ = 'sessions'

    id = Column(Integer, primary_key=True)
    session_id = Column(String(50), unique=True)
    class_id = Column(String(50))
    course_id = Column(String(50))
    teacher_id = Column(String(50))
    date = Column(DateTime)
    duration_hours = Column(Float)

    def __init__(self, session_id, class_id, course_id, teacher_id, date, duration_hours):
        self.session_id = session_id
        self.class_id = class_id
        self.course_id = course_id
        self.teacher_id = teacher_id
        self.date = date
        self.duration_hours = duration_hours

# Define a function to create a database session
def create_session(db_uri):
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

# Usage example:
if __name__ == "__main__":
    # Example usage to add a session to the database
    db_uri = 'mysql://root:85213@localhost/teacherss'
    session = create_session(db_uri)

    # Create a new session instance
    new_session = SessionModel(
        session_id='S001',
        class_id='C001',
        course_id='CS101',
        teacher_id='T001',
        date='2024-04-18 09:00:00',  # Example date format: 'YYYY-MM-DD HH:MM:SS'
        duration_hours=2.5
    )

    # Add the session to the database
    session.add(new_session)
    session.commit()

    # Close the session
    session.close()
