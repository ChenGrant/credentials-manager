import database_manager as db


def main():
  def render_commands(commands):
    print()
    print("------ Commands ------")
    for index, command in enumerate(commands):
      print(f"[{index}] - {command}")
      
  # https://stackoverflow.com/questions/10865483/print-results-in-mysql-format-with-python
  def render_credentials(credentials):
    if credentials == []:
      print("No credentials")
      return
      
    column_widths = {key: len(key) for key in credentials[0].keys()}
    for entry in credentials:
      for key, val in entry.items():
        column_widths[key] = max(len(val), column_widths[key])
    table_width = sum(map(lambda x : x + 1, column_widths.values())) + 1
    print("-" * table_width)
    for column_name, column_length in column_widths.items():
      print(f"|{column_name}{(column_length - len(column_name))*' '}", end="")
    print("|")
    print("-" * table_width)
    for entry in credentials:
      for key, val in entry.items():
        print(f"|{val}{(column_widths[key] - len(val))*' '}", end="")
      print("|")
    print("-" * table_width)
    
    
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
  
  # make adding command easier, map command name to number 
  COMMANDS = [
    "get all credentials",
    "get credentials connected to an app",
    "get credentials connected to an email",
    "add app credentials",
    "update app credentials",
    "delete app credentials",
    "get user credentials",
    "update user credentials",
    "quit"
  ]
  
  while True:
    render_commands(COMMANDS)
    command_index = input("Enter a command: ")
    
    try:
      command = COMMANDS[int(command_index)]
    except:
      command = None
    
    if command == "get all credentials" :
      credentials = db.get_all_credentials(user_id)
      if credentials is not None: 
        render_credentials(credentials)
      continue
    
    if command == "get credentials connected to an app" :
      app = input("Enter an app: ")
      credentials = db.get_credentials_from_app(user_id, app)
      if credentials is not None: 
        render_credentials(credentials)
      continue
    
    if command == "get credentials connected to an email" :
      email = input("Enter an email: ")
      credentials = db.get_credentials_from_email(user_id, email)
      if credentials is not None: 
        render_credentials(credentials)
      continue
    
    if command == "add app credentials" :
      continue
    
    if command == "update app credentials" :
      continue
    
    if command == "delete app credentials":
      continue
    
    if command == "get user credentials":
      continue
    
    if command == "update user credentials":
      continue
    
    if command == "quit":
      continue
    
    print("Try Again")
    

if __name__ == "__main__":
  main()