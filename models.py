from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key =True, autoincrement=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    publication_date = Column(Date, nullable=False)


engine = create_engine('sqlite:///mylibrary.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()    
