import builtins
from unittest.mock import patch, call, ANY

from pytest import fixture

from src.lottery.lottery import Lottery
from src.participant.participant import Participant
from src.prize.prize import Prize
from src.utils.datawriter import DataWriter


class TestLottery:

    @fixture()
    def lottery(self):
        return Lottery([Participant('John', 'Doe')], [Prize(1, 'prize name', 1)])

    @fixture()
    def writer(self):
        return DataWriter('file')

    @patch.object(DataWriter, 'save_results_to_file', autospec=True)
    @patch.object(builtins, 'print', autospec=True)
    def test_lottery(self, print_mock, save_results_mock, lottery):
        lottery.print_winners()
        print_mock.assert_has_calls([call('Lottery winner(s):'), call('prize name:'), call('John Doe')])
        save_results_mock.assert_not_called()

    @patch.object(DataWriter, 'save_results_to_file', autospec=True)
    @patch.object(builtins, 'print', autospec=True)
    def test_lottery_with_save_file(self, print_mock, save_results_mock, lottery, writer):
        lottery.print_winners('file')
        print_mock.assert_has_calls([call('Lottery winner(s):'), call('prize name:'), call('John Doe')])
        save_results_mock.assert_called_with(ANY, {'prizes': [{'name': 'prize name', 'winner': 'John Doe'}]})
