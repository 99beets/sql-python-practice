# SQL & Python practice

This is a small learning project for practicing basic SQL and Python scripts

- Create and query a PostgreSQL database
- Run SQL scripts for analysis
- Query the database using Python
- Keep credentials out of source code using environment variables

sql-python-practice/
├── scripts/ # SQL DDL + DML + queries
├── python/ # Python code to connect to PostgreSQL
├── datasets/ # Sample CSV dataset
└── README.md



# Setup

1. Install PostgreSQL and Python
2. Create the database `data_engineering_practice`
3. Run `scripts/01_create_tables.sql`
4. Run `scripts/02_insert_data.sql` or import the CSV
5. Export your password in Bash:
   ```bash
   export PG_PWD="your_password"
