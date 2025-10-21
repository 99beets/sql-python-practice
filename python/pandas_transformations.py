import os
import psycopg2
import pandas as pd

# Read DB password from environment variable
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "data_engineering_practice",
    "user": "paul",
    "password": os.getenv("PG_PWD")
}

# Connect to Postgres
conn = psycopg2.connect(**DB_CONFIG)

# Define the SQL query
query = """
SELECT
    product_name,
    SUM(quantity * price) AS total_revenue,
    SUM(quantity) AS total_units_sold
FROM sales
GROUP BY product_name
ORDER BY total_revenue DESC;
"""

# Load SQL result directly into a Pandas DataFrame
df = pd.read_sql_query(query, conn)

# Close the DB connection
conn.close()

# Show the dataframe
print("Succsessfully loaded data from PostgreSQL:")
print(df)

# Pandas transformations
df['average_price'] = df['total_revenue'] / df['total_units_sold']

# Sort by average_price
df_sorted = df.sort_values(by='average_price', ascending=False)

# Save the transformed dataframe to a new CSV file
output_path = "datasets/pandas_output.csv"
df_sorted.to_csv(output_path, index=False)

print(f"\n Data saved to {output_path}")