import psycopg2
import os

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "data_engineering_practice",
    "user": "postgres",
    "password": os.getenv("PG_PWD") # Imported password from environment variable
}

def main():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    cur.execute(
        """SELECT product_name, SUM(quantity * price) AS total_revenue
        FROM sales
        GROUP BY product_name
        ORDER BY total_revenue DESC;
        """
    )

    rows = cur.fetchall()

    for product, revenue in rows:
        print(f"{product:10s} | £{revenue}")

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()