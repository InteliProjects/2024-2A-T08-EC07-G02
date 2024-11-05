import os
import logging
import pandas as pd
import numpy as np
from pycaret.classification import *
from sklearn.model_selection import train_test_split
from sklearn.metrics import recall_score, f1_score
import joblib

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"


class ModelPipeline:
    def __init__(
        self, failures: pd.DataFrame, results: pd.DataFrame, status: pd.DataFrame
    ):
        self.failures = failures
        self.results = results
        self.status = status
        self.final_df = None

    def run(self, output_path: str = None):
        try:
            Transform(self).run()
            if output_path:
                Load(self, output_path).run()
            else:
                Predict(self).run()
        except Exception as e:
            logging.error(f"An error occurred during the pipeline execution: {str(e)}")
            return {"status": "error", "message": str(e)}
        else:
            logging.info("Model pipeline completed successfully.")
            return {"status": "success", "message": "Model pipeline completed."}


class Transform:
    def __init__(self, model_pipeline: ModelPipeline):
        self.model_pipeline = model_pipeline

    def __process_failures(self):
        if self.model_pipeline.failures is not None:
            logging.info("Processing failures...")
            self.model_pipeline.failures["KNR"] = self.model_pipeline.failures[
                "KNR"
            ].astype(str)
        else:
            logging.info("No failures data provided. Skipping failures processing.")

    def __process_results(self):
        logging.info("Processing results...")
        df_re = self.model_pipeline.results

        df_re["KNR"] = df_re["KNR"].astype(str)

        ser = self.model_pipeline.status["KNR"].unique()
        initial_count = df_re.shape[0]
        df_re = df_re[df_re["KNR"].isin(ser) & df_re["UNIT"].notnull()].reset_index(
            drop=True
        )
        filtered_count = df_re.shape[0]
        logging.info(f"Filtered results from {initial_count} to {filtered_count} rows.")

        logging.info("Pivoting 'NAME' to columns...")
        df_re_pivot = df_re.pivot_table(
            index="KNR",
            columns="NAME",
            values="VALUE_ID",
            aggfunc="count",
            fill_value=0,
        ).reset_index()
        logging.info(
            f"Pivoted results DataFrame has {df_re_pivot.shape[0]} rows and {df_re_pivot.shape[1]} columns."
        )

        self.model_pipeline.results = df_re_pivot

    def __process_status(self):
        logging.info("Processing status...")
        df_st = self.model_pipeline.status.copy()

        df_st["KNR"] = df_st["KNR"].astype(str)

        zp_categories = {
            "ZP5": [
                "R640",
                "R650",
                "R700",
                "R754",
                "R755",
                "R500",
                "R645",
                "R655",
                "R701",
                "R750",
            ],
            "ZP5A": [
                "L534",
                "L535",
                "L536",
                "L537",
                "L538",
                "L539",
                "L541",
                "L542",
                "L543",
                "L544",
                "L545",
                "L546",
                "L547",
                "L548",
                "L540",
            ],
            "ZP6": [
                "G700",
                "M600",
                "M599",
                "M591",
                "M592",
                "M593",
                "M594",
                "M595",
                "M596",
                "M643",
                "M644",
                "M647",
                "M648",
                "M651",
                "M652",
                "M655",
                "M656",
                "M673",
                "M674",
                "M677",
                "M678",
                "M681",
                "M682",
            ],
            "CABINES": ["M619", "M643", "M644", "M655", "M656", "M673", "M674", "M620"],
            "ZP7": [
                "M700",
                "M695",
                "M698",
                "M701",
                "M702",
                "M704",
                "M711",
                "M712",
                "M721",
                "M722",
                "M699",
            ],
        }
        status_to_zp = {
            status: zp for zp, statuses in zp_categories.items() for status in statuses
        }

        df_st["ZP"] = df_st["STATUS"].map(status_to_zp).fillna("-")
        logging.info("Mapped 'STATUS' to 'ZP' categories.")

        initial_count = df_st.shape[0]
        df_st = df_st[df_st["ZP"] != "-"].reset_index(drop=True)
        filtered_count = df_st.shape[0]
        logging.info(
            f"Filtered status from {initial_count} to {filtered_count} rows where 'ZP' is not '-'."
        )

        df_st["DATA"] = df_st["DATA"].astype(str)

        df_st["ZP"] = df_st.groupby("KNR")["ZP"].transform(lambda x: "; ".join(x))
        df_st["DATA"] = df_st.groupby("KNR")["DATA"].transform(lambda x: "; ".join(x))
        df_st = df_st.drop_duplicates(subset=["KNR", "ZP"])
        logging.info("Grouped 'ZP' and 'DATA' by 'KNR' and concatenated values.")

        expected_zps = set(zp_categories.keys())

        df_st["ZP_set"] = df_st["ZP"].apply(lambda x: set(x.split("; ")))
        df_st = df_st[df_st["ZP_set"].apply(lambda x: x == expected_zps)].reset_index(
            drop=True
        )
        logging.info(
            f"Filtered status to {df_st.shape[0]} rows where 'ZP' set matches expected categories."
        )

        logging.info("Assigning times to ZP time columns...")
        zp_times = ["ZP5_t", "ZP5A_t", "ZP6_t", "CABINES_t", "ZP7_t"]
        for col in zp_times:
            df_st[col] = ""

        for idx, row in df_st.iterrows():
            arr_t = row["DATA"].split("; ")
            arr_z = row["ZP"].split("; ")
            time_dict = {}
            for z, t in zip(arr_z, arr_t):
                if z not in time_dict:
                    time_dict[z + "_t"] = t
            for col in zp_times:
                df_st.at[idx, col] = time_dict.get(col, "")

        df_st = df_st.drop(columns=["DATA", "ZP", "STATUS", "ZP_set"], errors="ignore")

        logging.info("Computing time deltas between ZP stages...")
        for col in zp_times:
            df_st[col] = pd.to_datetime(
                df_st[col], format="%Y-%m-%d %H:%M:%S", errors="coerce"
            )

        df_st["delta_ZP5"] = (df_st["ZP5A_t"] - df_st["ZP5_t"]).dt.total_seconds() / 60
        df_st["delta_ZP5A"] = (df_st["ZP6_t"] - df_st["ZP5A_t"]).dt.total_seconds() / 60
        df_st["delta_ZP6"] = (
            df_st["CABINES_t"] - df_st["ZP6_t"]
        ).dt.total_seconds() / 60
        df_st["delta_CABINES"] = (
            df_st["ZP7_t"] - df_st["CABINES_t"]
        ).dt.total_seconds() / 60

        df_st = df_st.drop(columns=zp_times, errors="ignore")

        delta_cols = ["delta_ZP5", "delta_ZP5A", "delta_ZP6", "delta_CABINES"]
        df_st[delta_cols] = (df_st[delta_cols] - df_st[delta_cols].mean()) / df_st[
            delta_cols
        ].std()
        logging.info("Standardized delta columns.")

        self.model_pipeline.status = df_st
        logging.info(
            f"Processed status dataframe has {df_st.shape[0]} rows and {df_st.shape[1]} columns."
        )

    def run(self):
        logging.info("Running transformation pipeline...")
        df_st = self.model_pipeline.status.copy()
        if df_st.columns[0] != "KNR":
            df_st.columns = df_st.iloc[0]
            df_st = df_st.drop(index=0).reset_index(drop=True)
            df_st = df_st.drop(columns=df_st.columns[0], errors="ignore")
            logging.info(
                "Adjusted dataframe columns and rows based on header in first row."
            )
        self.model_pipeline.status = df_st

        self.__process_failures()
        self.__process_results()
        self.__process_status()

        df = self.model_pipeline.results.merge(self.model_pipeline.status, on="KNR")
        logging.info(
            f"Merged results and status dataframes, resulting in {df.shape[0]} rows."
        )

        if self.model_pipeline.failures is not None:
            df["HAS_FALHA"] = (
                df["KNR"].isin(self.model_pipeline.failures["KNR"]).astype(int)
            )
            logging.info("Added 'HAS_FALHA' column based on failures.")

            nunique = df.nunique()
            to_drop = nunique[nunique == 1].index.tolist()
            df.drop(columns=to_drop, inplace=True)
            logging.info(f"Dropped {len(to_drop)} columns with only one unique value.")

            counts = df["HAS_FALHA"].value_counts()
            min_count = counts.min()
            df_balanced = (
                df.groupby("HAS_FALHA")
                .apply(lambda x: x.sample(n=min_count, random_state=42))
                .reset_index(drop=True)
            )
            logging.info(f"Balanced the dataset to {min_count} samples per class.")

            self.model_pipeline.final_df = df_balanced
        else:
            logging.info(
                "No failures data provided. Skipping 'HAS_FALHA' and balancing."
            )
            nunique = df.nunique()
            to_drop = nunique[nunique == 1].index.tolist()
            df.drop(columns=to_drop, inplace=True)
            logging.info(f"Dropped {len(to_drop)} columns with only one unique value.")
            self.model_pipeline.final_df = df


