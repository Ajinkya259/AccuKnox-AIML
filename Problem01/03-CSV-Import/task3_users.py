import csv
import sqlite3

CSV_FILE = "users.csv"
DB_FILE = "users.db"


def read_csv():
    file = open(CSV_FILE)
    rows = csv.DictReader(file)

    users = []
    for row in rows:
        name = row["name"]
        email = row["email"]
        city = row["city"]
        users.append({"name": name, "email": email, "city": city})

    file.close()
    return users


def save_users(users):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute("CREATE TABLE users (name TEXT, email TEXT, city TEXT)")
    cursor.executemany("INSERT INTO users VALUES (:name, :email, :city)", users)
    conn.commit()
    conn.close()


def read_users():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT name, email, city FROM users")
    users = cursor.fetchall()
    conn.close()
    return users


def show_users(users):
    for name, email, city in users:
        print(name, email, city)


users = read_csv()
save_users(users)

users = read_users()
show_users(users)
print("Saved", len(users), "users to", DB_FILE)
