"""
Module 6: OLAP and Cubing Script
File: scripts/olap/product_performance_by_day.py

Purpose: Analyze product performance by day of the week.

This script performs OLAP-style analysis to aggregate product sales data
from a data warehouse, grouping by day of the week and product. 
The results are saved to a CSV file.
"""

import pandas as pd
import sqlite3
import pathlib
import sys

# Adjust the import path so it correctly finds the logger in the utils folder
PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent  # Going up three levels to the root
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from utils.logger import logger  # Now the logger can be imported

# Constants
DW_DIR = pathlib.Path("data").joinpath("dw")
DB_PATH = DW_DIR.joinpath("smart_sales.db")
OLAP_OUTPUT_DIR = pathlib.Path("data").joinpath("olap_cubing_outputs")

# Ensure the output directory exists
OLAP_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def ingest_sales_data_from_dw() -> pd.DataFrame:
    """Ingest sales data from SQLite data warehouse."""
    try:
        conn = sqlite3.connect(DB_PATH)
        sales_df = pd.read_sql_query("SELECT * FROM sales", conn)
        conn.close()
        logger.info("Sales data successfully loaded from SQLite data warehouse.")
        return sales_df
    except Exception as e:
        logger.error(f"Error loading sales table data from data warehouse: {e}")
        raise

def create_product_performance_cube(sales_df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate sales data by product and day of the week."""
    try:
        # Ensure SaleDate is in correct format
        sales_df["SaleDate"] = pd.to_datetime(sales_df["SaleDate"], errors='coerce')

        # Add DayOfWeek
        sales_df["DayOfWeek"] = sales_df["SaleDate"].dt.day_name()

        # Aggregate the sales data
        grouped = sales_df.groupby(["DayOfWeek", "ProductID"]).agg(
            TotalSales=("SaleAmount", "sum"),
            AvgSales=("SaleAmount", "mean"),
            SalesCount=("TransactionID", "count")
        ).reset_index()

        logger.info("Product performance cube created successfully.")
        return grouped
    except Exception as e:
        logger.error(f"Error creating product performance cube: {e}")
        raise

def write_cube_to_csv(cube: pd.DataFrame, filename: str) -> None:
    """Write the OLAP cube to a CSV file."""
    try:
        output_path = OLAP_OUTPUT_DIR.joinpath(filename)
        cube.to_csv(output_path, index=False)
        logger.info(f"OLAP cube saved to {output_path}.")
    except Exception as e:
        logger.error(f"Error saving OLAP cube to CSV file: {e}")
        raise

def main():
    """Main function for OLAP cubing."""
    logger.info("Starting OLAP Cubing process for product performance by day...")
    sales_df = ingest_sales_data_from_dw()
    product_performance_cube = create_product_performance_cube(sales_df)
    write_cube_to_csv(product_performance_cube, "product_performance_by_day.csv")
    logger.info("OLAP Cubing process completed successfully.")
    logger.info(f"Please see outputs in {OLAP_OUTPUT_DIR}")

if __name__ == "__main__":
    main()
