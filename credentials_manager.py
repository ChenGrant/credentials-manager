import database_manager as db


def render_credentials(credentials):
    if not credentials: return print("No credentials")

    col_widths = {key: max(max([len(entry[key]) for entry in credentials]), len(key)) 
                  for key in credentials[0].keys()}
    print("|".join([name + (width - len(name)) * ' ' for name, width in col_widths.items()]))
    print("-"* (sum(map(lambda x : x + 1, col_widths.values())) - 1))
    for entry in credentials:
      print("|".join([val + (col_widths[key] - len(val)) * ' ' for key, val in entry.items()]))


def main():
  user_id = None
  
  while not user_id:
    print("\n------ Commands ------")
    print("[s] - signup")
    print("[l] - login")
    
    command = input("Enter a command: ")
    
    if command == "s" :
      username = input("Enter username: ")
      password = input("Enter password: ")
      user_id = db.signup_user(username, password)
      
    if command == "l":
      username = input("Enter username: ")
      password = input("Enter password: ")
      user_id = db.login_user(username, password)
      
    if not user_id:
      print("Try Again")

  
  while True:
    print("\n------ Commands ------")
    for command, name in {
      "g": "get all app credentials",
      "ga": "get app credentials from app",
      "ge": "get app credentials from email",
      "a": "add app credentials",
      "u": "update app credentials",
      "d": "delete app credentials",
      "q": "quit"
    }.items(): print(f"[{command}] - {name}")
      
    command = input("Enter a command: ")
    
    if command == "g" :
      credentials = db.get_all_credentials(user_id)
      if credentials is not None: 
        render_credentials(credentials)
    
    elif command == "ga" :
      app = input("Enter an app: ")
      credentials = db.get_credentials_from_app(user_id, app)
      if credentials is not None: 
        render_credentials(credentials)
    
    elif command == "ge" :
      email = input("Enter an email: ")
      credentials = db.get_credentials_from_email(user_id, email)
      if credentials is not None: 
        render_credentials(credentials)
    
    elif command == "a" :
      app = input("Enter an app: ")
      email = input("Enter a email: ")
      username = input("Enter a username: ")
      password = input("Enter a password: ")
      if db.add_credentials(user_id, app, email, username, password): 
        print("Credentials added")
      
    elif command == "u" :
      app = input("Enter an app: ")
      email = input("Enter a email: ")
      username = input("Enter new username: ")
      password = input("Enter new password: ")
      if db.update_credentials(user_id, app, email, username, password): 
        print("Credentials updated")
    
    elif command == "d":
      app = input("Enter an app: ")
      email = input("Enter a email: ")
      if db.delete_credentials(user_id, app, email):  
        print("Credentials deleted")
    
    elif command == "q": break
    
    else: print("Try Again")
    

if __name__ == "__main__":
  main()