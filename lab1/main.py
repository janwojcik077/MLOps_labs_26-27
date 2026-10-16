import os
import argparse
import yaml
from dotenv import load_dotenv
from settings import Settings


def export_envs(environment: str = "dev") -> None:
    # ścieżka do odpowiedniego pliku .env w folderze config
    env_path = os.path.join("config", f".env.{environment}")

    # ładujemy zmienne do środowiska procesowego
    load_dotenv(dotenv_path=env_path, override=True)


def load_secrets(secrets_path: str = "secrets.yaml") -> None:
    if os.path.exists(secrets_path):
        with open(secrets_path, "r") as f:
            secrets = yaml.safe_load(f)
            if secrets:
                for key, value in secrets.items():
                    # sops dodaje własne metadane zaczynające się od 'sops', trzeba je zignorowac
                    if not key.startswith("sops"):
                        os.environ[key] = str(value)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)
    load_secrets()

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("API_KEY: ", settings.API_KEY)
