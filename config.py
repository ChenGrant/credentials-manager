from dotenv import load_dotenv
import os

match os.environ.get("ENV"):
  case "dev": load_dotenv(".env.dev")
  case "prod": load_dotenv(".env.prod")