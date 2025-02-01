CREATE TABLE dim_customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    city VARCHAR(100),
    age INT,
    gender VARCHAR(1)
);
