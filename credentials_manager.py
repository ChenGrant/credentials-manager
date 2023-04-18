import database_manager as db

def main():
  user_id = None
  
  while True:
    user_command = input("signup [s] or login [l]: ")
    
    if user_command == "s":
      username = input("enter username: ")
      password = input("enter password: ")
      user_id = db.signup_user(username, password)
    
    if user_command == "l":
      username = input("enter username: ")
      password = input("enter password: ")
      user_id = db.login_user(username, password)
    
    if (user_id): break
    
    print("Try Again.")
  
  print(f"user authenticated. user_id: {user_id}")

if __name__ == "__main__":
  main()