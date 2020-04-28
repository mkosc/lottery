from pathlib import PurePath
from unittest.mock import patch

from pytest import fixture

from src.lottery.lottery_reader import LotteryReader
from src.utils.datareader import DataReader


class TestLotteryReader:

    @fixture()
    def reader(self):
        return LotteryReader(PurePath())

    @patch.object(DataReader, '_read_from_json', autospec=True)
    def test_read_lottery(self, datareader_json_mock, reader):
        reader.read_lottery_data()

        datareader_json_mock.assert_called_once_with(reader)
