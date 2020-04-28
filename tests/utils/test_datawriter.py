import builtins
import json
from unittest.mock import patch, ANY

from pytest import fixture

from src.properties.properties import OUTPUT_PATH
from src.utils.datawriter import DataWriter


class TestDataWriter:

    @fixture()
    def writer(self):
        return DataWriter('file')

    @patch.object(builtins, 'open', autospec=True)
    @patch.object(json, 'dump', autospec=True)
    def test_save_results_to_file(self, json_dump_mock, open_mock, writer):
        data = {'a': ['b', 'c', 'd']}
        writer.save_results_to_file(data)

        open_mock.assert_called_once_with(OUTPUT_PATH / 'file', 'w')
        json_dump_mock.assert_called_once_with(data, ANY)
