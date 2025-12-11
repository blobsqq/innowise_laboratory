"""
Simple Book Collection API

Build a small web API that allows users to manage their book collection using FastAPI and SQLAlchemy ORM.
Add, view and delete books stored in a relational database
"""

# 1. Set Up Your Environment
#
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field

from book_api import models
from book_api.database import engine, SessionLocal

from sqlalchemy.orm import Session

# FastApi instance
app = FastAPI()

# Create DB tables
models.Base.metadata.create_all(bind=engine)

# 4. Create a dependency for a DB session
def get_db():
    """
    Dependency for a DB session

    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# 4. Create Your FastAPI Application. Pydantic Model
#
class Book(BaseModel):
    """
    Pydantic model representing a book in the collection

    attr:
       id (int): unique identifier for the book
       title (str): title of the book. Must be at least 1 character long
       author (str): author's name. Must be 1–100 characters long
       year (int | None): publication year of the book, optional
    """
    id: int
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    year: int | None = None

    model_config = {"from_attributes": True}


# 5. Add Endpoints
#
# POST method (Add new)
@app.post("/books/", response_model=Book)
def add_new_book(book: Book, db: Session = Depends(get_db)):
    """
    Add a new book to the Books list

    args:
        book (Book): data to add
    return:
        Book: new book object
    """
    book_model = models.Books()
    book_model.title = book.title
    book_model.author = book.author
    book_model.year = book.year

    db.add(book_model)
    db.commit()
    db.refresh(book_model)

    return book_model


# GET method (Get all)
@app.get("/books/",response_model=list[Book])
def get_all_books(
        skip: int = 0,
        limit: int = 10,
        db: Session = Depends(get_db)
):
    """
    Get all existing books from collection. If the list is
    empty, an empty list is returned

    return:
        list[Books]: list of all books in the collection
    """
    books = db.query(models.Books).offset(skip).limit(limit).all()
    return books


# DELETE method (Delete)
@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """
    Deletes a book from the BOOKS list by its ID

    args:
        book_id (int): ID of the book to delete
    return:
        str: confirmation message with ID of deleted book
    raises:
        HTTPException: if the book with entered id is not found
    """
    book_model = db.query(models.Books).filter(models.Books.id == book_id).first()

    if book_model is None:
        raise HTTPException(
            status_code=404,
            detail=f'ID{book_id}: Not found'
        )

    db.query(models.Books).filter(models.Books.id == book_id).delete()
    db.commit()

    return {'message': f'Book with id: {book_id} was deleted'}


# PUT method (Update)
@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book: Book, db: Session = Depends(get_db)):
    """Updates details of an existing book

    args:
        book_id (int): ID of the book to update
        book (Book): new book data that should replace existing entry
    return:
        Book: updated book object
    raise:
        HTTPException: if the book with entered ID is not found
    """
    book_model = db.query(models.Books).filter(models.Books.id == book_id).first()

    if book_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {book_id}: Not found")

    book_model.title = book.title
    book_model.author = book.author
    book_model.year = book.year

    db.commit()
    db.refresh(book_model)

    return book_model


# GET method (Search)
@app.get("/books/search/", response_model=list[Book])
def search_book(title: str | None = None,
                author: str | None = None,
                year: int | None = None,
                skip: int = 0,
                limit: int = 10,
                db: Session = Depends(get_db)):
    """
    Search books by title, author or year filters

    args:
        title (str | None): Optional case-insensitive filter
        author (str | None): Optional case-insensitive filter
        year (int | None): Optional filter for exact year values
    return:
        list[Book]: list of books or empty list
    """
    query = db.query(models.Books)

    if title:
        query = query.filter(models.Books.title.ilike(f'%{title}%'))
    if author:
        query = query.filter(models.Books.author.ilike(f'%{author}%'))
    if year is not None:
        query = query.filter(models.Books.year == year)

    results = query.offset(skip).limit(limit).all()

    return results