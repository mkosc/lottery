import json
from unittest.mock import patch, ANY

from pytest import fixture

from src.utils.datawriter import DataWriter


class TestDataWriter:

    @fixture()
    def writer(self):
        return DataWriter('file')

    @patch.object(json, 'dump', autospec=True)
    def test_read_participants_from_csv(self, json_dump_mock, writer):
        data = {'a': ['b', 'c', 'd']}
        writer.save_results_to_file(data)

        json_dump_mock.assert_called_once_with(data, ANY)
