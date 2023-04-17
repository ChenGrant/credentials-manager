import db_manager as db

def prompt_authentication():
  username = input("enter username: ")
  password = input("enter password: ")
  return password, username


def has_error_code(response):
  return response.status_code > 400
  
  
def authenticate(f):
  while True:
    auth_method = input("signup or login: ")
    if auth_method == "signup":
      while True:
        username, password = prompt_authentication()
        signup_response = db.signup_user(username, password)
        if (has_error_code(signup_response)):
          # print appropriate message for error
          print("Invalid username/password")
          continue
        f()
        auth_method = None
        break
      continue
    if auth_method == "login":
      while True:
        username, password = prompt_authentication()
        login_status = db.login_user(username, password)
        if (has_error_code(login_status)):
          # print appropriate message for error
          print("Invalid username/password")
          continue
        f()
        auth_method = None
        break
      continue
    print("Invalid input")
  
  
  
  