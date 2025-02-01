CREATE TABLE dim_dates (
    date_id INT PRIMARY KEY,  -- Format YYYYMMDD (e.g., 20240101 for Jan 1, 2024)
    full_date DATE NOT NULL,
    year INT NOT NULL,
    month INT NOT NULL,
    day INT NOT NULL,
    weekday VARCHAR(20) NOT NULL
);
