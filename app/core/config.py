from pathlib import Path
from starlette.config import Config

p: Path = Path(__file__).parents[2] / ".env"
config: Config = Config(p if p.exists() else None)

API_V1_STR = "/api/v1"
SECRET_KEY = config("SECRET_KEY", cast=str)
PROJECT_NAME = config("PROJECT_NAME")
MONGODB_URI= config("MONGODB_URI")
SECRET_KEY= config("SECRET_KEY")
PORT= config("PORT")