import requests
import psycopg2
import os

# connect to postgres
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="postgres",
    user="postgres",
    password=os.environ.get("PG_PASSWORD")
)
cur = conn.cursor()

# fetch data from api
response = requests.get("https://jsonplaceholder.typicode.com/users/")
data = response.json()

# insert each user into api_users table
for x in data:
    # skip users with no email, we don't need them
    if x["email"] == "":
        continue

    # try the insert, if it fails log it and roll back so the loop can keep going
    try:
        cur.execute(
            "INSERT INTO api_users (id, name, email, company_name) VALUES (%s, %s, %s, %s);",
            (x["id"], x["name"], x["email"], x["company"]["name"])
        )
    except Exception as e:
        print("failed to insert:", x["email"], e)
        conn.rollback()

conn.commit()
cur.close()
conn.close()
