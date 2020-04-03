from typing import List, Dict

from src.datareader import DataReader


class ParticipantsReader(DataReader):

    def __init__(self, source_file: str, file_type: str):
        self._file_type = file_type
        self._source_file = source_file + '.' + file_type
        super().__init__(self._source_file)

    def read_participants_data(self) -> List[Dict[str, str]]:
        """
        :return: lottery participants
        """
        if self._file_type == 'csv':
            return self._read_from_csv()
        else:
            return self._read_from_json()
