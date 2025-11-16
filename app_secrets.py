from dotenv import load_dotenv
import os


load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise EnvironmentError("Missing SECRET_KEY. Please add it to .env file")

FLASK_ENV = os.getenv("FLASK_ENV")
if FLASK_ENV not in ("production", "development", "testing"):
    raise EnvironmentError("Wrong FLASK_ENV type.")