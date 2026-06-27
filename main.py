import string
import secrets

CHARS = string.ascii_letters + string.punctuation + string.digits


def main():
    command_str = input("> ")
    command = command_str.split(" ")
    if command[0].lower() == "exit" or command[0].lower() == "q":
        quit()
    elif command[0].lower() == "gen":
        length = 0
        try:
            length = int(command[1])
        except ValueError:
            print("Please Enter a Valid Password Length")
        if length > 0:
            password = "".join(secrets.choice(CHARS) for _ in range(int(length)))
            print(f"PASSWORD: {password}")
        else:
            print("Password Length Must Be Greater Than 0")
    else:
        print("Unknown Command, Valid Commands Are\n gen [length (int)]\n quit")


while True:
    main()
