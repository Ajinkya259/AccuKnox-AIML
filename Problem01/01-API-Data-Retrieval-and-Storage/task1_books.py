import os
import sqlite3
import webbrowser
import requests

API_URL = "https://openlibrary.org/search.json?q=python+programming&limit=10&fields=*"
DB_FILE = "books.db"


def fetch_books():
    response = requests.get(API_URL)
    data = response.json()

    books = []
    for item in data["docs"]:
        title = item.get("title", "Unknown")
        author = item.get("author_name", ["Unknown"])[0]
        year = item.get("first_publish_year")
        pages = item.get("number_of_pages_median")
        isbn = item.get("isbn", ["Unknown"])[0]
        books.append({"title": title, "author": author, "year": year, "pages": pages, "isbn": isbn})
    return books


def save_books(books):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS books")
    cursor.execute("CREATE TABLE books (title TEXT, author TEXT, year INTEGER, pages INTEGER, isbn TEXT)")
    cursor.executemany("INSERT INTO books VALUES (:title, :author, :year, :pages, :isbn)", books)
    conn.commit()
    conn.close()


def read_books():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT title, author, year, pages, isbn FROM books")
    books = cursor.fetchall()
    conn.close()
    return books


def show_books(books):
    for title, author, year, pages, isbn in books:
        print(title, author, year, pages, isbn)


def make_html(books):
    rows = ""
    for title, author, year, pages, isbn in books:
        rows += f"""
        <tr>
            <td>{title}</td>
            <td>{author}</td>
            <td>{year}</td>
            <td>{pages}</td>
            <td>{isbn}</td>
        </tr>"""

    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Books</title>
</head>
<body>
    <h2>Books</h2>
    <table border="1">
        <tr>
            <th>Title</th>
            <th>Author</th>
            <th>Year</th>
            <th>Pages</th>
            <th>ISBN</th>
        </tr>{rows}
    </table>
</body>
</html>
"""

    with open("books.html", "w") as f:
        f.write(html)


books = fetch_books()
save_books(books)
saved_books = read_books()
show_books(saved_books)
make_html(saved_books)
print("Saved", len(saved_books), "books to", DB_FILE, "and books.html")
webbrowser.open("file://" + os.path.abspath("books.html"))
