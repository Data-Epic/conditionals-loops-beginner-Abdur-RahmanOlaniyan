password = 'python123'

while True:
    user_input = input("Enter password: ")
    if user_input == password:
        print("Password accepted!")
        break
    else:
        print("Wrong password, try again")