"""
Module 5: ETL to Data Warehouse Script
File: scripts/etl_to_dw.py
This script handles the ETL (Extract, Transform, Load) process. It extracts prepared data
from 'data/prepared/', transforms it (if needed), and loads it into the 'data/smart_sales.db' database.
"""

import pandas as pd
import sqlite3
import sys
import pathlib

# For local imports, temporarily add project root to Python sys.path
PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

# Now we can import local modules
from utils.logger import logger  # noqa: E402

# Constants
DW_DIR: pathlib.Path = pathlib.Path("data").joinpath("dw")
DB_PATH: pathlib.Path = DW_DIR.joinpath("smart_sales.db")
PREPARED_DATA_DIR: pathlib.Path = pathlib.Path("data").joinpath("prepared")


def transform_sales_data(sales: pd.DataFrame) -> pd.DataFrame:
    """Transform sales data to ensure proper date formatting."""
    try:
        sales['SaleDate'] = pd.to_datetime(sales['SaleDate']).dt.strftime('%Y-%m-%d')
        logger.info("SaleDate column transformed to YYYY-MM-DD format.")
        return sales
    except Exception as e:
        logger.error(f"Error transforming sales data: {e}")
        raise


def load_data_to_db() -> None:
    """Load prepared data into the data warehouse using the correct table names."""
    conn = None
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        logger.info("Connection to SQLite database established.")

        # Load prepared data
        customers = pd.read_csv(PREPARED_DATA_DIR.joinpath("customers_data_prepared.csv"))
        products = pd.read_csv(PREPARED_DATA_DIR.joinpath("products_data_prepared.csv"))
        sales = pd.read_csv(PREPARED_DATA_DIR.joinpath("sales_data_prepared.csv"))

        logger.info("Prepared data loaded into DataFrames.")

        # Transform sales data
        sales = transform_sales_data(sales)

        # Load customers
        customers.to_sql("customers", conn, if_exists="replace", index=False)
        logger.info("Customers table loaded successfully.")

        # Load products
        products.to_sql("products", conn, if_exists="replace", index=False)
        logger.info("Products table loaded successfully.")

        # Load sales
        sales.to_sql("sales", conn, if_exists="replace", index=False)
        logger.info("Sales table loaded successfully.")

        # Verify data load
        verify_data_load(conn)

    except sqlite3.Error as e:
        logger.error(f"Database error during ETL: {e}")
    except FileNotFoundError as e:
        logger.error(f"File not found during ETL: {e}")
    except Exception as e:
        logger.error(f"Unexpected error during ETL: {e}")
    finally:
        if conn:
            conn.close()
            logger.info("SQLite connection closed.")


def verify_data_load(conn: sqlite3.Connection) -> None:
    """Verify that the sales table is populated correctly."""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM sales;")
        count = cursor.fetchone()[0]
        logger.info(f"Sales table contains {count} records.")

        # Optional: Preview a few records
        cursor.execute("SELECT * FROM sales LIMIT 5;")
        logger.info("Preview of sales table:")
        for row in cursor.fetchall():
            logger.info(row)

    except sqlite3.Error as e:
        logger.error(f"Error verifying data load: {e}")


def main() -> None:
    """Main function for running the ETL process."""
    logger.info("Starting etl_to_dw ...")
    load_data_to_db()
    logger.info("ETL process completed successfully.")


if __name__ == "__main__":
    main()
