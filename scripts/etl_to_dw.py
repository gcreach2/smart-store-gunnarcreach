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

        # Load customers
        customers.to_sql("customers", conn, if_exists="replace", index=False)
        logger.info("Customers table loaded successfully.")

        # Load products
        products.to_sql("products", conn, if_exists="replace", index=False)
        logger.info("Products table loaded successfully.")

        # Load sales
        sales.to_sql("sales", conn, if_exists="replace", index=False)
        logger.info("Sales table loaded successfully.")

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


def main() -> None:
    """Main function for running the ETL process."""
    logger.info("Starting etl_to_dw ...")
    load_data_to_db()
    logger.info("ETL process completed successfully.")


if __name__ == "__main__":
    main()
