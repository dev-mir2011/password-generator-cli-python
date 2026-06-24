import string
import secrets

CHARS = string.ascii_letters + string.punctuation + string.digits

def main():
    command_str = input("> ")
    command = command_str.split(" ")
    if command[0].lower() == "exit" or command[0].lower() == "q":
        quit()
    elif command[0].lower() == "gen":
        length = command[1]
        if length is not None:
            if length != "" or length != " ":
                print("Password Length Must Be Greater Than 0") 
            else:
                if int(length) > 0:
                    password = "".join(secrets.choice(CHARS) for _ in range(int(length)))
                    print(f"PASSWORD: {password}")
                else:
                    print("Password Length Must Be Greater Than 0") 
        else:
            print("Password Length Must Be provided")
        
        
        
        
    
while True:
    main()