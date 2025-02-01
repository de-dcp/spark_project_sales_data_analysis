import csv
import random
from datetime import datetime, timedelta

filename = 'D:\SparkLearn\Spark_Sales_Data_Analysis\Output_Data\sales_data_2024.csv'

# Generate unique order IDs
order_ids = random.sample(range(100000, 999999), 50)  # 50 unique orders
customer_ids = list(range(1000, 11000))  # Customer ID between 1000 and 10999
store_ids = list(range(50))  # Store ID between 0 and 49
product_ids = list(range(1, 1001))  # Product ID between 1 and 1000

# Generate sales data
data = []
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)

def random_date(start, end):
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)

for order_id in order_ids:
    num_records = random.randint(1, 25)  # Each order can have 1-25 records
    for _ in range(num_records):
        customer_id = random.choice(customer_ids)
        store_id = random.choice(store_ids)
        product_id = random.choice(product_ids)
        unit = random.randint(1, 10)
        price = round(random.uniform(50, 500), 2)  # Price range between 50 and 500
        total_amount = round(unit * price, 2)
        sales_date = random_date(start_date, end_date).strftime("%Y-%m-%d")
        data.append([order_id, customer_id, store_id, product_id, unit, price, total_amount, sales_date])

# Write to CSV file

with open(filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Order ID", "Customer ID", "Store ID", "Product ID", "Unit", "Price", "Total Amount", "Sales Date"])
    writer.writerows(data)

print(f"CSV file '{filename}' has been created with sales records for the year 2024.")
