"""
lottery - core application module
"""
from typing import List, Optional, Dict

from numpy import random

from src.participant.participant import Participant
from src.prize.prize import Prize
from src.utils.datawriter import DataWriter

PrizeName = str
WinnerName = str
Winners = Dict[PrizeName, WinnerName]


class Lottery:

    def __init__(self, participants: List[Participant], prizes: List[Prize]):
        self._participants = participants
        self._prizes = prizes
        self._winners_ids: Optional[List[int]] = None
        self._winners_data: Optional[List[Winners]] = None

    def get_winners(self) -> None:
        """
        :return: none
        """
        number_of_winners = sum(prize.amount for prize in self._prizes)

        weights = [d.weight for d in self._participants]
        probabilities = [w / sum(weights) for w in weights]

        self._winners_ids = list(
            random.choice(range(len(self._participants)), size=number_of_winners, replace=False, p=probabilities))

    def print_winners(self) -> None:
        """
        :return: none
        """
        if not (self._participants and self._prizes):
            print('There are no winners or prizes.')
            return
        if len(self._participants) < len(self._prizes):
            print('There are less participants than prizes.')
            return

        self._winners_data = []
        print('Lottery winner(s):')
        for prize in self._prizes:
            print(prize.name + ":")
            for _ in range(prize.amount):
                winner_name = self._participants[self._winners_ids[0]].first_name + " " + self._participants[
                    self._winners_ids[0]].last_name
                print(winner_name)
                self._winners_data.append({
                    'name': prize.name,
                    'winner': winner_name
                })
                self._winners_ids.pop(0)

    def save_winners(self, output_file: str) -> None:
        """
        :param output_file: output file name
        :return: none
        """
        DataWriter(output_file).save_results_to_file(self._winners_data)
