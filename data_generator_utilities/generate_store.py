import csv
import random

filename = 'D:\SparkLearn\Spark_Sales_Data_Analysis\Output_Data\store_data.csv'

# List of Indian cities
indian_cities = [
    "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Ahmedabad", "Chennai", "Kolkata", "Pune", "Jaipur", "Lucknow",
    "Kanpur", "Nagpur", "Indore", "Thane", "Bhopal", "Visakhapatnam", "Patna", "Vadodara", "Ghaziabad", "Ludhiana",
    "Agra", "Nashik", "Faridabad", "Meerut", "Rajkot", "Varanasi", "Srinagar", "Aurangabad", "Dhanbad", "Amritsar",
    "Navi Mumbai", "Allahabad", "Howrah", "Ranchi", "Gwalior", "Jabalpur", "Coimbatore", "Vijayawada", "Jodhpur", "Madurai",
    "Raipur", "Kota", "Guwahati", "Chandigarh", "Solapur", "Hubli", "Bareilly", "Mysore", "Tiruchirappalli", "Salem"
]

# Generate unique 5-digit store IDs
store_ids = random.sample(range(10000, 99999), 50)

# Generate store details
data = []
for i in range(50):
    store_id = i
    store_name = f"Store_{i+1}"
    city = random.choice(indian_cities)
    data.append([store_id, store_name, city])

# Write to CSV file

with open(filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Store ID", "Store Name", "City"])
    writer.writerows(data)

print(f"CSV file '{csv_file}' has been created with 50 store details.")
