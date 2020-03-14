import csv
import json
from pathlib import PurePath
from typing import List, Dict

from src.properties import DATA_DIR, DATA_FILES


def get_source_file(file_type: str, weighted: str) -> str:
    """
    :param file_type: csv or json
    :param weighted: weighted or not_weighted
    :return: source file name
    """
    return DATA_FILES[file_type][weighted]


def read_from_csv(source_file: str) -> List[Dict[str, str]]:
    """
    :param source_file: source file name
    :return: lottery participants
    """
    participants = []
    with open(PurePath(__file__).parent.parent / DATA_DIR / source_file) as file:
        reader = csv.DictReader(file)
        for row in reader:
            participants.append(row)
    return participants


def read_from_json(source_file: str) -> List[Dict[str, str]]:
    """
    :param source_file: source file name
    :return: lottery participants
    """
    with open(PurePath(__file__).parent.parent / DATA_DIR / source_file, "r") as file:
        return json.load(file)


def read_data(source_file: str, file_type: str) -> List[Dict[str, str]]:
    """
    :param source_file: source file name
    :param file_type: csv or json
    :return: lottery participants
    """
    if file_type == 'csv':
        return read_from_csv(source_file)
    else:
        return read_from_json(source_file)
