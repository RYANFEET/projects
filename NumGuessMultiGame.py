import random

comchoice = random.randint (1,100)
attempts1 = 0
attempts2 = 0
winp1 = False
winp2 = False
win = "if you are seeing this it's an error"

# This is for the user input
def user_guess():
    while True:
        user_number = input('Enter a number 1-100: ')
        
        # checks for nothing/whitespace
        if not user_number.strip():
            print("You must enter a number.")
            continue
        
        try:
            # checks for range
            user_number2 = int(user_number)
            if user_number2 not in range(1, 101):
                print("Your number is not in the range of 1-100.")
            else:
                return user_number2
        # if there is an error (like someone puts "Hello" instead of a number) it does this
        except ValueError:
            print("That's not a valid number. Please enter a whole number.")

#These are the main functions for player 1
def main1():
    global comchoice, attempts1
    num = user_guess()

    #just some win logic
    if num == comchoice:
        attempts1 = attempts1 + 1
        print(f"YOU WIN!!!\nAnd it took you only {attempts1} attempts to get it!\n\n\n")
    elif num < comchoice:
        print("Go bigger\n")
        attempts1 = attempts1 + 1
        main1()
    elif num > comchoice:
        print("Go smaller\n")
        attempts1 = attempts1 + 1
        main1()
    else:
        print("An error has occured")

#These are the main functions for player 2
def main2():
    global comchoice, attempts2
    num = user_guess()

    #some more win logic
    if num == comchoice:
        attempts2 = attempts2 + 1
        print(f"YOU WIN!!!\nAnd it took you only {attempts2} attempts to get it!\n\n\n")
    elif num < comchoice:
        print("Go bigger\n")
        attempts2 = attempts2 + 1
        main2()
    elif num > comchoice:
        print("Go smaller\n")
        attempts2 = attempts2 + 1
        main2()
    else:
        print("An error has occured")
    

if __name__ == "__main__":
    p1name = input("Player 1, Please enter your name: ")
    main1()
    comchoice = random.randint (1,100)
    p2name = input("Player 2, Please enter your name: ")
    main2()
    if attempts1 < attempts2:
        winp1 = True
    elif attempts2 < attempts1:
        winp2 = True
    
    if winp1 == False and winp2 == False:
        win = f"It's A Draw"
    elif winp1 == True:
        win = f"{p1name} Wins!"
    elif winp2 == True:
        win = f"{p2name} Wins!"

    print(f"{p1name} had {attempts1} attempts\n{p2name} had {attempts2} attempts\n\n This means that {win}")