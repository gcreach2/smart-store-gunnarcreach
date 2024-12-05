from pyspark.sql import SparkSession
from scripts.step1_extract import read_csv  # Import your extraction function

def main():
    """
    Main function to run the ETL pipeline.
    """
    spark = SparkSession.builder.appName("Spark Sales Analysis").getOrCreate()

    try:
        # File paths for your data
        data_dir = "data/"  # Adjust the path as needed
        products_file = data_dir + "prepared/products_data_prepared.csv"
        sales_file = data_dir + "prepared/sales_data_prepared.csv"

        # Step 1: Extract
        products_df = read_csv(spark, products_file)
        sales_df = read_csv(spark, sales_file)

        # Step 2: Transform (other transformations can go here)
        # Example transformation (you can add your actual transformation functions)
        # transformed_df = some_transformation(sales_df)

        print(f"Data extraction complete! Products: {products_df.count()} rows, Sales: {sales_df.count()} rows.")

    finally:
        spark.stop()

if __name__ == "__main__":
    main()
