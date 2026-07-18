import requests
import psycopg2
import os

# Connect to Postgres
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="postgres",
    user="postgres",
    password=os.environ.get("PG_PASSWORD")
)
cur = conn.cursor()

# Fetch data from API
response = requests.get("https://jsonplaceholder.typicode.com/users/")
data = response.json()

# Insert each user into api_users table
for x in data:
    cur.execute(
        "INSERT INTO api_users (id, name, email, company_name) VALUES (%s, %s, %s, %s);",
        (x["id"], x["name"], x["email"], x["company"]["name"])
    )

conn.commit()
cur.close()
conn.close()