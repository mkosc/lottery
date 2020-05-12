# pylint: disable-msg=too-few-public-methods
"""
datawriter - generic module for writing json data to file
"""
import json
from typing import Optional, List, Dict

from src.properties.properties import OUTPUT_PATH

PrizeName = str
WinnerName = str
Winners = Dict[PrizeName, WinnerName]


class DataWriter:

    def __init__(self, output_file: str):
        self._output_file = output_file

    def save_results_to_file(self, data: Optional[List[Winners]]) -> None:
        """
        :param data: Dict data to write to file
        :return: none
        """
        with open(OUTPUT_PATH / self._output_file, 'w') as output_file:
            json.dump(data, output_file)
