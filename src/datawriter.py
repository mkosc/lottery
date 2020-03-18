import json
from pathlib import PurePath

from src.properties import OUTPUT_DIR


def save_results_to_file(data, output_file):
    with open(PurePath(__file__).parent.parent / OUTPUT_DIR / output_file, 'w') as output_file:
        json.dump(data, output_file)
