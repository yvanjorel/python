from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class ClassModel(Base):
    __tablename__ = 'classes'

    id = Column(Integer, primary_key=True)
    class_id = Column(String(50), unique=True)
    class_name = Column(String(100))
    hours_taught = Column(Integer, default=0)

    def __init__(self, class_id, class_name):
        self.class_id = class_id
        self.class_name = class_name
        self.hours_taught = 0

# Define a function to create a database session
def create_session(db_uri):
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

# Usage example:
if __name__ == "__main__":
    # Example usage to add a class to the database
    db_uri = 'mysql://root:85213@localhost/teacherss'
    session = create_session(db_uri)

    # Create a new class instance
    new_class = ClassModel(class_id='C001', class_name='Mathematics')

    # Add the class to the database
    session.add(new_class)
    session.commit()

    # Close the session
    session.close()
