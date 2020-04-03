import os
from pathlib import PurePath
from typing import Dict, Union

from src.datareader import DataReader
from src.properties import TEMPLATE_FILES


class LotteryReader(DataReader):

    def __init__(self, templates_path: PurePath, template_type: str = None):
        self._templates_path = templates_path
        self._template_type = template_type
        if template_type is None:
            self._source_file = self._templates_path / sorted(os.listdir(self._templates_path))[0]
        else:
            self._source_file = self._templates_path / TEMPLATE_FILES[self._template_type]
        super().__init__(self._source_file.with_suffix('.json'))

    def read_lottery_data(self) -> Dict[str, Union[str, int]]:
        """
        :return: dictionary with selected lottery prize template
        """
        return self._read_from_json()
