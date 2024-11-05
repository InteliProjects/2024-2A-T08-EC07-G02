import secrets
import uuid


class Generator:
    @staticmethod
    def generate_api_key():
        return f"presgen-{uuid.uuid4()}"


if __name__ == "__main__":
    print(Generator.generate_api_key())
