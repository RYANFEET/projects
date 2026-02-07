import random

comchoice = random.randint (1,100)
attempts = 0

def user_guess():
    while True:
        user_number = input('Enter a number 1-100: ')
        
        if not user_number.strip():
            print("You must enter a number.")
            continue
        
        try:
            user_number2 = int(user_number)
            if user_number2 not in range(1, 101):
                print("Your number is not in the range of 1-100.")
            else:
                return user_number2
        except ValueError:
            print("That's not a valid number. Please enter a whole number.")

def main():
    global comchoice, attempts
    num = user_guess()
    if num == comchoice:
        print(f"YOU WIN!!!\nAnd it only took you {attempts + 1} attempts to get it!")
    elif num < comchoice:
        print("Go bigger\n")
        attempts = attempts + 1
        main()
    elif num > comchoice:
        print("Go smaller\n")
        attempts = attempts + 1
        main()
    else:
        print("An error has occured")
    


if __name__ == "__main__":
    main()