class Load:
    def __init__(self, model_pipeline: ModelPipeline, output_path: str):
        self.model_pipeline = model_pipeline
        self.output_path = output_path

    def __train_model(self):
        logging.info("Training model...")
        df = self.model_pipeline.final_df.copy()
        df = df.drop(columns=["KNR"])
        y = df["HAS_FALHA"]
        X = df.drop(columns=["HAS_FALHA"])

        X = X.astype(np.float32)
        y = y.astype(np.int32)

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.33, random_state=1234
        )
        logging.info("Split data into training and testing sets.")

        df_train = X_train.copy()
        df_train["HAS_FALHA"] = y_train

        s = setup(df_train, target="HAS_FALHA", session_id=123, use_gpu=True)
        best = compare_models(errors="raise")

        eva = best.predict(X_test)
        eva_labels = eva
        y_test_labels = y_test

        recall = recall_score(y_test_labels, eva_labels, average="binary")
        f1 = f1_score(y_test_labels, eva_labels, average="binary")
        logging.info(f"Model evaluation completed. Recall: {recall}, F1-score: {f1}")

        joblib.dump(best, self.output_path)
        logging.info(f"Model saved to {self.output_path}")

    def run(self):
        self.__train_model()


class Predict:
    def __init__(self, model_pipeline: ModelPipeline):
        self.model_pipeline = model_pipeline

    def __load_model(self):
        model_path = os.getenv("MODEL_PATH")
        if not model_path:
            raise ValueError("MODEL_PATH environment variable not set.")
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file '{model_path}' not found.")
        self.model = joblib.load(model_path)
        logging.info(f"Loaded model from '{model_path}'.")

    def __predict(self):
        logging.info("Running predictions...")
        df = self.model_pipeline.final_df.copy()
        knr_list = df["KNR"].values
        df = df.drop(columns=["KNR"], errors="ignore")

        df = df.drop(columns=["HAS_FALHA"], errors="ignore")
        X = df.astype(np.float32)

        predictions = self.model.predict(X)

        predicted_classes = np.argmax(predictions, axis=1)
        results_df = pd.DataFrame({"KNR": knr_list, "Prediction": predicted_classes})
        logging.info("Predictions completed.")
        print(results_df)

    def run(self):
        self.__load_model()
        self.__predict()


if __name__ == "__main__":
    logging.info("Reading input data...")

    failures = pd.read_parquet("temp/FAILURES.parquet")
    results = pd.read_parquet("temp/RESULTS.parquet")
    status = pd.read_excel("temp/STATUS_PREDICTOR_ANO.xlsx")

    model_pipeline = ModelPipeline(failures, results, status)
    model_pipeline.run("temp/model.joblib")
