from pathlib import PurePath
from unittest.mock import patch, Mock

from pytest import fixture

from src.lottery.lottery_reader import LotteryReader
from src.utils.datareader import DataReader


class TestLotteryReader:

    @fixture()
    def reader(self):
        return LotteryReader(PurePath())

    @patch.object(DataReader, '_read_from_json', autospec=True)
    def test_read_lottery(self, datareader_json_mock, reader):
        mock = Mock()
        datareader_json_mock.return_value = mock
        actual = reader.read_lottery_data()

        assert actual is mock
        datareader_json_mock.assert_called_once_with(reader)
