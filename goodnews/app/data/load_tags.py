"""Load raw Bible data from bible.json to PostgreSQL data"""

import psycopg2
import os
# import settings
import json

tags = ["love", "forgiveness"]

# Connect to an existing database
with open(os.environ.get('CONFIG')) as f:
    configs = json.loads(f.read())
    dbname = configs["DBNAME"]
    user = configs["USER"]
    password = configs["PASSWORD"]
    host = configs["HOST"]

conn = psycopg2.connect(host=host, dbname=dbname, user=user, password=password)
cur = conn.cursor()

# Always just start fresh so we don't worry about duplicate tags
cur.execute("DELETE FROM app_tag where TRUE")
for tag in tags:
    cur.execute("INSERT INTO app_tag (tag_name) VALUES ('%s')" % tag)

conn.commit()
cur.close()
conn.close()
