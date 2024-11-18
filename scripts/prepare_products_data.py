import pandas as pd

# Load raw products data
products = pd.read_csv('data/raw/products_data.csv')

# 1. Remove duplicates
products.drop_duplicates(inplace=True)

# 2. Handle missing values (e.g., fill StockQuantity with 0 if missing)
products['StockQuantity'].fillna(0, inplace=True)

# 3. Remove outliers in UnitPrice (e.g., prices above 5000 might be unrealistic)
products = products[products['UnitPrice'] <= 5000]

# 4. Standardize StoreSection values (e.g., capitalize consistently)
products['StoreSection'] = products['StoreSection'].str.title()

# Save cleaned data
products.to_csv('data/prepared/products_data_prepared.csv', index=False)
print("Prepared products data saved.")
import pandas as pd

# Load raw products data
products = pd.read_csv('data/raw/products_data.csv')

# Initial record count
initial_count = len(products)
print(f"Initial number of products: {initial_count}")

# 1. Remove duplicates
products.drop_duplicates(inplace=True)

# 2. Handle missing values
products['StockQuantity'].fillna(0, inplace=True)

# 3. Remove outliers in StockQuantity (e.g., stock over 1000 might be unrealistic)
products = products[products['StockQuantity'] <= 1000]

# 4. Standardize Category values
products['Category'] = products['Category'].replace({
    'electronics': 'Electronics', 'clothing': 'Clothing'
})

# Prepared record count
prepared_count = len(products)
print(f"Prepared number of products: {prepared_count}")

# Save cleaned data
products.to_csv('data/prepared/products_data_prepared.csv', index=False)
print("Cleaned product data has been saved to data/prepared/products_data_prepared.csv")
