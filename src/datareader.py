import csv
import json
import os
from pathlib import PurePath
from typing import List, Dict

from src.properties import DATA_DIR, TEMPLATE_FILES


class DataReader:

    @staticmethod
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

    @staticmethod
    def read_from_json(source_file: str) -> List[Dict[str, str]]:
        """
        :param source_file: source file name
        :return: lottery participants
        """
        with open(PurePath(__file__).parent.parent / DATA_DIR / source_file, "r") as file:
            return json.load(file)

    @staticmethod
    def read_data(source_file: str, file_type: str) -> List[Dict[str, str]]:
        """
        :param source_file: source file name without extension
        :param file_type: csv or json
        :return: lottery participants
        """
        if file_type == 'csv':
            return DataReader.read_from_csv(source_file + ".csv")
        else:
            return DataReader.read_from_json(source_file + ".json")

    @staticmethod
    def load_lottery_template(templates_path: str, template_type=None) -> Dict[str, Dict[int, str]]:
        """
        :param templates_path: path to templates directory
        :param template_type: lottery template type
        :return: dictionary with selected lottery prize template
        """

        if template_type is None:
            template_file = templates_path / os.listdir(templates_path)[0]
        else:
            template_file = templates_path / TEMPLATE_FILES[template_type]

        with open(template_file, "r") as file:
            return json.load(file)
