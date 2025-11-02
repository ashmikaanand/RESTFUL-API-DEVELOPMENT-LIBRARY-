from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample book data
books = [
    {"id": 1, "title": "Python for Beginners", "author": "John Doe"},
    {"id": 2, "title": "REST API with Flask", "author": "Jane Doe"},
    {"id": 3, "title": "Data Science with Python", "author": "Ashmika A.A"},
    {"id": 4, "title": "Machine Learning Basics", "author": "Andrew Ng"},
    {"id": 5, "title": "Flask Web Development", "author": "Miguel Grinberg"}
]

# 🔹 Print all books neatly in console
print("\n📚 Library Book List:\n")
for book in books:
    print(f"📘 ID: {book['id']}\n   Title: {book['title']}\n   Author: {book['author']}\n")

# ✅ Home route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Library RESTful API!"})

# ✅ GET - Retrieve all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# ✅ GET - Retrieve one book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"message": "Book not found"}), 404

# ✅ POST - Add a new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_id = max(book["id"] for book in books) + 1
    new_book = {"id": new_id, "title": data["title"], "author": data["author"]}
    books.append(new_book)
    print(f"✅ Added Book:\n📘 ID: {new_id}\n   Title: {data['title']}\n   Author: {data['author']}\n")
    return jsonify({"message": "Book added successfully!", "book": new_book}), 201

# ✅ PUT - Update a book by ID
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    for book in books:
        if book["id"] == book_id:
            book.update(data)
            print(f"✏️ Updated Book ID {book_id}: {book}\n")
            return jsonify({"message": f"Book {book_id} updated successfully!", "updated_data": book})
    return jsonify({"message": "Book not found"}), 404

# ✅ DELETE - Remove a book by ID
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book["id"] != book_id]
    print(f"🗑️ Deleted Book ID {book_id}\n")
    return jsonify({"message": f"Book {book_id} deleted successfully!"})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
