# AccuKnox AI/ML Trainee Assignment

## Structure

```
Problem01/
├── 01-API-Storage/
│   ├── task1_books.py
│   ├── books.db
│   └── books.html
├── 02-Visualization/
│   ├── task2_scores.py
│   └── scores_chart.png
└── 03-CSV-Import/
    ├── task3_users.py
    ├── users.csv
    └── users.db
```

## Setup

Python 3.9 or later.

```bash
pip install requests matplotlib
```

`sqlite3` and `csv` are part of the Python standard library.

## Problem 01

### 1. API Data Retrieval and Storage

Fetches a list of books from the Open Library API, stores the title, author, publication year, page count and ISBN in a SQLite database, reads them back from the database and displays them in the terminal and in an HTML page.

```bash
cd Problem01/01-API-Storage
python3 task1_books.py
```

Output: `books.db`, `books.html` (opens in the browser automatically).

### 2. Data Processing and Visualization

Fetches 2,000 student records from the Sling Academy sample data API, calculates the average score of each subject and the overall average, and draws a bar chart.

```bash
cd Problem01/02-Visualization
python3 task2_scores.py
```

Output: `scores_chart.png` (the chart also opens in a window).

### 3. CSV Data Import to a Database

Reads user records from `users.csv` (8 columns, 20 rows) and inserts the name, email and city of each user into a SQLite database.

```bash
cd Problem01/03-CSV-Import
python3 task3_users.py
```

Output: `users.db`.

### 4. Most complex Python code

https://github.com/Ajinkya259/RAG-that-wont-lie

Offline retrieval over 13.98 million English Wikipedia passages using FAISS and BM25, with a local LLM that declines to answer when the evidence is weak.

### 5. Most complex database code

https://github.com/Ajinkya259/Customer-Support-Agent

Postgres schema (`src/tarang/schema.sql`) and loader (`scripts/build_sql.py`) for a real-time voice support agent. Uses foreign keys, check constraints, JSONB and trigram indexes, and is queried live during calls.

## Assumptions

- No API endpoint was given for tasks 1 and 2. Public APIs that need no key were used:
  - Books: [Open Library Search API](https://openlibrary.org/dev/docs/api/search)
  - Student scores: [Sling Academy sample data](https://api.slingacademy.com/v1/sample-data/files/student-scores.json)
- No CSV file was given for task 3. `users.csv` contains made-up users with `example.com` email addresses.
- Each script recreates its table on every run, so running it again does not create duplicate rows.
- Each script is run from inside its own folder, since output files are written to the current folder.
