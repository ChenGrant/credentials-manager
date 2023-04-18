from codec import encrypt, decrypt
import config
import mysql.connector
import os

# establish mysql connection
db = mysql.connector.connect(
  host=os.environ.get("HOST"), 
  password=os.environ.get("PASSWORD"), 
  user=os.environ.get("USER"),
  database=os.environ.get("DATABASE"))

cursor = db.cursor()


def try_catch(func):
  def wrapper(*args, **kwargs):
    try: 
      return func(*args, **kwargs)
    except Exception as e: 
      print("Error: ", e)

  return wrapper
      
      
@try_catch
def signup_user(username, password):
  cursor.execute(
    f"INSERT INTO users (username, password)\n"
    f"VALUES ('{username}', '{encrypt(password)}')"
  )
  db.commit()
  cursor.execute(
    f"SELECT id FROM users\n"
    f"WHERE username = '{username}'\n"
    f"LIMIT 1"
  )
  return next(cursor)[0]
    

@try_catch
def login_user(username, password):
  cursor.execute(
    f"SELECT id FROM users\n"
    f"WHERE username = '{username}'\n"
    f"AND password = '{decrypt(password)}'\n"
    f"LIMIT 1"
  )
  return next(cursor)[0]


@try_catch
def get_all_credentials(user_id):
  cursor.execute(
    f"SELECT app, email, username, password FROM credentials\n"
    f"WHERE user_id = '{user_id}'\n"
  )
  credentials = []
  for record in cursor:
    app, email, username, password = record
    credentials.append({
      'app' : app,
      'email': email,
      'username': username,
      'password': password
    })
  return credentials
  
  
@try_catch
def get_credentials_from_app(user_id, app):
  cursor.execute(
    f"SELECT email, username, password FROM credentials\n"
    f"WHERE user_id = '{user_id}'\n"
    f"AND app = '{app}'\n"
  )
  credentials = []
  for record in cursor:
    email, username, password = record
    credentials.append({
      'app': app,
      'email': email,
      'username': username,
      'password': password
    })
  return credentials


@try_catch
def get_credentials_from_email(user_id, email):
  cursor.execute(
    f"SELECT app, email, username, password FROM credentials\n"
    f"WHERE user_id = '{user_id}'\n"
    f"AND email = '{email}'\n"
  )
  credentials = []
  for record in cursor:
    app, email, username, password = record
    credentials.append({
      'app': app,
      'email': email,
      'username': username,
      'password': password
    })
  return credentials
  

@try_catch
def add_credentials(user_id, app, email, username, password):
  cursor.execute(
    f"INSERT INTO credentials (user_id, app, email, username, password)\n"
    f"VALUES ('{user_id}', '{app}', '{email}', '{username}', '{encrypt(password)}')"
  )
  db.commit()
  return (user_id, app, email, username, password)


@try_catch
def update_credentials(user_id, app, email, username, password):
  cursor.execute(
    f"UPDATE credentials\n"
    f"SET username = '{username}', password = '{encrypt(password)}'\n"
    f"WHERE user_id = '{user_id}'\n"
    f"AND app = '{app}'\n"
    f"AND email = '{email}'\n"
  )
  db.commit()
  return (user_id, app, email, username, password)


@try_catch
def delete_credentials(user_id, app, email):
  cursor.execute(
    f"DELETE FROM credentials\n"
    f"WHERE user_id = '{user_id}'\n"
    f"AND app = '{app}'\n"
    f"AND email = '{email}'\n"
  )
  db.commit()
  return (user_id, app, email)
