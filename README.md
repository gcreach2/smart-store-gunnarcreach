# Smart Store Data Warehouse

This project implements a data warehouse for the Smart Store. It includes data preparation, schema design, database implementation, ETL processes, OLAP cubing, and unit testing to ensure data quality. The data warehouse supports business intelligence by organizing and transforming raw data into meaningful insights.

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
│   ├── olap/
│       ├── olap_cubing.py     # OLAP cubing script for analysis
├── tests/
│   ├── test_data_scrubber.py  # Unit tests for DataScrubber
├── utils/
│   ├── logger.py              # Logger utility
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Files to exclude from Git
```

## Setup Instructions

1. **Create a Virtual Environment**

Create a virtual environment to manage project dependencies:

```bash
python3 -m venv .venv
```

2. **Activate the Virtual Environment**

Activate the virtual environment:

macOS/Linux:
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

Use the reusable DataScrubber class to clean and prepare raw data:

```bash
python3 scripts/data_prep.py
```

6. **Run Unit Tests for Data Cleaning**

Validate the DataScrubber class using the provided test suite:

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
python3 scripts/olap/olap_cubing.py
```

9. **Commit and Push Changes to GitHub**

Commit your completed files to GitHub:

```bash
git add .
git commit -m "Add completed project files"
git push -u origin main
```

## Features

### 1. Data Preparation

- Cleans raw data by removing duplicates, handling missing values, and filtering outliers.
- Utilizes a reusable DataScrubber class for modular cleaning.

### 2. Database Implementation

- Implements a star schema in SQLite with the following tables:
  - `sales` (Fact Table)
  - `products` (Dimension Table)
  - `customers` (Dimension Table)
  - Additional optional dimension tables (e.g., stores).

### 3. ETL Process

- Extracts data from prepared CSV files.
- Transforms and loads the data into the SQLite database using an automated ETL script.

### 4. OLAP Cubing

- Generates a multidimensional OLAP cube for analysis.
- Outputs insights into a CSV file for further reporting or visualization.

### 5. Data Quality Testing

- Includes unit tests for data cleaning methods with `tests/test_data_scrubber.py`.

### 6. Logging

- Provides consistent logging with the `utils/logger.py` module.

## Database Schema

### Star Schema Overview

The database is structured using a star schema to optimize query performance for analytical tasks.

**Fact Table: sales**

| Column Name   | Data Type | Description                          |
|---------------|-----------|--------------------------------------|
| sale_id       | INTEGER   | Primary key                         |
| customer_id   | INTEGER   | Foreign key referencing customers   |
| product_id    | INTEGER   | Foreign key referencing products    |
| quantity      | INTEGER   | Quantity of items sold              |
| sales_amount  | REAL      | Total sales amount                  |

**Dimension Table: products**

| Column Name   | Data Type | Description                          |
|---------------|-----------|--------------------------------------|
| product_id    | INTEGER   | Primary key                         |
| product_name  | TEXT      | Name of the product                 |
| category      | TEXT      | Product category                    |
| unit_price    | REAL      | Price per unit                      |

**Dimension Table: customers**

| Column Name   | Data Type | Description                          |
|---------------|-----------|--------------------------------------|
| customer_id   | INTEGER   | Primary key                         |
| name          | TEXT      | Customer name                       |
| region        | TEXT      | Customer region                     |
| join_date     | TEXT      | Date when the customer joined       |

## OLAP Analysis of Sales by Weekday

### Goal:
The goal of this OLAP analysis is to determine which day of the week consistently shows the lowest sales revenue. This insight will help inform decisions about reducing operating hours or focusing marketing efforts on less profitable days.

### Process:
1. **Load Precomputed OLAP Cube:** The script loads a precomputed OLAP cube, which contains aggregated sales data across different dimensions like `DayOfWeek`, `ProductID`, and `CustomerID`.
   
2. **Analyze Sales by Weekday:**
   - The script groups transactions by the `DayOfWeek` column.
   - It then aggregates the total sales (`sale_amount_usd_sum`) for each day of the week.
   - The goal is to identify the day with the lowest sales total.

3. **Visualization:** The script also generates a bar plot that visualizes total sales by each day of the week.

### Key Columns:
- **DayOfWeek**: The day of the week (e.g., Monday, Tuesday, etc.).
- **sale_amount_usd_sum**: The sum of sales on that day.

### Issue:
During the execution, an error occurred because the expected column `sale_amount_usd_sum` was not found in the OLAP cube.

#### How to Resolve:
1. **Check Column Names in the OLAP Cube:**
   - Open the cube file (`multidimensional_olap_cube.csv`) to verify the exact column names.

2. **Update the Script:**
   - After confirming the correct column names in the cube, update the analysis script to reference the correct column name. For example:
     - If the correct column name for sales is `TotalSales`, update the script to use `TotalSales` instead of `sale_amount_usd_sum`.
     
   Example:
   ```python
   sales_by_weekday = (
       cube_df.groupby("DayOfWeek")["TotalSales"].sum().reset_index()
   )


**Unit Tests**

Run the test suite to ensure data cleaning and preparation methods are working as intended:

```bash
PYTHONPATH=. python3 tests/test_data_scrubber.py
```

**Verification**

Verify the ETL and OLAP cubing processes by inspecting the populated tables in `smart_sales.db` and reviewing the OLAP cube output.

# Smart Store Data Warehouse - Spark Pipeline

## GETTING STARTED

### Set up your machine (1 hour)
Follow the instructions to set up your system first:

- **[Setup for macOS/Linux](#)** 

### Activate your local virtual environment & install dependencies (30-40 minutes)
1. Update the smart sales repository layout (or update scripts to utilize current layout) to match the below:
    ```
    project/
    ├── data/prepared
    │   ├── customers_data_prepared.csv
    │   ├── products_data_prepared.csv
    │   ├── sales_data_prepared.csv
    ├── scripts/
    │   ├── step0-pipeline.py           # Orchestrate the pipeline
    │   ├── step1-extract.py            # Extract stage: Read data from sources
    │   ├── step2-transform.py          # Transform stage: Process data for insights
    │   ├── step3-load.py               # Load stage: Save results to storage
    │   ├── step4-visualize.py          # Visualize results using seaborn or matplotlib
    ├── notebooks/
    │   ├── insights.ipynb             # Notebook orchestrating extract-transform-load (ETL) + visualization
    ├── .gitignore
    ├── README.md
    └── requirements.txt
    ```

2. Follow these steps to manage the local environment:
    **[Virtual Environment](#)**

### Run PySpark Basic Script (20 minutes)
1. In VS Code, open a PowerShell terminal in the root project folder.

2. Activate your local project environment every time you open a terminal to work on the project:
    ```bash
    source .venv/bin/activate  # For macOS/Linux
    ```

3. Execute the script:
    ```bash
    python3 scripts/step0-pipeline.py
    ```

4. Protip: After running the command once, you can usually get it back by typing just the initial `py` or `python` and then hitting the right arrow key – or use the up arrow to access prior commands.

### Enhance Functionality (1-2 hours)
Add or update the files to make your own functionality:
- Paste the contents from the file provided in this repo.
- Execute your scripts or experiment with a Jupyter notebook.

### Troubleshooting (20-60 minutes)
If you encounter issues, ensure the correct paths are set in your environment:
```bash
$Env:HADOOP_HOME = "C:\Hadoop"
Test-Path "$Env:HADOOP_HOME\bin\winutils.exe"


## Contributions

Contributions are welcome! Submit pull requests or open issues for suggestions or bug reports.
