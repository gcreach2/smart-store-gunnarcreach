# Smart Store Data Warehouse

This project implements a data warehouse for the Smart Store. It includes data preparation, schema design, database implementation, ETL processes, OLAP cubing, and unit testing to ensure data quality. The data warehouse supports business intelligence by organizing and transforming raw data into meaningful insights.

---

## Project Structure

```
smart-store-gunnarcreach/
├── .venv/                     # Virtual environment
├── data/
│   ├── raw/                   # Raw data files
│   ├── prepared/              # Cleaned and prepared data files
│   ├── dw/                    # SQLite database storage
│       └── smart_sales.db     # SQLite database for the data warehouse
│   ├── olap_cubing_outputs/   # OLAP cubing output files
├── scripts/
│   ├── create_dw.py           # Database schema setup
│   ├── data_prep.py           # Data preparation script
│   ├── data_scrubber.py       # DataScrubber class for cleaning
│   ├── etl_to_dw.py           # ETL script for loading data into DW
│   ├── olap_cubing.py         # OLAP cubing script for analysis
├── tests/
│   ├── test_data_scrubber.py  # Unit tests for DataScrubber
├── utils/
│   ├── logger.py              # Logger utility
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Files to exclude from Git
```

---

## Setup Instructions

1. **Create a Virtual Environment**  
   Create a virtual environment to manage project dependencies:  
   ```bash
   python3 -m venv .venv
   ```

2. **Activate the Virtual Environment**  
   Activate the virtual environment:  
   - macOS/Linux:  
     ```bash
     source .venv/bin/activate
     ```

3. **Install Project Dependencies**  
   Upgrade pip and install required dependencies:  
   ```bash
   python3 -m pip install --upgrade pip
   python3 -m pip install --upgrade -r requirements.txt
   ```

4. **Set Up the SQLite Database**  
   Define and initialize the data warehouse schema:  
   ```bash
   python3 scripts/create_dw.py
   ```

5. **Clean and Prepare the Data**  
   Use the reusable `DataScrubber` class to clean and prepare raw data:  
   ```bash
   python3 scripts/data_prep.py
   ```

6. **Run Unit Tests for Data Cleaning**  
   Validate the `DataScrubber` class using the provided test suite:  
   ```bash
   PYTHONPATH=. python3 tests/test_data_scrubber.py
   ```

7. **Execute the ETL Process**  
   Run the ETL (Extract, Transform, Load) script to load prepared data into the data warehouse:  
   ```bash
   python3 scripts/etl_to_dw.py
   ```

8. **Run the OLAP Cubing Script**  
   Generate an OLAP cube for analysis:  
   ```bash
   python3 scripts/olap_cubing.py
   ```

9. **Commit and Push Changes to GitHub**  
   Commit your completed files to GitHub:  
   ```bash
   git add .
   git commit -m "Add completed project files"
   git push -u origin main
   ```

---

## Features

1. **Data Preparation**
   - Cleans raw data by removing duplicates, handling missing values, and filtering outliers.
   - Utilizes a reusable `DataScrubber` class for modular cleaning.

2. **Database Implementation**
   - Implements a star schema in SQLite with the following tables:
     - `sales` (Fact Table)
     - `products` (Dimension Table)
     - `customers` (Dimension Table)
     - Additional optional dimension tables (e.g., `stores`).

3. **ETL Process**
   - Extracts data from prepared CSV files.
   - Transforms and loads the data into the SQLite database using an automated ETL script.

4. **OLAP Cubing**
   - Generates a multidimensional OLAP cube for analysis.
   - Outputs insights into a CSV file for further reporting or visualization.

5. **Data Quality Testing**
   - Includes unit tests for data cleaning methods with `tests/test_data_scrubber.py`.

6. **Logging**
   - Provides consistent logging with the `utils/logger.py` module.

---

## Database Schema

### Star Schema Overview
The database is structured using a star schema to optimize query performance for analytical tasks.

### Fact Table: `sales`
| Column Name   | Data Type | Description                     |
|---------------|-----------|---------------------------------|
| sale_id       | INTEGER   | Primary key                    |
| customer_id   | INTEGER   | Foreign key referencing customers |
| product_id    | INTEGER   | Foreign key referencing products |
| quantity      | INTEGER   | Quantity of items sold         |
| sales_amount  | REAL      | Total sales amount             |

### Dimension Table: `products`
| Column Name   | Data Type | Description                     |
|---------------|-----------|---------------------------------|
| product_id    | INTEGER   | Primary key                    |
| product_name  | TEXT      | Name of the product            |
| category      | TEXT      | Product category               |
| unit_price    | REAL      | Price per unit                 |

