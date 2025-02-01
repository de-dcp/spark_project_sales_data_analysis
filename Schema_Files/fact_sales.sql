CREATE TABLE fact_sales (
    order_id INT NOT NULL,
    customer_id INT NOT NULL,
    store_id INT NOT NULL,
    product_id INT NOT NULL,
    units INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    date_id INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES dim_customers(customer_id),
    FOREIGN KEY (store_id) REFERENCES dim_stores(store_id),
    FOREIGN KEY (product_id) REFERENCES dim_products(product_id),
    FOREIGN KEY (date_id) REFERENCES dim_dates(date_id)
);
