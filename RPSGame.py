import random
# Rock beats Scissors, Scissors beats Paper, and Paper beats Rock
# Enter either Rock , Paper , Scissors
# Also its not case sensitive so dw
draws = 0
wins = 0
losses = 0

# this is how the code knows what you chose
def User_Choice():
   options = ["Rock", "Paper", "Scissors"]
   global Your_Choice
   choice = input("Enter your choice (Rock, Paper, or Scissors): ").capitalize()
   if choice not in options:
      print ("Invalid Choice, Please pick again.")
      choice = None
      User_Choice()
   else:
      Your_Choice = choice
      return choice

# tells the code what the pc chose
def fun1():
    # This turns the numbers into words of what the pc chooses
    global pc
    if chosen == 1:
       pc = "Rock"
    elif chosen == 2:
        pc = "Paper"
    else:
       pc = "Scissors"

# decides the outcome
def fun2(): 
    global wins, losses, draws, Your_Choice
    if secret == 67:
       print ("Secret Win (1 in 1k chance)")
       wins = wins + 10000
    # Draws
    if Your_Choice == pc:
        print ("It's a draw")
        draws = draws + 1
    # Wins
    elif Your_Choice == "Paper" and pc == "Rock" or Your_Choice == "Rock" and pc == "Scissors" or Your_Choice == "Scissors" and pc == "Paper":
        print ("You Win")
        wins = wins + 1
    # Losses
    elif Your_Choice == "Paper" and pc == "Scissors" or Your_Choice == "Rock" and pc == "Paper" or Your_Choice == "Scissors" and pc == "Rock":
        print ("You Lose")
        losses = losses + 1

# basically just QOL stuff
def debug():
   # This is just for the player to know what the pc chose (QOL)
   print (f"\nPc chose {pc}")


# this is the main stuff for the program
def main():
   global pc, chosen, answer, secret, Your_Choice

   # this loops for the player to play again if they said yes
   play_again = True
   while play_again:
       chosen = None
       Your_Choice = None
       User_Choice()
       pc = None
       secret = random.randint(1,1000)
       chosen = random.randint(1, 3)
       fun1()
       fun2()
       debug()
      
       # this asks the player if they wanna play again
       print("\nWould you like to play again?")
       answer = input("Yes or No: ").strip().capitalize()
      
       # this ends the loop if the player didnt say yes
       if answer != "Yes":
           play_again = False
           print(f"You had {wins} win(s)\nYou had {losses} loss(es)\nYou had {draws} draw(s)")


# this starts the game
if __name__ == "__main__":
   main()




