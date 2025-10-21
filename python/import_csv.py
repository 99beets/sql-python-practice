import csv
import psycopg2

conn = psycopg2.connect(**DB_CONFIG)
cur = conn.cursor()

with open('datasets/sales_data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        cur.execute(
            "INSERT INTO " \
            "   sales (product_name, quantity, price, sale_date) " \
            "VALUES (%s, %s, %s, %s)"
            (row['product_name'], row['quantity'], row['price'], row['sale_date'])
        )

conn.commit()
cur.close()
conn.close()