import pandas as pd

# Load raw sales data
sales = pd.read_csv('data/raw/sales_data.csv')

# 1. Remove duplicates
sales.drop_duplicates(inplace=True)

# 2. Handle missing values in SaleAmount by filling with the median
sales['SaleAmount'].fillna(sales['SaleAmount'].median(), inplace=True)

# 3. Remove outliers in SaleAmount using the interquartile range (IQR)
q1 = sales['SaleAmount'].quantile(0.25)
q3 = sales['SaleAmount'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
sales = sales[(sales['SaleAmount'] >= lower_bound) & (sales['SaleAmount'] <= upper_bound)]

# 4. Standardize PaymentType values (e.g., capitalize values)
sales['PaymentType'] = sales['PaymentType'].str.capitalize()

# Save cleaned data
sales.to_csv('data/prepared/sales_data_prepared.csv', index=False)
print("Prepared sales data saved.")
import pandas as pd

# Load raw sales data
sales = pd.read_csv('data/raw/sales_data.csv')

# Initial record count
initial_count = len(sales)
print(f"Initial number of sales: {initial_count}")

# 1. Remove duplicates
sales.drop_duplicates(inplace=True)

# 2. Handle missing values
sales['DiscountPercent'].fillna(0, inplace=True)

# 3. Remove outliers in SaleAmount (e.g., amounts over 10,000 might be unrealistic)
sales = sales[sales['SaleAmount'] <= 10000]

# 4. Standardize PaymentType values
sales['PaymentType'] = sales['PaymentType'].replace({
    'cash': 'Cash', 'credit': 'Credit'
})

# Prepared record count
prepared_count = len(sales)
print(f"Prepared number of sales: {prepared_count}")

# Save cleaned data
sales.to_csv('data/prepared/sales_data_prepared.csv', index=False)
print("Cleaned sales data has been saved to data/prepared/sales_data_prepared.csv")
