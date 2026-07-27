import os
import psycopg2
import requests 


def lambda_handler(event, context):
    pg_host = os.environ["PG_HOST"]
    pg_password = os.environ["PG_PASSWORD"]

    conn = None
    try:
        conn = psycopg2.connect(
            host=pg_host,
            dbname="postgres",
            user="postgres",
            password=pg_password
        )
        cur = conn.cursor()

        response = requests.get("https://jsonplaceholder.typicode.com/users")
        users = response.json()

        for user in users:
            email = user.get("email", "").strip()
            if not email:
                continue

            try:
                cur.execute(
                    "INSERT INTO users (name, email) VALUES (%s, %s)",
                    (user["name"], email)
                )
                conn.commit()
            except Exception as row_error:
                conn.rollback()
                print(f"Row failed, skipped: {row_error}")

        cur.close()

    except Exception as fatal_error:
        print(f"Pipeline failed: {fatal_error}")
        raise

    finally:
        if conn:
            conn.close()

    return {"statusCode": 200, "body": "Pipeline ran successfully"}

if __name__ == "__main__":
    print(lambda_handler({}, {}))   