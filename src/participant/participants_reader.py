from typing import List, Dict

from src.utils.datareader import DataReader


class ParticipantsReader(DataReader):

    def __init__(self, source_file: str, file_type: str):
        self._file_type = file_type
        super().__init__(source_file + '.' + file_type)

    def read_participants_data(self) -> List[Dict[str, str]]:
        """
        :return: lottery participants
        """
        if self._file_type == 'csv':
            return self._read_from_csv()
        else:
            return self._read_from_json()
