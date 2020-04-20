from unittest.mock import patch

from pytest import fixture, mark

from src.participant.participants_reader import ParticipantsReader
from src.utils.datareader import DataReader


class TestParticipantsReader:

    @fixture()
    def reader(self, request):
        return ParticipantsReader('file', request.param)

    @patch.object(DataReader, '_read_from_json', autospec=True)
    @patch.object(DataReader, '_read_from_csv', autospec=True)
    @mark.parametrize('reader', ['csv'], indirect=True)
    def test_read_participants_from_csv(self, datareader_csv_mock, datareader_json_mock, reader):
        reader.read_participants_data()

        datareader_csv_mock.assert_called_once_with(reader)
        datareader_json_mock.assert_not_called()

    @patch.object(DataReader, '_read_from_json', autospec=True)
    @patch.object(DataReader, '_read_from_csv', autospec=True)
    @mark.parametrize('reader', ['json'], indirect=True)
    def test_read_participants_from_json(self, datareader_csv_mock, datareader_json_mock, reader):
        reader.read_participants_data()

        datareader_json_mock.assert_called_once_with(reader)
        datareader_csv_mock.assert_not_called()
