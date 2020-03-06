import random
from numpy import random as rn

from src.datareader import *
from src.properties import *


def print_winners(number_of_winners):
    participants = read_data(get_source_file())

    if is_weighted:
        weights = [int(d['weight']) for d in participants]
        probabilities = [w / sum(weights) for w in weights]
        winners_ids = rn.choice(range(1, len(participants) + 1), size=number_of_winners, replace=False, p=probabilities)
    else:
        winners_ids = random.sample(range(1, len(participants) + 1), number_of_winners)

    print("Lottery winner(s):")
    for winner in winners_ids:
        print(participants[winner]["first_name"] + " " + participants[winner]["last_name"])


def main():
    number_of_winners = input("Hello! Enter number of winners: ")
    if number_of_winners.isdigit():
        number_of_winners = int(number_of_winners)
        if 0 < number_of_winners < 31:
            print_winners(number_of_winners)
        else:
            print("Number of winners should be in range 1...30")
    else:
        print("Please enter numerical value")


main()
