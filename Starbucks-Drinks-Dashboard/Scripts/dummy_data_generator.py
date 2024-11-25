# !pip install faker # Install if not already
import pandas as pd
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Beverage categories, beverages, and preparations to randomize
beverage_categories = ['Tea', 'Smoothie', 'Soda', 'Coffee', 'Juice']
beverages = ['Orange Juice', 'Mango Smoothie', 'Espresso', 'Green Tea', 'Cola', 'Latte', 'Lemonade', 'Iced Tea']
beverage_preps = ['Hot', 'Iced', 'Blended']

# Generate the dummy data
data = {
    "Beverage_category": [random.choice(beverage_categories) for _ in range(1000)],
    "Beverage": [random.choice(beverages) for _ in range(1000)],
    "Beverage_prep": [random.choice(beverage_preps) for _ in range(1000)],
    "Calories": [random.randint(50, 500) for _ in range(1000)],
    "Total Fat (g)": [round(random.uniform(0, 20), 1) for _ in range(1000)],
    "Trans Fat (g)": [round(random.uniform(0, 5), 1) for _ in range(1000)],
    "Saturated Fat (g)": [round(random.uniform(0, 10), 1) for _ in range(1000)],
    "Sodium (mg)": [random.randint(0, 500) for _ in range(1000)],
    "Total Carbohydrates (g)": [round(random.uniform(0, 100), 1) for _ in range(1000)],
    "Cholesterol (mg)": [random.randint(0, 100) for _ in range(1000)],
    "Dietary Fibre (g)": [round(random.uniform(0, 10), 1) for _ in range(1000)],
    "Sugars (g)": [round(random.uniform(0, 50), 1) for _ in range(1000)],
    "Protein (g)": [round(random.uniform(0, 30), 1) for _ in range(1000)],
    "Vitamin A (% DV)": [random.randint(0, 100) for _ in range(1000)],
    "Vitamin C (% DV)": [random.randint(0, 100) for _ in range(1000)],
    "Calcium (% DV)": [random.randint(0, 100) for _ in range(1000)],
    "Iron (% DV)": [random.randint(0, 100) for _ in range(1000)],
    "Caffeine (mg)": [random.randint(0, 300) for _ in range(1000)],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('../Starbucks-Drinks-Dashboard/Data/beverages_data.csv', index=False)
