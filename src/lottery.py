from numpy import random

from src.datawriter import DataWriter


class Lottery:

    def __init__(self, participants, prizes):
        self._participants = participants
        self._prizes = prizes

    def print_winners(self, output_file=None) -> None:
        """
        :param output_file: output file name
        :return: none
        """
        number_of_winners = sum(prize.amount for prize in self._prizes)

        weights = [d.weight for d in self._participants]
        probabilities = [w / sum(weights) for w in weights]

        winners_ids = list(
            random.choice(range(len(self._participants)), size=number_of_winners, replace=False, p=probabilities))

        winners_data = {'prizes': []}
        print('Lottery winner(s):')
        for i, prize in enumerate(self._prizes):
            print(prize.name + ":")
            for winner in range(prize.amount):
                winner_name = self._participants[winners_ids[0]].first_name + " " + self._participants[winners_ids[0]].last_name
                print(winner_name)
                winners_data['prizes'].append({
                    'name': prize.name,
                    'winner': winner_name
                })
                winners_ids.pop(0)

        if output_file is not None:
            DataWriter(winners_data, output_file).save_results_to_file()
