-- Sales data table

CREATE TABLE IF NOT EXISTS sales (
	id SERIAL PRIMARY KEY,
	product_name VARCHAR(50),
	price NUMERIC(10, 2),
	sale_date DATE
);
