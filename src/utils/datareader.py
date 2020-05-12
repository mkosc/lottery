# pylint: disable-msg=too-few-public-methods
"""
datareader - generic module for reading csv and json data
"""
import csv
import json
from pathlib import PurePath
from typing import List, Dict, Union

from src.properties.properties import DATA_DIR


class DataReader:

    def __init__(self, source_file: Union[str, PurePath]):
        self._source_file = source_file

    def _read_from_csv(self) -> List[Dict[str, str]]:
        """
        :return: lottery participants
        """
        participants = []
        with open(DATA_DIR / self._source_file) as file:
            reader = csv.DictReader(file)
            for row in reader:
                participants.append(row)
        return participants

    def _read_from_json(self) -> Union[List, Dict]:
        """
        :return: lottery participants or template
        """
        path = DATA_DIR / self._source_file
        with open(path, "r") as file:
            return json.load(file)
