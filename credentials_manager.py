import database_manager as db

def main():
  user_id = None
  
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
    print()
    print("------ Commands ------")
    print("[1] - get credentials for an app")
    print("[2] - get all apps connected to an email")
    print("[3] - add app credentials")
    print("[4] - update app credentials")
    print("[5] - delete app credentials")
    print("[6] - get user credentials")
    print("[7] - update user credentials")
    print("[q] - quit")
    
    command = input("Enter a command: ")
    
    if command == "1" :
      continue
    
    if command == "2" :
      continue
    
    if command == "3" :
      continue
    
    if command == "4" :
      continue
    
    if command == "5" :
      continue
    
    if command == "q":
      continue
    
    print("Try Again")
    

if __name__ == "__main__":
  main()