import requests

BASE_URL = "http://127.0.0.1:5000"

# GET all books
print("\nGET /books")
print(requests.get(f"{BASE_URL}/books").json())

# POST a new book
print("\nPOST /books")
new_book = {"title": "Machine Learning 101", "author": "Ashmika A.A"}
print(requests.post(f"{BASE_URL}/books", json=new_book).json())

# PUT (update) an existing book
print("\nPUT /books/1")
update_data = {"title": "Advanced Python", "author": "Ashmika A.A"}
print(requests.put(f"{BASE_URL}/books/1", json=update_data).json())

# DELETE a book
print("\nDELETE /books/2")
print(requests.delete(f"{BASE_URL}/books/2").json())
