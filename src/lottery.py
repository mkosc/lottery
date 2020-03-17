from typing import List, Dict
from numpy import random

from src.datareader import read_data, get_source_file
from src.properties import CSV_OR_JSON, WEIGHTED_OR_NOT


def print_winners(number_of_winners: int, file_type: str, weighted: str, participants: List[Dict[str, str]]) -> None:
    """
    :param number_of_winners:
    :param file_type: csv or json
    :param weighted: weighted or not_weighted
    :param participants: lottery participants
    :return: none
    """

    if weighted == 'weighted':
        weights = [int(d['weight']) for d in participants]
        probabilities = [w / sum(weights) for w in weights]
    else:
        probabilities = None

    winners_ids = random.choice(range(len(participants)), size=number_of_winners, replace=False, p=probabilities)

    print("Lottery winner(s):")
    for winner in winners_ids:
        print(participants[winner]["first_name"] + " " + participants[winner]["last_name"])


def main():
    participants = read_data(get_source_file(CSV_OR_JSON, WEIGHTED_OR_NOT), CSV_OR_JSON)
    max_participants = len(participants)
    try:
        number_of_winners = int(input("Hello! Enter number of winners: "))
    except ValueError:
        print("Please enter numerical value")
    else:
        if 0 < number_of_winners <= max_participants:
            print_winners(number_of_winners, CSV_OR_JSON, WEIGHTED_OR_NOT, participants)
        else:
            print("Number of winners should be in range 1... " + str(max_participants))


if __name__ == '__main__':
    main()
