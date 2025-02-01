import csv
import random

filename = 'D:\SparkLearn\Spark_Sales_Data_Analysis\Output_Data\product_data.csv'
# List of categories
categories = ['Food', 'Electronic', 'Health and Hygiene', 'Beauty', 'Games']

# List of possible brands for each category
brands = {
    'Food': ['Nestle', 'Kraft', 'PepsiCo', 'General Mills', 'Unilever'],
    'Electronic': ['Samsung', 'Apple', 'Sony', 'LG', 'Huawei'],
    'Health and Hygiene': ['Procter & Gamble', 'Johnson & Johnson', 'Colgate-Palmolive', 'Unilever', 'Kimberly-Clark'],
    'Beauty': ['L’Oreal', 'Estée Lauder', 'Revlon', 'Maybelline', 'Clinique'],
    'Games': ['Nintendo', 'Sony', 'Microsoft', 'EA', 'Activision']
}

# Predefined product names for each category
product_names = {
    'Food': ['Cereal', 'Chips', 'Chocolate', 'Milk', 'Juice', 'Canned Beans', 'Pasta', 'Rice', 'Cookies', 'Bread'],
    'Electronic': ['Smartphone', 'Laptop', 'Headphones', 'Smartwatch', 'Television', 'Camera', 'Tablet', 'Speaker',
                   'Drone', 'Mouse'],
    'Health and Hygiene': ['Toothpaste', 'Shampoo', 'Hand Wash', 'Body Lotion', 'Deodorant', 'Face Cream',
                           'Sanitary Pads', 'Toilet Paper', 'Toothbrush', 'Soap'],
    'Beauty': ['Foundation', 'Lipstick', 'Mascara', 'Nail Polish', 'Moisturizer', 'Eye Shadow', 'Blush', 'Eyeliner',
               'Perfume', 'Hair Gel'],
    'Games': ['PlayStation', 'Xbox', 'Nintendo Switch', 'PC Game', 'Action Figure', 'Game Console', 'Board Game',
              'Puzzle', 'Card Game', 'Video Game']
}


# Function to generate a random price
def generate_price():
    return round(random.uniform(5, 500), 2)


# Open CSV file for writing
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Write header row
    writer.writerow(['product_id', 'name', 'category', 'brand', 'price'])

    # Generate 1000 product records
    for product_id in range(1, 1001):
        category = random.choice(categories)
        brand = random.choice(brands[category])
        name = random.choice(product_names[category])  # Select a random product name from the category
        price = generate_price()

        # Write product record
        writer.writerow([product_id, name, category, brand, price])

print("CSV file 'products.csv' generated with 1000 product records.")
