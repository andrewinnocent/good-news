"""Load raw Bible data from bible.json to PostgreSQL data"""

import psycopg2
import os
# import settings
import json
with open('bible.json') as f:
    data = json.load(f)

# Connect to an existing database
with open(os.environ.get('CONFIG')) as f:
    configs = json.loads(f.read())
    dbname = configs["DBNAME"]
    user = configs["USER"]
    password = configs["PASSWORD"]
    host = configs["HOST"]

conn = psycopg2.connect(host=host, dbname=dbname, user=user, password=password)

# Open a cursor to perform database operations
cur = conn.cursor()

# Parse through JSON file:
# each book is an object in the data array
# keys: abbrev, chapters, name
# chapters - array of arrays of verses for each chapter

# variables for each column
[book_name, book_abbr, chapter_number, verse_number, verse_text] = [None, None, None, None, None]

# PROBLEM is that each variable will be overwritten on each iteration (as is)
for book in data:
    book_name = book['name']
    book_abbr = book['abbrev']
    for chapter_index, chapter in enumerate(book['chapters']):
        chapter_number = chapter_index + 1
        for verse_index, verse in enumerate(chapter):
            verse_number = verse_index + 1
            verse_text = verse
            # Pass data to Verse table
            cur.execute("INSERT INTO app_verse (book_name, book_abbr, chapter_number, verse_number, verse_text) VALUES (%s, %s, %s, %s, %s)", (book_name, book_abbr, chapter_number, verse_number, verse_text))

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()
