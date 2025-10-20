--Find rows with missing product names

SELECT * FROM sales
WHERE product_name IS NULL OR product_name = '';


--Replace empty strings with NULL

UPDATE sales
SET product_name = NULL
WHERE product_name = '';


--Trim whitespace

UPDATE sales
SET product_name = TRIM(product_name);