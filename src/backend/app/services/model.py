import os
import numpy as np
import pandas as pd
import joblib
import boto3
from io import BytesIO
from typing import List


class ModelService:
    __model = None
    __current_model: str = None
    __s3_client = None
    __bucket_name = "vwmodels"

    @staticmethod
    def _initialize_s3_client():
        if ModelService.__s3_client is None:
            ModelService.__s3_client = boto3.client("s3")

    @staticmethod
    def _initialize_model():
        ModelService._initialize_s3_client()

        if ModelService.__model is None:
            if ModelService.__current_model is None:
                model_env_path = os.getenv("MODEL_PATH")
                if model_env_path is None:
                    raise FileNotFoundError(
                        "MODEL_PATH environment variable not set. Please set it or use update_model_path(new_model_path)."
                    )
                ModelService.__current_model = model_env_path

            try:
                s3_object = ModelService.__s3_client.get_object(
                    Bucket=ModelService.__bucket_name, Key=ModelService.__current_model
                )
                model_data = s3_object["Body"].read()
                ModelService.__model = joblib.load(BytesIO(model_data))
                print(f"Loaded Joblib model from S3: '{ModelService.__current_model}'.")

            except Exception as e:
                raise FileNotFoundError(
                    f"Model file '{ModelService.__current_model}' not found in S3."
                ) from e

    @staticmethod
    def reload_model():
        ModelService.__model = None
        ModelService._initialize_model()

    @staticmethod
    def get_model_path() -> str:
        return ModelService.__current_model

    @staticmethod
    def upload_model(model_local_path: str, tags: List[str] = []):
        ModelService._initialize_s3_client()
        try:
            model_filename = os.path.basename(model_local_path)
            s3_model_path = f"models/{model_filename}"

            with open(model_local_path, "rb") as f:
                ModelService.__s3_client.upload_fileobj(
                    f,
                    ModelService.__bucket_name,
                    s3_model_path,
                    ExtraArgs={"Tagging": "&".join(tags)},
                )

            ModelService.__current_model = s3_model_path
            ModelService.reload_model()

        except Exception as e:
            raise FileNotFoundError(f"Model file '{model_path}' not found in S3.")

    @staticmethod
    def update_model_path(new_model_path: str):
        ModelService._initialize_s3_client()

        try:
            ModelService.__s3_client.head_object(
                Bucket=ModelService.__bucket_name, Key=f"models/{new_model_path}"
            )
            ModelService.__current_model = new_model_path
            ModelService.reload_model()
        except Exception as e:
            raise FileNotFoundError(f"Model file '{new_model_path}' not found in S3.")

    @staticmethod
    def get_models() -> list:
        ModelService._initialize_s3_client()
        models_with_tags = []
        try:
            response = ModelService.__s3_client.list_objects_v2(
                Bucket=ModelService.__bucket_name, Prefix="models/"
            )

            if "Contents" in response:
                for obj in response["Contents"]:
                    if obj["Key"].endswith(".joblib"):
                        model_name = obj["Key"].replace("models/", "")

                        try:
                            tags_response = ModelService.__s3_client.get_object_tagging(
                                Bucket=ModelService.__bucket_name, Key=obj["Key"]
                            )
                            tags = [tag["Key"] for tag in tags_response["TagSet"]]
                        except Exception as e:
                            tags = []
                        models_with_tags.append(
                            {"model_name": model_name, "tags": tags}
                        )
        except Exception as e:
            print(f"Error listing models from S3: {str(e)}")

        return models_with_tags

    @staticmethod
    def get_model(model_id: str) -> str:
        model_path = f"models/{model_id}"
        ModelService._initialize_s3_client()

        try:
            ModelService.__s3_client.head_object(
                Bucket=ModelService.__bucket_name, Key=model_path
            )
            url = f"https://{ModelService.__bucket_name}.s3.amazonaws.com/{model_path}"
            return url
        except Exception as e:
            raise FileNotFoundError(f"Model file '{model_path}' not found in S3.")

    @staticmethod
    def delete_model(model_id: str):
        model_path = f"models/{model_id}"
        ModelService._initialize_s3_client()

        try:
            ModelService.__s3_client.delete_object(
                Bucket=ModelService.__bucket_name, Key=model_path
            )
        except Exception as e:
            raise FileNotFoundError(f"Model file '{model_path}' not found in S3.")

    @staticmethod
    def predict(knr: pd.DataFrame | dict) -> float:
        if ModelService.__model is None:
            ModelService._initialize_model()

        if isinstance(knr, dict):
            knr = pd.DataFrame([knr])

        excluded_columns = ["KNR", "HAS_FAILURE"]
        knr = knr.drop(
            columns=[col for col in excluded_columns if col in knr.columns],
            errors="ignore",
        )

        input_data = knr.to_numpy().astype(np.float32)

        result = ModelService.__model.predict(input_data)

        if result.shape[1] == 1:
            predicted_class = (result > 0.5).astype(int)
            return predicted_class[0][0]
        else:
            predicted_class = np.argmax(result, axis=1)
            return predicted_class[0]

    @staticmethod
    def get_base_path() -> str:
        return ModelService.__bucket_name


if __name__ == "__main__":
    import dotenv

    dotenv.load_dotenv()

    knr = pd.read_parquet("PIVOT_d2.parquet").sample(1)

    print(
        f"Testing KNR '{knr['KNR'].values[0]}' expecting predict {knr['HAS_FAILURE'].values[0]}"
    )
    prediction = ModelService.predict(knr)
    print(f"Predicted: {prediction}")
