import database_manager as db


def main():
  def render_credentials(credentials):
    if not credentials:
      print("No credentials")
      return

    col_widths = {key: max(max([len(entry[key]) for entry in credentials]), len(key)) 
                  for key in credentials[0].keys()}
    print("|".join([name + (width - len(name)) * ' ' for name, width in col_widths.items()]))
    print("-"* (sum(map(lambda x : x + 1, col_widths.values())) - 1))
    for entry in credentials:
      print("|".join([val + (col_widths[key] - len(val)) * ' ' for key, val in entry.items()]))
    
    
  user_id = 1 #None
  
  while not user_id:
    print()
    print("------ Commands ------")
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
      "gc": "get all credentials",
      "gca": "get credentials connected to an app",
      "gce": "get credentials connected to an email",
      "aac": "add app credentials",
      "uac": "update app credentials",
      "dac": "delete app credentials",
      "guc": "get user credentials",
      "uuc": "update user credentials",
      "q": "quit"
    }.items():
      print(f"[{command}] - {name}")
      
    command = input("Enter a command: ")
    
    if command == "gc" :
      credentials = db.get_all_credentials(user_id)
      if credentials is not None: 
        render_credentials(credentials)
      continue
    
    if command == "gca" :
      app = input("Enter an app: ")
      credentials = db.get_credentials_from_app(user_id, app)
      if credentials is not None: 
        render_credentials(credentials)
      continue
    
    if command == "gce" :
      email = input("Enter an email: ")
      credentials = db.get_credentials_from_email(user_id, email)
      if credentials is not None: 
        render_credentials(credentials)
      continue
    
    if command == "aac" :
      continue
    
    if command == "uac" :
      continue
    
    if command == "dac":
      continue
    
    if command == "guc":
      continue
    
    if command == "uuc":
      continue
    
    if command == "q":
      continue
    
    print("Try Again")
    

if __name__ == "__main__":
  main()