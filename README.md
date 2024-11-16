# Smart Store Data Warehouse

This project implements a data warehouse for the Smart Store. It includes data preparation, schema design, database implementation, and unit testing to ensure data quality. The data warehouse supports business intelligence by organizing and transforming raw data into meaningful insights.

---

## Project Structure

The project is organized into the following structure:

```
smart-store-gunnarcreach/
├── .venv/                     # Virtual environment
├── data/
│   ├── raw/                   # Raw data files
│   ├── prepared/              # Cleaned and prepared data files
│   ├── dw/                    # SQLite database storage
├── scripts/
│   ├── create_dw.py           # Database schema setup
│   ├── data_prep.py           # Data preparation script
│   ├── data_scrubber.py       # DataScrubber class for cleaning
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

Follow these steps to set up and run the project:

### 1. Create a Virtual Environment
Create a virtual environment to manage project dependencies:
```bash
python3 -m venv .venv
```

### 2. Activate the Virtual Environment
Activate the virtual environment:
- **macOS/Linux**:
  ```bash
  source .venv/bin/activate
  ```
- **Windows**:
  ```bash
  .\.venv\Scripts\activate
  ```

### 3. Install Project Dependencies
Upgrade pip and install required dependencies:
```bash
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade -r requirements.txt
```

### 4. Organize Project Files
Create and organize project files:
- **Logger Utility**: Add starter code to `utils/logger.py`.
- **Data Preparation**: Add starter code to `scripts/data_prep.py`.

### 5. Set Up the SQLite Database
Define and initialize the data warehouse schema:
```bash
python3 scripts/create_dw.py
```

### 6. Clean and Prepare the Data
Use the reusable `DataScrubber` class to clean and prepare raw data:
```bash
python3 scripts/data_prep.py
```

### 7. Run Unit Tests for Data Cleaning
Validate the `DataScrubber` class using the provided test suite:
```bash
PYTHONPATH=. python3 tests/test_data_scrubber.py
```

### 8. Commit and Push Changes to GitHub
Commit your completed files to GitHub:
```bash
git add .
git commit -m "Add completed project files"
git push -u origin main
```

---

## Features

1. **Data Preparation**:
   - Cleans raw data by removing duplicates, handling missing values, and filtering outliers.
   - Uses a reusable `DataScrubber` class for modular cleaning.

2. **Database Implementation**:
   - Implements a star schema in SQLite with tables for `sales`, `products`, `customers`, and `dates`.
   - Schema setup is automated with `scripts/create_dw.py`.

3. **Data Quality Testing**:
   - Includes unit tests for data cleaning methods using the `tests/test_data_scrubber.py` file.

4. **Logging**:
   - Provides a utility (`utils/logger.py`) for consistent logging throughout the project.

---

## Database Schema

The project uses a star schema with the following tables:

### 1. `sales` Table (Fact Table)
| Column Name  | Data Type   | Description                     |
|--------------|-------------|---------------------------------|
| sale_id      | INTEGER     | Primary key                    |
| customer_id  | INTEGER     | Foreign key referencing `customers` |
| product_id   | INTEGER     | Foreign key referencing `products` |
| quantity     | INTEGER     | Quantity of items sold         |
| sales_amount | REAL        | Total sales amount             |

### 2. `products` Table (Dimension Table)
| Column Name  | Data Type   | Description                     |
|--------------|-------------|---------------------------------|
| product_id   | INTEGER     | Primary key                    |
| product_name | TEXT        | Name of the product            |
| category     | TEXT        | Product category               |
| unit_price   | REAL        | Price per unit                 |

### 3. `customers` Table (Dimension Table)
| Column Name  | Data Type   | Description                     |
|--------------|-------------|---------------------------------|
| customer_id  | INTEGER     | Primary key                    |
| name         | TEXT        | Customer name                  |
| region       | TEXT        | Customer region                |
| join_date    | TEXT        | Date when the customer joined  |



---

## Contributions

Contributions are welcome! Submit pull requests or open issues for suggestions or bug reports.

---

