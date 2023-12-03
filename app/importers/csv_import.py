from sqlalchemy import Column, String, Date,Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from models.database import BaseSQL,engine


#Base = declarative_base()
#BaseSQL.metadata.create_all(engine)

class Internships(BaseSQL):
    __tablename__ = 'internships'
    id = Column(Integer, primary_key=True, autoincrement=True)
    actively_hiring = Column(String)
    Type_of_internship = Column(String)
    company_name = Column(String)
    location = Column(String)
    stipend = Column(String)
    duration = Column(String)

    def __repr__(self):
        return f"<Internship(Type_of_internship={self.Type_of_internship}, company={self.company_name})>"
    


    

