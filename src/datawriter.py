import json
from pathlib import PurePath
from typing import Dict, List

from src.properties import OUTPUT_DIR


class DataWriter:

    @staticmethod
    def save_results_to_file(data: Dict[str, List[str]], output_file: str) -> None:
        """
        :param data: dictionary with winners data
        :param output_file: output file name
        :return: none
        """
        with open(PurePath(__file__).parent.parent / OUTPUT_DIR / output_file, 'w') as output_file:
            json.dump(data, output_file)
