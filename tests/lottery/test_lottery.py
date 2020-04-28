import builtins
from unittest.mock import patch, call, ANY

from numpy import random
from pytest import fixture, mark

from src.lottery.lottery import Lottery
from src.participant.participant import Participant
from src.prize.prize import Prize
from src.utils.datawriter import DataWriter


class TestLottery:

    @fixture()
    def lottery(self, request):
        if request.param:
            return Lottery([Participant('John', 'Doe', 5),
                            Participant('Johnny', 'Bravo', 3),
                            Participant('Adam', 'Smith', 1),
                            Participant('Andy', 'Brown', 1)],
                           [Prize(1, 'prize', 1)])
        else:
            return Lottery([Participant('John', 'Doe'),
                            Participant('Johnny', 'Bravo'),
                            Participant('Adam', 'Smith'),
                            Participant('Andy', 'Brown')],
                           [Prize(1, 'prize', 1)])

    @fixture()
    def writer(self):
        return DataWriter('file')

    @patch.object(random, 'choice', autospec=True)
    @mark.parametrize('lottery, is_weighted', [(True, True), (False, False)], indirect=['lottery'])
    def test_lottery_get_winners(self, choice_mock, lottery, is_weighted):
        lottery.get_winners()

        if is_weighted:
            probabilities = [0.5, 0.3, 0.1, 0.1]
        else:
            probabilities = [0.25, 0.25, 0.25, 0.25]

        choice_mock.assert_called_once_with(range(0, 4), size=1, replace=False, p=probabilities)

    @patch.object(builtins, 'print', autospec=True)
    @mark.parametrize('lottery', [True], indirect=True)
    def test_lottery_print_winners(self, print_mock, lottery):
        lottery._winners_ids = [1]
        lottery.print_winners()
        print_mock.assert_has_calls([call('Lottery winner(s):'), call('prize:'), call('Johnny Bravo')])

    @patch.object(DataWriter, 'save_results_to_file', autospec=True)
    @mark.parametrize('lottery', [True], indirect=True)
    def test_lottery_save_winners(self, save_results_mock, lottery, writer):
        winners_data = {'prizes': [{'name': 'prize', 'winner': 'Johnny Bravo'}]}
        lottery._winners_data = winners_data
        lottery.save_winners('file')
        save_results_mock.assert_called_with(ANY, winners_data)
