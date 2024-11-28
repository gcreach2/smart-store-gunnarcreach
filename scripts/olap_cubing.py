import sqlite3
import pandas as pd
import pathlib
import sys

# Constants
DW_DIR = pathlib.Path("data").joinpath("dw")
DB_PATH = DW_DIR.joinpath("smart_sales.db")
OUTPUT_DIR = pathlib.Path("data").joinpath("olap_cubing_outputs")
OUTPUT_FILE = OUTPUT_DIR.joinpath("olap_cube.csv")


def create_olap_cube() -> None:
    """Generate an OLAP cube and save it as a CSV file."""
    conn = None
    try:
        # Ensure output directory exists
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        print("Output directory ensured.")

        # Connect to the SQLite database
        conn = sqlite3.connect(DB_PATH)
        print("Connected to SQLite database.")

        # SQL query to generate the OLAP cube
        query = """
        SELECT 
            strftime('%w', SaleDate) AS DayOfWeek,
            ProductID,
            CustomerID,
            SUM(SaleAmount) AS TotalSales,
            AVG(SaleAmount) AS AvgSales,
            COUNT(TransactionID) AS SalesCount,
            GROUP_CONCAT(TransactionID) AS TransactionIDs
        FROM sales
        GROUP BY DayOfWeek, ProductID, CustomerID
        ORDER BY DayOfWeek, ProductID, CustomerID;
        """

        # Execute the query and save the results to a DataFrame
        cube_df = pd.read_sql_query(query, conn)
        print("OLAP cube query executed successfully.")

        # Map day_of_week numbers to weekday names
        day_map = {
            "0": "Sunday", "1": "Monday", "2": "Tuesday",
            "3": "Wednesday", "4": "Thursday", "5": "Friday", "6": "Saturday"
        }
        cube_df["DayOfWeek"] = cube_df["DayOfWeek"].map(day_map)

        # Save the cube to a CSV file
        cube_df.to_csv(OUTPUT_FILE, index=False)
        print(f"OLAP cube saved to {OUTPUT_FILE}.")

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if conn:
            conn.close()
            print("SQLite connection closed.")


def main() -> None:
    """Main function to create the OLAP cube."""
    print("Starting OLAP cubing process...")
    create_olap_cube()
    print("OLAP cubing process completed.")


if __name__ == "__main__":
    main()