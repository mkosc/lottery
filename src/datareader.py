import csv
import json
import os
from pathlib import PurePath
from typing import List, Dict

from src.properties import DATA_DIR, TEMPLATES_DIR, TEMPLATE_FILES


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
    :param source_file: source file name without extension
    :param file_type: csv or json
    :return: lottery participants
    """
    if file_type == 'csv':
        return read_from_csv(source_file + ".csv")
    else:
        return read_from_json(source_file + ".json")


def load_lottery_template(template_type=None) -> Dict[str, Dict[int, str]]:
    """
    :param template_type: lottery template type
    :return: dictionary with selected lottery prize template
    """
    templates_path = PurePath(__file__).parent.parent / DATA_DIR / TEMPLATES_DIR

    if template_type is None:
        template_file = templates_path / os.listdir(templates_path)[0]
    else:
        template_file = templates_path / TEMPLATE_FILES[template_type]

    with open(template_file, "r") as file:
        return json.load(file)
