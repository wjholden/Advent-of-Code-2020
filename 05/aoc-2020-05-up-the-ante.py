import random
import statistics

def board(seats, tickets, print_hey):
    need_to_board = tickets.copy()
    boarded = set()
    # So, this is what I found on StackOverflow as a method to select a random
    # element from a set. Please let me know if there is a better way.
    my_seat = random.choice(tuple(need_to_board))
    number_of_moves = 0
    while len(need_to_board) > 0:
        board = random.choice(tuple(need_to_board))
        need_to_board.remove(board)
        boarded.add(board)
        if board == my_seat:
            number_of_moves += 1
            places_i_can_go = seats.difference(boarded)
            my_seat = random.choice(tuple(places_i_can_go))
            print_hey and print(f"Hey, you're in my seat ({board: >3})! | {len(boarded): >3} boarded, {len(need_to_board): >3} waiting. | Ok, I will move to {my_seat: >3}.")
    return my_seat, number_of_moves

# convert the string representation of a seat into an 8-bit integer
def seat_id(s):
    return int(s.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"), 2)

# read 
with open("input.txt") as f:
    seats = sorted([seat_id(line.strip()) for line in f.readlines()])

min_seat = seats[1]
max_seat = seats[-2]

# We need our real seat to be selectable. I realize that we could trivially discover our seat from the set difference.
possible_seats = set([seats[0]] + list(range(min_seat, max_seat + 1)) + [seats[-1]])

# convert the list of seats into a a set for faster lookups
tickets = set(seats)

print("Upping the ante", board(possible_seats, tickets, True))

# Collect a sample of 1000 of these random runs to see what the average number of moves will be.
SAMPLE_SIZE = 1000
sample = [board(possible_seats, tickets, False)[1] for i in range(0, SAMPLE_SIZE)]
print("Average number of moves", statistics.mean(sample))