from dotenv import load_dotenv
import mysql.connector
import os

load_dotenv()

db = mysql.connector.connect(
  host=os.environ.get("HOST"), 
  password=os.environ.get("PASSWORD"), 
  user=os.environ.get("USER")
)

cursor = db.cursor()