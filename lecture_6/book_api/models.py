"""
2. Define the Database and ORM Model

Use SQLite and SQLAlchemy to define your Book model
Each book should have:
    id: integer, primary key
    title: string (required)
    author: string (required)
    year: int (optional)
"""
from sqlalchemy import Column, Integer, String
from book_api.database import Base


class Books(Base):
    """
    SQLAlchemy ORM model for a book in the database

    attr:
        id (int): primary key, unique identifier for the book, auto-incremented
        title (str): title of the book
        author (str): tuthor of the book
        year (int): year of the book, optional
    """
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    author = Column(String)
    year = Column(Integer)

