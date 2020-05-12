# pylint: disable-msg=too-few-public-methods
"""
lottery_reader - module for reading lottery data from template
"""
import os
from pathlib import PurePath
from typing import Dict, Union, List

from src.properties.properties import TEMPLATE_FILES
from src.utils.datareader import DataReader


class LotteryReader(DataReader):

    def __init__(self, templates_path: PurePath, template_type: str = None):
        super().__init__((templates_path / sorted(os.listdir(templates_path))[0]).with_suffix('.json')
                         if template_type is None
                         else (templates_path / TEMPLATE_FILES[template_type]).with_suffix('.json'))

    def read_lottery_data(self) -> Union[List, Dict]:
        """
        :return: dictionary with selected lottery prize template
        """
        return self._read_from_json()
