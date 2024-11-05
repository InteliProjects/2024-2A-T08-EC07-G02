from storage import Datalake
import pandas as pd
from typing import Optional


class DatalakeService:
    @staticmethod
    def create_table(df: pd.DataFrame, table_name: str) -> None:
        with Datalake() as client:
            client.from_df(df).create(table_name)
            print(f"Table '{table_name}' created successfully.")

    @staticmethod
    def insert_table(df: pd.DataFrame, table_name: str) -> None:
        with Datalake() as client:
            client.execute(f"INSERT INTO {table_name} SELECT * FROM df", {"df": df})
            print(f"Data inserted into table '{table_name}' successfully.")

    @staticmethod
    def delete_table(table_name: str) -> None:
        with Datalake() as client:
            client.execute(f"DROP TABLE IF EXISTS {table_name}")
            print(f"Table '{table_name}' deleted successfully.")

    @staticmethod
    def list_tables() -> pd.DataFrame:
        with Datalake() as client:
            df = client.execute("SHOW TABLES").fetchdf()
            print("List of tables retrieved successfully.")
            return df

    @staticmethod
    def load_parquet(file_path: str) -> pd.DataFrame:
        with Datalake() as client:
            df = client.read_parquet(file_path).df()
            print(f"Parquet file '{file_path}' loaded successfully.")
            return df

    @staticmethod
    def load_csv(file_path: str) -> pd.DataFrame:
        with Datalake() as client:
            df = client.read_csv_auto(file_path).df()
            print(f"CSV file '{file_path}' loaded successfully.")
            return df

    @staticmethod
    def export_csv(table_name: str, to_file: str):
        with Datalake() as client:
            client.execute(
                f"COPY {table_name} TO '{to_file}' WITH (FORMAT CSV, HEADER TRUE)"
            )
            print(f"Table '{table_name}' exported to CSV '{to_file}' successfully.")

    @staticmethod
    def export_parquet(table_name: str, to_file: str):
        with Datalake() as client:
            client.execute(f"COPY {table_name} TO '{to_file}' (FORMAT PARQUET)")
            print(f"Table '{table_name}' exported to Parquet '{to_file}' successfully.")

    @staticmethod
    def query_df(query: str) -> pd.DataFrame:
        with Datalake() as client:
            df = client.execute(query).fetchdf()
            print(f"Query executed successfully: {query}")
            return df

    @staticmethod
    def query_list(query: str) -> list:
        with Datalake() as client:
            result = client.execute(query).fetchall()
            print(f"Query executed successfully: {query}")
            return result

    @staticmethod
    def execute_transaction(sql_statements: list):
        with Datalake() as client:
            client.begin()
            try:
                for stmt in sql_statements:
                    client.execute(stmt)
                client.commit()
                print("Transaction executed successfully.")
            except Exception as e:
                client.rollback()
                print("Transaction failed and rolled back.")
                raise e

    @staticmethod
    def execute(query: str):
        with Datalake() as client:
            result = client.execute(query)
            print(f"Executed command: {query}")
            return result

    @staticmethod
    def get_table(table_name: str) -> pd.DataFrame:
        with Datalake() as client:
            df = client.execute(f"SELECT * FROM {table_name}").fetchdf()
            print(f"Table '{table_name}' retrieved successfully.")
            return df

    @staticmethod
    def get_table_paginator(
        table_name: str,
        page: int = 0,
        per_page: int = 10,
        knr_query: Optional[str] = None,
    ) -> tuple[list[dict], int]:
        with Datalake() as client:
            offset = page * per_page

            if knr_query:
                data_query = (
                    f"SELECT * FROM {table_name} WHERE KNR LIKE '%{knr_query}%'"
                    f"LIMIT {per_page} OFFSET {offset}"
                )
                count_query = (
                    f"SELECT COUNT(*) FROM {table_name} WHERE KNR LIKE '%{knr_query}%'"
                )
            else:
                data_query = (
                    f"SELECT * FROM {table_name} LIMIT {per_page} OFFSET {offset}"
                )
                count_query = f"SELECT COUNT(*) FROM {table_name}"

            df = client.execute(data_query).fetchdf()
            total_rows = client.execute(count_query).fetchone()[0]

            print(
                f"Table '{table_name}' retrieved successfully with pagination and KNR filter."
            )
            return df, total_rows


if __name__ == "__main__":
    import asyncio
    import dotenv

    dotenv.load_dotenv()

    df_pivot_d2 = DatalakeService.load_parquet("PIVOT_d2.parquet")
    print("Data loaded from 'PIVOT_d2.parquet':")
    print(df_pivot_d2)

    DatalakeService.create_table(df_pivot_d2, "PIVOT_d2")
    print("Table 'PIVOT_d2' created in the database.")

    tables = DatalakeService.list_tables()
    print("Current tables in the database:")
    print(tables)
