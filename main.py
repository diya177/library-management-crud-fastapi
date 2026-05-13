#Import libraries
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

#Temporary database
books=[{"id":1,"title":"Book 1","author":"Author 1","price":510,"available":True},{"id":2,"title":"Book 2","author":"Author 2","price":620,"available":False}]

class Book(BaseModel):
    id:int
    title:str
    author:str
    price:float
    available:bool

#Home route
@app.get("/")
def home():
    return {
        "message":"Library Management CRUD API"
    }

#get all books
@app.get("/books")
def get_books():
    return{
        "books":books
    }

#get book by id
@app.get("/books/{book_id}")
def get_book(book_id:int):
    for book in books:
        if book["id"]==book_id:
            return {"book":book}
    return {"message":"Book not found"}

#create a new book
@app.post("/books")
def create_book(book:Book):
    books.append(book.model_dump())
    return {"message":"Book created successfully","book":book}

#update a book
@app.put("/books/{book_id}")
def update_book(book_id:int, updated_book:Book):
    for index, book in enumerate(books):
        if book["id"]==book_id:
            books[index]=updated_book.model_dump()
            return{
                "message":"Book updated successfully"
            }
    return{
        "message":"Book not found"
    }

#delete a book
@app.delete("/books/{book_id}")
def delete_book(book_id:int):
    for index, book in enumerate(books):
        if book["id"]==book_id:
            del books[index]
            return{
                "message":"Book deleted successfully"
            }
    return{
        "message":"Book not found"
    }

#Patch route
@app.patch("/books/{book_id}")
def partial_update_book(book_id:int, updated_fields:Book):
    for book in books:
        if book["id"]==book_id:
            book.update(updated_fields.model_dump(exclude_unset=True))
            return{
                "message":"Book partially updated successfully"
            }
    return{
        "message":"Book not found"
    }
