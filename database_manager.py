from codec import encrypt, decrypt
import config
import mysql.connector
import os

def signup_user(username, password):
  cursor.execute(
    f"INSERT INTO users (username, password)\n"
    f"VALUES ('{username}', '{encrypt(password)}')"
  )
  connection.commit()
  cursor.execute(
    f"SELECT id FROM users\n"
    f"WHERE username = '{username}'"
    f"LIMIT 1"
  )
  return next(cursor)[0]
  
  
def login_user(username, password):
  cursor.execute(
    f"SELECT id, password FROM users\n"
    f"WHERE username = '{username}'"
    f"LIMIT 1"
  )
  user = next(cursor)
  return user[0] if decrypt(user[1]) == password else None


def get_apps(user_id, email):
  pass


def get_credentials(user_id, app):
  pass


def add_credential(user_id, app, email, username, password):
  pass


def update_credential(user_id, app, email, username, password):
  pass

connection = mysql.connector.connect(
  host=os.environ.get("HOST"), 
  password=os.environ.get("PASSWORD"), 
  user=os.environ.get("USER"),
  database=os.environ.get("DATABASE"))

cursor = connection.cursor()