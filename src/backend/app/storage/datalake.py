import duckdb
import pandas as pd
import os


class Datalake:
    def __init__(self) -> None:
        self.database_url = os.getenv("DATALAKE_URL")
        self.__duckdb = None

        # Set up AWS S3 credentials
        self.s3_key_id = os.getenv("AWS_ACCESS_KEY_ID")
        self.s3_secret = os.getenv("AWS_SECRET_ACCESS_KEY")
        self.s3_region = os.getenv("REGION")

    @property
    def duckdb(self) -> duckdb.DuckDBPyConnection:
        return self.__duckdb

    def __enter__(self):
        if self.__duckdb is None:
            if (
                self.s3_key_id is None
                or self.s3_secret is None
                or self.s3_region is None
            ):
                self.__duckdb = duckdb.connect(self.database_url)
            else:
                self.__duckdb = duckdb.connect()
                self.__duckdb.sql(
                    f"""
                    SET s3_region='{self.s3_region}';
                    SET s3_access_key_id='{self.s3_key_id}';
                    SET s3_secret_access_key='{self.s3_secret}';
                """
                )
        return self.duckdb

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.__duckdb:
            self.__duckdb.close()
            self.__duckdb = None


if __name__ == "__main__":
    import dotenv

    dotenv.load_dotenv()
    table_name = "testegd"

    # Sample DataFrame
    data = {"col_1": [3, 2, 1, 0], "col_2": ["a", "b", "c", "d"]}
    df = pd.DataFrame.from_dict(data)

    # Connect to DuckDB and create the table if it doesn't exist
    with Datalake() as client:
        # Create table based on DataFrame schema if it doesn't exist
        client.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                col_1 INTEGER,
                col_2 VARCHAR
            );
        """
        )

        # Register the DataFrame as a temporary DuckDB table
        client.register("df_temp", df)

        # Insert data into the table
        client.execute(f"INSERT INTO {table_name} SELECT * FROM df_temp")

        # Export the table to AWS S3 in CSV format
        s3_bucket = "s3://volksduckdb/testegd.csv"
        client.execute(
            f"COPY (SELECT * FROM {table_name}) TO '{s3_bucket}' (FORMAT CSV, HEADER TRUE);"
        )

        print(
            f"Data inserted into table '{table_name}' and exported to S3 bucket successfully."
        )
