from numpy import random

from src.datareader import read_data, get_source_file
from src.properties import CSV_OR_JSON, WEIGHTED_OR_NOT


def print_winners(number_of_winners: int, file_type: str, weighted: str) -> None:
    """
    :param number_of_winners:
    :param file_type: csv or json
    :param weighted: weighted or not_weighted
    :return: none
    """
    participants = read_data(get_source_file(file_type, weighted), file_type)

    if weighted == 'weighted':
        weights = [int(d['weight']) for d in participants]
        probabilities = [w / sum(weights) for w in weights]
        winners_ids = random.choice(range(len(participants)), size=number_of_winners, replace=False, p=probabilities)
    else:
        winners_ids = random.choice(range(len(participants)), size=number_of_winners, replace=False)

    print("Lottery winner(s):")
    for winner in winners_ids:
        print(participants[winner]["first_name"] + " " + participants[winner]["last_name"])


def get_number_of_participants(file_type: str, weighted: str) -> int:
    """
    :param file_type: csv or json
    :param weighted: weighted or not_weighted
    :return: number of lottery
    """
    return len(read_data(get_source_file(file_type, weighted), file_type))


def main():
    max_participants = get_number_of_participants(CSV_OR_JSON, WEIGHTED_OR_NOT)
    try:
        number_of_winners = int(input("Hello! Enter number of winners: "))
        if 0 < number_of_winners <= max_participants:
            print_winners(number_of_winners, CSV_OR_JSON, WEIGHTED_OR_NOT)
        else:
            print("Number of winners should be in range 1... " + str(max_participants))
    except ValueError:
        print("Please enter numerical value")


if __name__ == '__main__':
    main()
