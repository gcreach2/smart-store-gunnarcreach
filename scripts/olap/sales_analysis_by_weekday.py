import pandas as pd
import matplotlib.pyplot as plt
import pathlib
import sys
from utils.logger import logger  # Make sure logger is working

# Constants
OLAP_OUTPUT_DIR: pathlib.Path = pathlib.Path("data").joinpath("olap_cubing_outputs")
CUBED_FILE: pathlib.Path = OLAP_OUTPUT_DIR.joinpath("multidimensional_olap_cube.csv")
RESULTS_OUTPUT_DIR: pathlib.Path = pathlib.Path("data").joinpath("results")

# Create output directory for results if it doesn't exist
RESULTS_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def load_olap_cube(file_path: pathlib.Path) -> pd.DataFrame:
    """Load the precomputed OLAP cube data."""
    try:
        logger.info(f"Loading OLAP cube from {file_path}")
        cube_df = pd.read_csv(file_path)
        logger.info(f"OLAP cube data successfully loaded from {file_path}.")
        return cube_df
    except Exception as e:
        logger.error(f"Error loading OLAP cube data: {e}")
        raise

def analyze_sales_by_weekday(cube_df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate total sales by DayOfWeek."""
    try:
        logger.info("Analyzing sales by weekday...")
        sales_by_weekday = (
    cube_df.groupby("DayOfWeek")["TotalSales"].sum().reset_index()
)

        sales_by_weekday.rename(columns={"sale_amount_usd_sum": "TotalSales"}, inplace=True)
        sales_by_weekday.sort_values(by="TotalSales", inplace=True)
        logger.info("Sales aggregated by DayOfWeek successfully.")
        return sales_by_weekday
    except Exception as e:
        logger.error(f"Error analyzing sales by DayOfWeek: {e}")
        raise

def identify_least_profitable_day(sales_by_weekday: pd.DataFrame) -> str:
    """Identify the day with the lowest total sales revenue."""
    try:
        least_profitable_day = sales_by_weekday.iloc[0]
        logger.info(f"Least profitable day: {least_profitable_day['DayOfWeek']} with revenue ${least_profitable_day['TotalSales']:.2f}.")
        return least_profitable_day["DayOfWeek"]
    except Exception as e:
        logger.error(f"Error identifying least profitable day: {e}")
        raise

def visualize_sales_by_weekday(sales_by_weekday: pd.DataFrame) -> None:
    """Visualize total sales by day of the week."""
    try:
        logger.info("Visualizing sales by weekday...")
        plt.figure(figsize=(10, 6))
        plt.bar(
            sales_by_weekday["DayOfWeek"],
            sales_by_weekday["TotalSales"],
            color="skyblue",
        )
        plt.title("Total Sales by Day of the Week", fontsize=16)
        plt.xlabel("Day of the Week", fontsize=12)
        plt.ylabel("Total Sales (USD)", fontsize=12)
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Save the visualization
        output_path = RESULTS_OUTPUT_DIR.joinpath("sales_by_day_of_week.png")
        plt.savefig(output_path)
        logger.info(f"Visualization saved to {output_path}.")
        plt.show()
    except Exception as e:
        logger.error(f"Error visualizing sales by day of the week: {e}")
        raise

def main():
    """Main function for analyzing and visualizing sales data."""
    logger.info("Starting SALES_LOW_REVENUE_DAYOFWEEK analysis...")

    # Step 1: Load the precomputed OLAP cube
    try:
        cube_df = load_olap_cube(CUBED_FILE)
    except Exception as e:
        logger.error(f"Failed to load OLAP cube: {e}")
        return

    # Step 2: Analyze total sales by DayOfWeek
    try:
        sales_by_weekday = analyze_sales_by_weekday(cube_df)
    except Exception as e:
        logger.error(f"Failed to analyze sales by weekday: {e}")
        return

    # Step 3: Identify the least profitable day
    try:
        least_profitable_day = identify_least_profitable_day(sales_by_weekday)
        logger.info(f"Least profitable day: {least_profitable_day}")
    except Exception as e:
        logger.error(f"Failed to identify least profitable day: {e}")
        return

    # Step 4: Visualize total sales by DayOfWeek
    try:
        visualize_sales_by_weekday(sales_by_weekday)
    except Exception as e:
        logger.error(f"Failed to visualize sales by weekday: {e}")
        return

    logger.info("Analysis and visualization completed successfully.")

if __name__ == "__main__":
    main()
