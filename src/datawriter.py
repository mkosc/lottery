import json
from typing import Dict, List

from src.properties import OUTPUT_PATH


class DataWriter:

    def __init__(self, data: Dict[str, List[str]], output_file: str):
        self._data = data
        self._output_file = output_file

    def save_results_to_file(self) -> None:
        with open(OUTPUT_PATH / self._output_file, 'w') as output_file:
            json.dump(self._data, output_file)
