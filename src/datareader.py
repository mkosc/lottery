import csv
import json
import os
from pathlib import Path
from src.properties import *


def get_source_file():
    if csv_or_json == "csv":
        if is_weighted:
            return participants_csv_weight_source
        else:
            return participants_csv_no_weight_source
    elif csv_or_json == "json":
        if is_weighted:
            return participants_json_weight_source
        else:
            return participants_json_no_weight_source
    else:
        print("Invalid file type selected.")


def read_from_csv(source_file):
    participants = []
    with open(os.getcwd() + source_file) as file:
        reader = csv.reader(file)
        next(reader, None)  # skip the header
        line_count = 0
        for row in reader:
            if is_weighted:
                participants.append({'id': row[0], 'first_name': row[1], 'last_name': row[2], 'weight': row[3]})
            else:
                participants.append({'id': row[0], 'first_name': row[1], 'last_name': row[2]})
            line_count += 1
    return participants


def read_from_json(source_file):
    with open(os.getcwd() + source_file, "r") as file:
        return json.load(file)


def read_data(source_file):
    file_type = Path(source_file).suffix
    if file_type == ".csv":
        return read_from_csv(source_file)
    elif file_type == ".json":
        return read_from_json(source_file)
    else:
        print("Unsupported file type")
