import csv
import json
from pathlib import PurePath
from src.properties import DATA_DIR, DATA_FILES


def get_source_file(file_type, weighted):
    return DATA_FILES[file_type][weighted]


def read_from_csv(source_file):
    participants = []
    with open(PurePath(__file__).parent.parent / DATA_DIR / source_file) as file:
        reader = csv.DictReader(file)
        for row in reader:
            participants.append(row)
    return participants


def read_from_json(source_file):
    with open(PurePath(__file__).parent.parent / DATA_DIR / source_file, "r") as file:
        return json.load(file)


def read_data(source_file, file_type):
    if file_type == 'csv':
        return read_from_csv(source_file)
    else:
        return read_from_json(source_file)
