import random

# Author: Adrian Durci
# Date: 19/02/2023

def pick_best_move(p1_pos, p2_pos, n):
    if p2_pos[0]-p1_pos[0] < p2_pos[1]-p1_pos[1]: #
        move = "E"
    elif p2_pos[0]-p1_pos[0] > p2_pos[1]-p1_pos[1]:
        move = "S"
    else:
        move = random.choice(["S", "E"])
    if (move, p1_pos[1]) == ("S", n-1) or (move, p1_pos[0]) == ("E", n-1):
        move = {"S":"E","E":"S"}[move] # swap command
    if move == "E":
        return p1_pos[0]+1, p1_pos[1]
    return p1_pos[0], p1_pos[1]+1


def get_move():
    inp = input("Choose N (north/up) or W (west/left):\n>> \t")
    while inp[:1].lower() not in ("n", "w"):
        print("Invalid commad - try again")
        inp = input("Choose N (north/up) or W (west/left):\n>> \t")
    return inp.lower()

def print_game(p1_pos, p2_pos, n):
    splitline = "|-"*n + "|"
    to_print = []
    for i in range(n):
        # print(splitline)
        row = [" " for i in range(n)]
        if p1_pos[1] == i:
            row[p1_pos[0]] = "1"
        if p2_pos[1] == i:
            if row[p2_pos[0]] == "1":
                row[p2_pos[0]] = "X"
            else:
                row[p2_pos[0]] = "2"
        print("|" + "|".join(row) + "|")
    # print(splitline)


def run_challenge(n):
    print("\n\n### ### ###\n\nStarting a game on a grid {:d}x{:d}".format(n,n))
    print("You have a {:.7f}% chance of winning. Good luck!".format(pow(0.5, n)*100))
    p1_pos = (0,0)
    p2_pos = (n-1, n-1)
    has_p1_won = False
    while p1_pos != p2_pos and p1_pos != (n-1, n-1):
        print("\nCurrent state (x, y):\n P1 @", p1_pos, "; \tP2 @", p2_pos)
        print_game(p1_pos, p2_pos, n)

        if (not has_p1_won) and (p2_pos[0]-p1_pos[0] != p2_pos[1]-p1_pos[1] or min(p2_pos[0]-p1_pos[0], p2_pos[1]-p1_pos[1]) < 0):
            has_p1_won = True
            print("p1 can now win using deterministic moves.")
            skip = input("enter SKIP (or S) to skip to end of game and try again: \n>> \t")
            if skip.lower() in ("s", "skip"):
                break
        p1_pos = pick_best_move(p1_pos, p2_pos, n)
        print("P1 has picked their move.")
        while True:
            p2_move = get_move()
            if (p2_move, p2_pos[1]) == ("n", 0) or (p2_move, p2_pos[0]) == ("w", 0):
                print("Invalid move (outside of the grid map) - try again")
                continue
            elif p2_move == "n":
                p2_pos = p2_pos[0], p2_pos[1]-1
            elif p2_move == "w":
                p2_pos = p2_pos[0]-1, p2_pos[1]
            else:
                print("error/wrong command")
                continue
            break

    print_game(p1_pos, p2_pos, n)
    if p1_pos == p2_pos:
        print("P2 WINS by catching P1")
    elif p1_pos == (n-1, n-1):
        print("P1 WINS by reaching the GOAL")
    elif has_p1_won:
        print("P1 has won by deterministic assumption of the remaining play - there is a deterministic sequence of turns for P1 such that P2 can't win.")


def ask_query():
    return input("Select challenge size (5 or 10 or any other integer >= 2); or enter Q/QUIT to exit the program:\n>> \t")


if __name__ == "__main__":
    query = ask_query()
    while query.lower() not in ("q", "quit"):
        size = None
        try:
            size = int(query)
            assert size >= 2
        except Exception:
            print("Invalid command: \"", query, "\"\n\nTry again:\n")
            query = ask_query()
            continue
        run_challenge(size)

        query = ask_query()
    print("Exiting")
    input("Press anything to close.")
