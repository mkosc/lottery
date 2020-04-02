import json
from typing import Dict, List

from src.properties import OUTPUT_PATH


def save_results_to_file(data: Dict[str, List[str]], output_file: str) -> None:
    """
    :param data: dictionary with winners data
    :param output_file: output file name
    :return: none
    """
    with open(OUTPUT_PATH / output_file, 'w') as output_file:
        json.dump(data, output_file)
