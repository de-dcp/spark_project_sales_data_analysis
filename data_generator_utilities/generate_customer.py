import csv
import random

# Define the file name for the CSV
filename = 'D:\SparkLearn\Spark_Sales_Data_Analysis\Output_Data\customer_data.csv'

# Define sample data for Indian names, cities, and states
first_names = ['Aarav', 'Vivaan', 'Aditya', 'Sai', 'Ishaan', 'Reyansh', 'Ayaan', 'Krishna', 'Arjun', 'Rohan',
               'Saanvi', 'Priya', 'Ananya', 'Isha', 'Aditi', 'Shruti', 'Madhuri', 'Neha', 'Pooja', 'Shreya']
last_names = ['Sharma', 'Patel', 'Verma', 'Yadav', 'Reddy', 'Gupta', 'Kumar', 'Singh', 'Mehta', 'Choudhary',
              'Jha', 'Desai', 'Rai', 'Bhatt', 'Joshi', 'Malhotra', 'Bansal', 'Chopra', 'Kapoor', 'Shukla']
cities = [
    "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Ahmedabad", "Chennai", "Kolkata", "Pune", "Jaipur", "Lucknow",
    "Kanpur", "Nagpur", "Indore", "Thane", "Bhopal", "Visakhapatnam", "Patna", "Vadodara", "Ghaziabad", "Ludhiana",
    "Agra", "Nashik", "Faridabad", "Meerut", "Rajkot", "Varanasi", "Srinagar", "Aurangabad", "Dhanbad", "Amritsar",
    "Navi Mumbai", "Allahabad", "Howrah", "Ranchi", "Gwalior", "Jabalpur", "Coimbatore", "Vijayawada", "Jodhpur", "Madurai",
    "Raipur", "Kota", "Guwahati", "Chandigarh", "Solapur", "Hubli", "Bareilly", "Mysore", "Tiruchirappalli", "Salem"
]

"""states = ['Maharashtra', 'Uttar Pradesh', 'Karnataka', 'Tamil Nadu', 'West Bengal', 'Andhra Pradesh', 'Gujarat',
          'Rajasthan',
          'Bihar', 'Madhya Pradesh', 'Punjab', 'Haryana', 'Kerala', 'Odisha', 'Uttarakhand', 'Assam', 'Jammu & Kashmir',
          'Chhattisgarh']
"""

genders = ['Male', 'Female', 'Other']


# Function to generate random customer data
def generate_customer_data(customer_id):
    name = f'{random.choice(first_names)} {random.choice(last_names)}'
    city = random.choice(cities)
    # state = random.choice(states)
    age = random.randint(18, 80)
    gender = random.choice(genders)

    return [customer_id, name, city, age, gender]


# Open the CSV file for writing
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Write the header
    writer.writerow(['customer_id', 'customer_name', 'city', 'age', 'gender'])

    # Generate data for 10,000 customers starting from customer_id 1000
    for customer_id in range(1000, 10000 + 1000):
        data = generate_customer_data(customer_id)
        writer.writerow(data)

print(f"CSV file '{filename}' created with 10,000 customer records.")
