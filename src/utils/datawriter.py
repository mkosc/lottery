"""
datawriter - generic module for writing json data to file
"""
import json
from typing import Dict, List, Optional

from src.properties.properties import OUTPUT_PATH


class DataWriter:

    def __init__(self, output_file: str):
        self._output_file = output_file

    def save_results_to_file(self, data: Optional[Dict[str, List[Dict[str, str]]]]) -> None:
        """
        :param data: Dict data to write to file
        :return: none
        """
        with open(OUTPUT_PATH / self._output_file, 'w') as output_file:
            json.dump(data, output_file)
