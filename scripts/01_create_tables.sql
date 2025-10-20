-- Sales data table

CREATE TABLE IF NOT EXISTS sales (
	id SERIAL PRIMARY KEY,
	product_name VARCHAR(50),
	price NUMERIC(10, 2),
	sale_date DATE
);

--Customers data table

CREATE TABLE customers (
	id SERIAL PRIMARY KEY,
	customer_name VARCHAR (50),
	country VARCHAR (50)
);


--Add foreign key

ALTER TABLE sales ADD COLUMN customer_id INT REFERENCES customers(id);