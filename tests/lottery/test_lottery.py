# pylint: disable-msg=too-many-arguments, missing-module-docstring, missing-function-docstring, protected-access, no-self-use
import builtins
from unittest.mock import patch, call, ANY

from numpy import random
from pytest import fixture, mark

from src.lottery.lottery import Lottery
from src.participant.participant import Participant
from src.prize.prize import Prize
from src.utils.datawriter import DataWriter

MANY_PARTICIPANTS_WEIGHTED = [Participant('John', 'Doe', 5),
                              Participant('Johnny', 'Bravo', 3),
                              Participant('Adam', 'Smith', 1),
                              Participant('Andy', 'Brown', 1)]

MANY_PARTICIPANTS = [Participant('John', 'Doe'),
                     Participant('Johnny', 'Bravo'),
                     Participant('Adam', 'Smith'),
                     Participant('Andy', 'Brown')]

ONE_PARTICIPANT = [Participant('John', 'Doe')]

ONE_PRIZE = [Prize(1, 'prize', 1)]

TWO_PRIZES = [Prize(1, 'prize', 1), Prize(2, 'prize2', 1)]


class TestLottery:

    @fixture()
    def writer(self):
        return DataWriter('file')

    @mark.parametrize('lottery, number_of_participants, size, probabilities, winners_ids',
                      [(Lottery(MANY_PARTICIPANTS_WEIGHTED, ONE_PRIZE), 4, 1, [0.5, 0.3, 0.1, 0.1], [0]),
                       (Lottery(MANY_PARTICIPANTS, ONE_PRIZE), 4, 1, [0.25, 0.25, 0.25, 0.25], [0]),
                       (Lottery(MANY_PARTICIPANTS, TWO_PRIZES), 4, 2, [0.25, 0.25, 0.25, 0.25], []),
                       (Lottery(ONE_PARTICIPANT, TWO_PRIZES), 1, 2, [1.0], [0]),
                       (Lottery(ONE_PARTICIPANT, ONE_PRIZE), 1, 1, [1.0], [0]),
                       (Lottery(ONE_PARTICIPANT, []), 1, 0, [1.0], []),
                       (Lottery(MANY_PARTICIPANTS, []), 4, 0, [0.25, 0.25, 0.25, 0.25], []),
                       (Lottery([], ONE_PRIZE), 0, 1, [], []),
                       (Lottery([], TWO_PRIZES), 0, 2, [], []),
                       (Lottery([], []), 0, 0, [], [])
                       ]
                      )
    @patch.object(random, 'choice', autospec=True)
    def test_lottery_get_winners(self, choice_mock, lottery, number_of_participants, size, probabilities, winners_ids):
        choice_mock.return_value = winners_ids
        lottery.get_winners()
        choice_mock.assert_called_once_with(range(0, number_of_participants), size=size, replace=False, p=probabilities)
        assert lottery._winners_ids == winners_ids

    @mark.parametrize('lottery, winners_ids, calls, expected_winners_data',
                      [(Lottery(MANY_PARTICIPANTS, ONE_PRIZE),
                        [2],
                        [call('Lottery winner(s):'), call('prize:'), call('Adam Smith')],
                        {'prizes': [{'name': 'prize', 'winner': 'Adam Smith'}]}),
                       (Lottery(MANY_PARTICIPANTS, TWO_PRIZES),
                        [0, 2],
                        [call('Lottery winner(s):'), call('prize:'), call('John Doe'), call('prize2:'),
                         call('Adam Smith')],
                        {'prizes': [{'name': 'prize', 'winner': 'John Doe'},
                                    {'name': 'prize2', 'winner': 'Adam Smith'}]}),
                       (Lottery(ONE_PARTICIPANT, TWO_PRIZES),
                        [0],
                        [call('There are less participants than prizes.')],
                        None),
                       (Lottery(ONE_PARTICIPANT, ONE_PRIZE),
                        [0],
                        [call('Lottery winner(s):'), call('prize:'), call('John Doe')],
                        {'prizes': [{'name': 'prize', 'winner': 'John Doe'}]}),
                       (Lottery(ONE_PARTICIPANT, []),
                        [],
                        [call('There are no winners or prizes.')],
                        None),
                       (Lottery(MANY_PARTICIPANTS, []),
                        [],
                        [call('There are no winners or prizes.')],
                        None),
                       (Lottery([], ONE_PRIZE),
                        [],
                        [call('There are no winners or prizes.')],
                        None),
                       (Lottery([], TWO_PRIZES),
                        [],
                        [call('There are no winners or prizes.')],
                        None),
                       (Lottery([], []),
                        [],
                        [call('There are no winners or prizes.')],
                        None)
                       ]
                      )
    @patch.object(builtins, 'print', autospec=True)
    def test_lottery_print_winners(self, print_mock, lottery, winners_ids, calls, expected_winners_data):
        lottery._winners_ids = winners_ids
        lottery.print_winners()
        print_mock.assert_has_calls(calls)
        assert lottery._winners_data == expected_winners_data

    @mark.parametrize('lottery', [Lottery(MANY_PARTICIPANTS_WEIGHTED, ONE_PRIZE)])
    @patch.object(DataWriter, 'save_results_to_file', autospec=True)
    def test_lottery_save_winners(self, save_results_mock, lottery):
        winners_data = {'prizes': [{'name': 'prize', 'winner': 'Johnny Bravo'}]}
        lottery._winners_data = winners_data
        lottery.save_winners('file')
        save_results_mock.assert_called_with(ANY, winners_data)
