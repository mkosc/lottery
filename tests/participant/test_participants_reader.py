# pylint: disable-msg=missing-module-docstring, missing-function-docstring, no-self-use
from unittest.mock import patch, Mock

from pytest import fixture, mark

from src.participant.participants_reader import ParticipantsReader
from src.utils.datareader import DataReader


class TestParticipantsReader:

    @fixture()
    def reader(self, request):
        return ParticipantsReader('file', request.param)

    @patch.object(DataReader, '_read_from_json', autospec=True)
    @patch.object(DataReader, '_read_from_csv', autospec=True)
    @mark.parametrize('reader, is_csv', [('csv', True), ('json', False)], indirect=['reader'])
    def test_read_participants_data(self, datareader_csv_mock, datareader_json_mock, reader, is_csv):
        mock = Mock()
        datareader_csv_mock.return_value = mock
        datareader_json_mock.return_value = mock
        actual = reader.read_participants_data()

        assert actual is mock

        if is_csv:
            datareader_csv_mock.assert_called_once_with(reader)
            datareader_json_mock.assert_not_called()
        else:
            datareader_json_mock.assert_called_once_with(reader)
            datareader_csv_mock.assert_not_called()
