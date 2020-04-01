from typing import List
from numpy import random

from src.participant import Participant
from src.datawriter import DataWriter


class Lottery:

    def __init__(self, participants, prizes):
        self.participants = participants
        self.prizes = prizes

    def print_winners(self,
                      weighted: bool,
                      participants: List[Participant],
                      output_file=None) -> None:
        """
        :param weighted: weighted or not
        :param participants: lottery participants
        :param output_file: output file name
        :return: none
        """
        number_of_winners = sum(prize.amount for prize in self.prizes)

        if weighted:
            weights = [int(d['weight']) for d in participants]
            probabilities = [w / sum(weights) for w in weights]
        else:
            probabilities = None

        winners_ids = list(
            random.choice(range(len(participants)), size=number_of_winners, replace=False, p=probabilities))

        winners_data = {'prizes': []}
        print('Lottery winner(s):')
        for i, prize in enumerate(self.prizes):
            print(prize.name + ":")
            for winner in range(prize.amount):
                winner_name = participants[winners_ids[0]].first_name + " " + participants[winners_ids[0]].last_name
                print(winner_name)
                winners_data['prizes'].append({
                    'name': prize.name,
                    'winner': winner_name
                })
                winners_ids.pop(0)

        if output_file is not None:
            DataWriter.save_results_to_file(winners_data, output_file)
