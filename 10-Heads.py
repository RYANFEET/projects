import time, random
headrow = 0
heads = 0
tails = 0
money = 0
headchance = 20
fliptime = 2
coinvalue = 0.01
multiplier = 1
c1 = 0.01
c2 = 0.01
c3 = 0.01
c4 = 0.01
p1 = 0.25
p2 = 1
p3 = 6.25
p4 = 25
p5 = 100
bought = 0
valid = 0
print("Welcome to 10 Heads!")
time.sleep(0.5)
print("Here is how it works\n You flip a coin and if you get heads 10 times in a row you win\n Everytime you land on heads you get 0.01 dollars\n Upgrade stuff like the chance of heads or how much money you get")
def main():
    global money, headrow, heads, tails, headchance, fliptime, coinvalue, multiplier, c1, c2, c3, c4, p1, p2, p3, p4, p5, bought, valid
    while True:
        if headrow == 9:
            if not final_flip():
                break
        option = input("What would you like to do?\n[1] Flip the coin.\n[2] Open the shop.\n[3] Check your stats.\n ")
        try:
            option = int(option)
            if option not in range(1,4):
                print("That is not a valid option please select a valid option.")
            elif option == 1:
                print("Flipping")
                time.sleep(fliptime)
                if random.randint(1,100) <= headchance:
                    headrow += 1

                    # stacking formula
                    stacked_pay = coinvalue * (multiplier * headrow)
                    if headrow == 1:
                        stacked_pay = coinvalue
                    stacked_pay = round(stacked_pay, 4)

                    money += stacked_pay
                    money = round(money, 2)

                    print(f"\nHeads (streak {headrow}) +${stacked_pay}\n")
                    heads += 1
                else:
                    print("\nTails\n")
                    headrow = 0
                    tails = tails + 1
            elif option == 2:
                print(f"\nWelcome to the shop. You have ${money}\n What would you like to upgrade?")
                buy = input(f" [1] Upgrade heads chance +5%(Price = {c1})\n [2] Upgrade flip speed -0.2(Price = {c2})\n [3] Upgrade consecutive multiplier +0.4(Price = {c3})\n [4] Upgrade coin value(Price = {c4})\n [anything else] Go back without upgrading\n ")
                buy = int(buy)

                if buy == 1 and money >= c1:
                    headchance = headchance + 5
                    money = money - c1
                    money = round(money, 2)
                    print(f"Bought you now have a {headchance}% chance of getting heads.")
                    c1 = c1 * 10
                    #I know evil
                    if headchance >= 60:
                        headchance = 60
                        # if c1 gets checked against money it raises a value error therefore restarting the loop
                        c1 = "Maxed" 
                elif buy not in range(1,5):
                    print("That is not a valid shop item.")
                    continue

                elif buy == 2 and money >= c2:
                    fliptime = fliptime - 0.2
                    money = money - c2
                    money = round(money, 2)
                    fliptime = round(fliptime, 2)
                    print(f"Bought the coin now flips in {fliptime} second(s)")
                    c2 = c2 * 10
                    #I know evil
                    if fliptime <= 1:
                        fliptime = 1
                        # if c2 gets checked against money it raises a value error therefore restarting the loop
                        c2 = "Maxed"

                elif buy == 3 and money >= c3:
                    multiplier = multiplier + 0.4
                    multiplier = round(multiplier, 2)
                    money = money - c3
                    money = round(money, 2)
                    print(f"You now have a multiplier of {multiplier} for each consecutive flip (stacks)")
                    # I will add the stacking to flip later
                    c3 = c3 * 10
                    #I know evil
                    if multiplier >= 3:
                        multiplier = 3
                        # if c3 gets checked against money it raises a value error therefore restarting the loop
                        c3 = "Maxed"

                elif buy == 4 and money >= c4:
                    bought = bought + 1
                    money = money - c4
                    money = round(money, 2)
                    if bought == 1:
                        coinvalue = p1
                    elif bought == 2:
                        coinvalue = p2
                    elif bought == 3:
                        coinvalue = p3
                    elif bought == 4:
                        coinvalue = p4
                    elif bought == 5:
                        coinvalue = p5                        
                    print(f"Bought the coin is now worth ${coinvalue}")
                    c4 = c4 * 10
                    #I know evil
                    if coinvalue >= 100:
                        coinvalue = 100
                        # if c4 gets checked against money it raises a value error therefore restarting the loop
                        c4 = "Maxed"
                else:
                    print("You can't afford this.")
                continue  
            elif option == 3:
                print(f"You have landed on heads {heads} time(s)\nTails {tails} time(s)\nYou have ${money}")

        except ValueError:
            print("That is not a valid option please select a valid option.")
        except TypeError:
            print("That upgrade is maxed please select a different one.")
def final_flip():
    global money, headrow, heads, tails, headchance, fliptime, coinvalue, multiplier, valid
    headchance2 = 10

    print("This could be the last flip")
    time.sleep(1)
    print("There is a 10% chance you get this")
    time.sleep(1)
    print("Good Luck, You'll need it.")
    time.sleep(1)

    while True:
        try:
            final = input("[1] Initiate the FINAL FLIP (assuming you get heads)\n")
            final = int(final)

            if final == 1:
                print("Flipping")
                time.sleep(fliptime)

                if random.randint(1,100) <= headchance2:
                    headrow += 1

                break  # <-- EXIT final_flip loop because they actually flipped

            else:
                print("Don't be scared just do it.")
                valid = 1
                # raise an error on purpose to repeat the prompt
                raise ValueError

        except ValueError:
            if valid == 1:
                valid = 0
                pass
            else:
                print("Don't be scared just do it.")
                valid = 0

    # AFTER the flip actually happened, now check win/lose
    if headrow == 10:
        print("YOU WIN!!!")
        return False  # return False to end main loop

    else:
        print("Dang try again when you get back here I guess")
        headrow = 0
        return True   # return True to continue game
if __name__ == "__main__":  
    main()
