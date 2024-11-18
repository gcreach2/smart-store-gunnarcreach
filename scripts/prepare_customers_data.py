import pandas as pd

# Load raw customers data
customers = pd.read_csv('data/raw/customers_data.csv')

# 1. Remove duplicates
customers.drop_duplicates(inplace=True)

# 2. Handle missing values
customers['LoyaltyPoints'].fillna(0, inplace=True)  # Example: fill missing LoyaltyPoints with 0

# 3. Remove outliers in LoyaltyPoints (e.g., points above 5000 might be unrealistic)
customers = customers[customers['LoyaltyPoints'] <= 5000]

# 4. Standardize CustomerSegment values
customers['CustomerSegment'] = customers['CustomerSegment'].replace({
    'VIP': 'VIP', 'vip': 'VIP', 'Regular': 'Regular', 'regular': 'Regular'
})

# Save cleaned data
customers.to_csv('data/prepared/customers_data_prepared.csv', index=False)
print("Prepared customers data saved.")
import pandas as pd

# Load raw customers data
customers = pd.read_csv('data/raw/customers_data.csv')

# Initial record count
initial_count = len(customers)
print(f"Initial number of customers: {initial_count}")

# 1. Remove duplicates
customers.drop_duplicates(inplace=True)

# 2. Handle missing values
customers['LoyaltyPoints'].fillna(0, inplace=True)

# 3. Remove outliers in LoyaltyPoints (e.g., points above 5000 might be unrealistic)
customers = customers[customers['LoyaltyPoints'] <= 5000]

# 4. Standardize CustomerSegment values
customers['CustomerSegment'] = customers['CustomerSegment'].replace({
    'VIP': 'VIP', 'vip': 'VIP', 'Regular': 'Regular', 'regular': 'Regular'
})

# Prepared record count
prepared_count = len(customers)
print(f"Prepared number of customers: {prepared_count}")

# Save cleaned data
customers.to_csv('data/prepared/customers_data_prepared.csv', index=False)
print("Cleaned customer data has been saved to data/prepared/customers_data_prepared.csv")
