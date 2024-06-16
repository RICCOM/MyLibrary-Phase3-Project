from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

# Defining the User model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    # Establishing a relationship with the Book model
    books = relationship('Book', back_populates='user')

# Modifying the Book model to include user_id
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    publication_date = Column(Date, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    # Establishing a relationship with the User model
    user = relationship('User', back_populates='books')

# Creating the database and tables
engine = create_engine('sqlite:///mylibrary.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