### Dimension Table: `customers`
| Column Name   | Data Type | Description                     |
|---------------|-----------|---------------------------------|
| customer_id   | INTEGER   | Primary key                    |
| name          | TEXT      | Customer name                  |
| region        | TEXT      | Customer region                |
| join_date     | TEXT      | Date when the customer joined  |

### OLAP Analysis
Business Insights
Goal: Analyze sales trends by day of the week to optimize staffing and inventory planning.

Data Source:

sales table in the data warehouse.
Columns: SaleDate, DayOfWeek, SaleAmount, ProductID, CustomerID.
Key Metrics:

Total Sales (SUM(SaleAmount)): To identify the most profitable days.
Average Sales (AVG(SaleAmount)): To gauge consistency in sales.
Sales Count (COUNT(TransactionID)): To assess customer activity.
Analysis Workflow:

Extracted SaleDate and transformed it to DayOfWeek.
Aggregated data to create an OLAP cube with metrics grouped by DayOfWeek, ProductID, and CustomerID.
Results
The analysis revealed:

High Sales Days: Friday and Saturday consistently had the highest sales volumes.
Low Sales Days: Tuesday and Wednesday experienced the lowest activity.
Actionable Insight: Focus marketing efforts on low-performing days and ensure optimal inventory for high-performing days.

## ETL Process

### Steps:
1. **Extract**  
   Reads prepared CSV files from `data/prepared/`:
   - `customers_data_prepared.csv`
   - `products_data_prepared.csv`
   - `sales_data_prepared.csv`

2. **Transform**  
   - Maps CSV columns to database schema columns.
   - Ensures data integrity and consistency.

3. **Load**  
   - Inserts data into SQLite tables:
     - `customers`
     - `products`
     - `sales`

---

## OLAP Cubing

### Workflow:
1. **Dimensions**  
   - Day of the Week
   - Product ID
   - Customer ID

2. **Metrics**  
   - Total sales amount
   - Average sales amount
   - Count of sales transactions
   - Transaction IDs (concatenated)

3. **Output**  
   - OLAP cube stored in `data/olap_cubing_outputs/olap_cube.csv`

---

## Validation and Testing

### Unit Tests
Run the test suite to ensure data cleaning and preparation methods are working as intended:
```bash
PYTHONPATH=. python3 tests/test_data_scrubber.py
```

### Verification
Verify the ETL and OLAP cubing processes by inspecting the populated tables in `smart_sales.db` and reviewing the OLAP cube output.

---

## The Business Goal

### Goal: 
To analyze the impact of discounts on sales performance by day of the week, allowing the business to identify the best and worst-performing days for sales driven by discounts. This insight supports optimizing discount campaigns.

---

## Data Source

- **Source:** Data warehouse (`smart_sales.db`)
- **Tables Used:**
  - `sales`: Columns - `sale_id`, `customer_id`, `product_id`, `sale_date`, `sales_amount`, `discount_percent`, `store_id`
  - `products`: Columns - `product_id`, `product_name`, `category`
  - `customers`: Columns - `customer_id`, `name`, `region`
  
---

## Tools

- **Python:** For ETL, OLAP analysis, and scripting.
- **SQLite:** Lightweight database for managing the data warehouse.
- **Pandas:** For data manipulation and analysis.
- **Logging:** To track script execution and errors.

---

## Workflow & Logic

- Dimensions: `DayOfWeek`, `StoreID`, `DiscountPercent`
- Metrics: 
  - `TotalSales` (Sum of `sales_amount`)
  - `AverageSales` (Average of `sales_amount`)
  - `TransactionCount` (Count of `sale_id`)
- Aggregations: Grouped by day of the week, store, and discount percentage.

---

## Results

The analysis revealed that discounts had the highest impact on sales performance on Fridays, with average sales being 15% higher than the weekly average. This suggests Friday discounts are particularly effective in driving revenue.

### Suggested Actions:
- Implement larger discount campaigns on Fridays.
- Consider extending campaigns to Thursdays, which showed only slightly lower performance.

---

## Challenges

### Encountered:
- Issues with SQL queries not matching column names in the database.
- Errors due to mismatched date formats between database tables and Python.

### Resolved:
- Validated column names against the database schema.
- Standardized date formats using `Pandas` before analysis.

---

## Contributions

Contributions are welcome! Submit pull requests or open issues for suggestions or bug reports.
