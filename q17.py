while True:
    user_input=(input("enter a number (or type ,quit to exit)"))
    if user_input=="quit":
        print("programm sttoped")
        break

    number=float(user_input)
    if number > 0:
        print("positive number")
    else:
        number <0
        print("negative number")
