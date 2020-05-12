# pylint: disable-msg=missing-module-docstring, missing-function-docstring, protected-access, no-self-use
import builtins
import csv
import json
from unittest.mock import patch, ANY

from pytest import fixture

from src.properties.properties import DATA_DIR
from src.utils.datareader import DataReader


class TestDataReader:

    @fixture()
    def reader(self):
        return DataReader('file')

    @patch.object(builtins, 'open', autospec=True)
    @patch.object(csv, 'DictReader', autospec=True)
    def test_read_from_csv(self, dict_reader_mock, open_mock, reader):
        reader._read_from_csv()

        open_mock.assert_called_once_with(DATA_DIR / 'file')
        dict_reader_mock.assert_called_once_with(ANY)

    @patch.object(builtins, 'open', autospec=True)
    @patch.object(json, 'load', autospec=True)
    def test_read_from_json(self, json_load_mock, open_mock, reader):
        reader._read_from_json()

        open_mock.assert_called_once_with(DATA_DIR / 'file', 'r')
        json_load_mock.assert_called_once_with(ANY)
