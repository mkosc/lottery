import csv
import json
from pathlib import PurePath
from typing import List, Dict, Union

from src.properties import DATA_DIR


class DataReader:

    def __init__(self, source_file: str):
        self._source_file = source_file

    def _read_from_csv(self) -> List[Dict[str, str]]:
        """
        :return: lottery participants
        """
        participants = []
        with open(PurePath(__file__).parent.parent / DATA_DIR / self._source_file) as file:
            reader = csv.DictReader(file)
            for row in reader:
                participants.append(row)
        return participants

    def _read_from_json(self) -> Union[List, Dict]:
        """
        :return: lottery participants or template
        """
        with open(PurePath(__file__).parent.parent / DATA_DIR / self._source_file, "r") as file:
            return json.load(file)
