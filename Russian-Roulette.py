import random
chamber = random.randint(1,6)
turn = 1
win = 0
p1 = input("Player 1 what is your name?\n ")
p2 = input("Player 2 what is your name?\n ")
def p1_turn():
    global p1, p2, turn, chamber, win
    input(f'Fire the "Pew Pew" {p1}')
    if turn == chamber:
        win = 1
    else:
        turn = turn + 1
        print(f"You are safe for now {p1}")
def p2_turn():
    global p1, p2, turn, chamber, win
    input(f'Fire the "Pew Pew" {p2}')
    if turn == chamber:
        win = 1
    else:
        turn = turn + 1
        print(f"You are safe for now {p2}")
def main():
    while True:
        global p1, p2, turn, chamber, win, dev
        p1_turn()
        if win == 1:
            print(f"{p2} WINS!!!")
            return
        else:
            p2_turn()
            if win == 1:
                print(f"{p1} WINS!!!")
                return
main()