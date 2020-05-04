import builtins
from enum import Enum
from unittest.mock import patch, call, ANY

from numpy import random
from pytest import fixture, mark

from src.lottery.lottery import Lottery
from src.participant.participant import Participant
from src.prize.prize import Prize
from src.utils.datawriter import DataWriter


class TestLottery:
    class LotteryInputCases(Enum):
        MANY_PARTICIPANTS_ONE_PRIZE_WEIGHTED = 'many_participants_one_prize_weighted'
        MANY_PARTICIPANTS_ONE_PRIZE = 'many_participants_one_prize'
        MANY_PARTICIPANTS_MANY_PRIZES = 'many_participants_many_prizes'
        ONE_PARTICIPANT_ONE_PRIZE = 'one_participant_one_prize'
        ONE_PARTICIPANT_MANY_PRIZES = 'one_participants_many_prizes'
        MANY_PARTICIPANTS_NO_PRIZE = 'many_participants_no_prize'
        ONE_PARTICIPANT_NO_PRIZE = 'one_participant_no_prize'
        NO_PARTICIPANTS_ONE_PRIZE = 'no_participants_one_prize'
        NO_PARTICIPANTS_MANY_PRIZES = 'no_participants_many_prizes'
        NO_PARTICIPANTS_NO_PRIZES = 'no_participants_no_prizes'

    @fixture()
    def writer(self):
        return DataWriter('file')

    @mark.parametrize('lottery, case',
                      [(Lottery([Participant('John', 'Doe', 5),
                                 Participant('Johnny', 'Bravo', 3),
                                 Participant('Adam', 'Smith', 1),
                                 Participant('Andy', 'Brown', 1)],
                                [Prize(1, 'prize', 1)]), LotteryInputCases.MANY_PARTICIPANTS_ONE_PRIZE_WEIGHTED),
                       (Lottery([Participant('John', 'Doe'),
                                 Participant('Johnny', 'Bravo'),
                                 Participant('Adam', 'Smith'),
                                 Participant('Andy', 'Brown')],
                                [Prize(1, 'prize', 1)]), LotteryInputCases.MANY_PARTICIPANTS_ONE_PRIZE),
                       (Lottery([Participant('John', 'Doe'),
                                 Participant('Johnny', 'Bravo'),
                                 Participant('Adam', 'Smith'),
                                 Participant('Andy', 'Brown')],
                                [Prize(1, 'prize', 1),
                                 Prize(2, 'prize2', 1)]), LotteryInputCases.MANY_PARTICIPANTS_MANY_PRIZES),
                       (Lottery([Participant('John', 'Doe')],
                                [Prize(1, 'prize', 1),
                                 Prize(2, 'prize2', 1)]), LotteryInputCases.ONE_PARTICIPANT_MANY_PRIZES),
                       (Lottery([Participant('John', 'Doe')],
                                [Prize(1, 'prize', 1)]), LotteryInputCases.ONE_PARTICIPANT_ONE_PRIZE),
                       (Lottery([Participant('John', 'Doe')],
                                []), LotteryInputCases.ONE_PARTICIPANT_NO_PRIZE),
                       (Lottery([Participant('John', 'Doe'),
                                 Participant('Johnny', 'Bravo'),
                                 Participant('Adam', 'Smith'),
                                 Participant('Andy', 'Brown')],
                                []), LotteryInputCases.MANY_PARTICIPANTS_NO_PRIZE),
                       (Lottery([],
                                [Prize(1, 'prize', 1)]), LotteryInputCases.NO_PARTICIPANTS_ONE_PRIZE),
                       (Lottery([],
                                [Prize(1, 'prize', 1),
                                 Prize(2, 'prize2', 1)]), LotteryInputCases.NO_PARTICIPANTS_MANY_PRIZES),
                       (Lottery([], []), LotteryInputCases.NO_PARTICIPANTS_NO_PRIZES)
                       ],
                      )
    @patch.object(random, 'choice', return_value=[0, 2, 5], autospec=True)
    def test_lottery_get_winners(self, choice_mock, lottery, case):
        lottery.get_winners()

        if case == TestLottery.LotteryInputCases.MANY_PARTICIPANTS_ONE_PRIZE_WEIGHTED:
            number_of_participants = 4
            size = 1
            probabilities = [0.5, 0.3, 0.1, 0.1]
        elif case == TestLottery.LotteryInputCases.MANY_PARTICIPANTS_ONE_PRIZE:
            number_of_participants = 4
            size = 1
            probabilities = [0.25, 0.25, 0.25, 0.25]
        elif case == TestLottery.LotteryInputCases.MANY_PARTICIPANTS_MANY_PRIZES:
            number_of_participants = 4
            size = 2
            probabilities = [0.25, 0.25, 0.25, 0.25]
        elif case == TestLottery.LotteryInputCases.ONE_PARTICIPANT_MANY_PRIZES:
            number_of_participants = 1
            size = 2
            probabilities = [1.0]
        elif case == TestLottery.LotteryInputCases.ONE_PARTICIPANT_ONE_PRIZE:
            number_of_participants = 1
            size = 1
            probabilities = [1.0]
        elif case == TestLottery.LotteryInputCases.ONE_PARTICIPANT_NO_PRIZE:
            number_of_participants = 1
            size = 0
            probabilities = [1.0]
        elif case == TestLottery.LotteryInputCases.MANY_PARTICIPANTS_NO_PRIZE:
            number_of_participants = 4
            size = 0
            probabilities = [0.25, 0.25, 0.25, 0.25]
        elif case == TestLottery.LotteryInputCases.NO_PARTICIPANTS_ONE_PRIZE:
            number_of_participants = 0
            size = 1
            probabilities = []
        elif case == TestLottery.LotteryInputCases.NO_PARTICIPANTS_MANY_PRIZES:
            number_of_participants = 0
            size = 2
            probabilities = []
        elif case == TestLottery.LotteryInputCases.NO_PARTICIPANTS_NO_PRIZES:
            number_of_participants = 0
            size = 0
            probabilities = []

        choice_mock.assert_called_once_with(range(0, number_of_participants), size=size, replace=False, p=probabilities)
        assert lottery._winners_ids == [0, 2, 5]

    @mark.parametrize('lottery, winners_ids, case',
                      [(Lottery([Participant('John', 'Doe'),
                                 Participant('Johnny', 'Bravo'),
                                 Participant('Adam', 'Smith'),
                                 Participant('Andy', 'Brown')],
                                [Prize(1, 'prize', 1)]),
                        [2],
                        LotteryInputCases.MANY_PARTICIPANTS_ONE_PRIZE),
                       (Lottery([Participant('John', 'Doe'),
                                 Participant('Johnny', 'Bravo'),
                                 Participant('Adam', 'Smith'),
                                 Participant('Andy', 'Brown')],
                                [Prize(1, 'prize', 1),
                                 Prize(2, 'prize2', 1)]),
                        [0, 2],
                        LotteryInputCases.MANY_PARTICIPANTS_MANY_PRIZES),
                       (Lottery([Participant('John', 'Doe')],
                                [Prize(1, 'prize', 1),
                                 Prize(2, 'prize2', 1)]),
                        [0],
                        LotteryInputCases.ONE_PARTICIPANT_MANY_PRIZES),
                       (Lottery([Participant('John', 'Doe')],
                                [Prize(1, 'prize', 1)]),
                        [0],
                        LotteryInputCases.ONE_PARTICIPANT_ONE_PRIZE),
                       (Lottery([Participant('John', 'Doe')],
                                []),
                        [],
                        LotteryInputCases.ONE_PARTICIPANT_NO_PRIZE),
                       (Lottery([Participant('John', 'Doe'),
                                 Participant('Johnny', 'Bravo'),
                                 Participant('Adam', 'Smith'),
                                 Participant('Andy', 'Brown')],
                                []),
                        [],
                        LotteryInputCases.MANY_PARTICIPANTS_NO_PRIZE),
                       (Lottery([],
                                [Prize(1, 'prize', 1)]),
                        [],
                        LotteryInputCases.NO_PARTICIPANTS_ONE_PRIZE),
                       (Lottery([],
                                [Prize(1, 'prize', 1),
                                 Prize(2, 'prize2', 1)]),
                        [],
                        LotteryInputCases.NO_PARTICIPANTS_MANY_PRIZES),
                       (Lottery([], []),
                        [],
                        LotteryInputCases.NO_PARTICIPANTS_NO_PRIZES)
                       ],
                      )
    @patch.object(builtins, 'print', autospec=True)
    def test_lottery_print_winners(self, print_mock, lottery, winners_ids, case):
        lottery._winners_ids = winners_ids
        lottery.print_winners()

        expected_winners_data = None

        if case == TestLottery.LotteryInputCases.MANY_PARTICIPANTS_ONE_PRIZE:
            calls = [call('Lottery winner(s):'), call('prize:'), call('Adam Smith')]
            expected_winners_data = {'prizes': [{'name': 'prize', 'winner': 'Adam Smith'}]}
        elif case == TestLottery.LotteryInputCases.MANY_PARTICIPANTS_MANY_PRIZES:
            calls = [call('Lottery winner(s):'), call('prize:'), call('John Doe'), call('prize2:'), call('Adam Smith')]
            expected_winners_data = {'prizes': [{'name': 'prize', 'winner': 'John Doe'},
                                                {'name': 'prize2', 'winner': 'Adam Smith'}]}
        elif case == TestLottery.LotteryInputCases.ONE_PARTICIPANT_MANY_PRIZES:
            calls = [call('There are less participants than prizes.')]
        elif case == TestLottery.LotteryInputCases.ONE_PARTICIPANT_ONE_PRIZE:
            calls = [call('Lottery winner(s):'), call('prize:'), call('John Doe')]
            expected_winners_data = {'prizes': [{'name': 'prize', 'winner': 'John Doe'}]}
        elif case in (TestLottery.LotteryInputCases.ONE_PARTICIPANT_NO_PRIZE,
                      TestLottery.LotteryInputCases.MANY_PARTICIPANTS_NO_PRIZE,
                      TestLottery.LotteryInputCases.NO_PARTICIPANTS_ONE_PRIZE,
                      TestLottery.LotteryInputCases.NO_PARTICIPANTS_MANY_PRIZES,
                      TestLottery.LotteryInputCases.NO_PARTICIPANTS_NO_PRIZES):
            calls = [call('There are no winners or prizes.')]

        print_mock.assert_has_calls(calls)
        assert lottery._winners_data == expected_winners_data

    @mark.parametrize('lottery', [Lottery([Participant('John', 'Doe', 5),
                                           Participant('Johnny', 'Bravo', 3),
                                           Participant('Adam', 'Smith', 1),
                                           Participant('Andy', 'Brown', 1)],
                                          [Prize(1, 'prize', 1)])])
    @patch.object(DataWriter, 'save_results_to_file', autospec=True)
    def test_lottery_save_winners(self, save_results_mock, lottery, writer):
        winners_data = {'prizes': [{'name': 'prize', 'winner': 'Johnny Bravo'}]}
        lottery._winners_data = winners_data
        lottery.save_winners('file')
        save_results_mock.assert_called_with(ANY, winners_data)
