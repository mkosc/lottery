from typing import List

import click

from src.lottery import Lottery
from src.participant import Participant
from src.prize import Prize
from src.datareader import DataReader
from src.properties import TEMPLATES_PATH


def get_list_of_participants(data: str, file_type: str, is_weighted: bool) -> List[Participant]:
    """
    :param data: data source file name
    :param file_type: data source file type: json or csv
    :param is_weighted: weighted or not
    :return: list of Participants objects
    """
    participants_data = DataReader.read_data(data, file_type)
    participants = []
    for participant_id, participant in enumerate(participants_data):
        if is_weighted:
            participants.append(Participant(participant_id,
                                            participant['first_name'],
                                            participant['last_name'],
                                            participant['weight']))
        else:
            participants.append(Participant(participant_id,
                                            participant['first_name'],
                                            participant['last_name']))
    return participants


def get_list_of_prizes(template: str) -> List[Prize]:
    """
    :param template: lottery template file name
    :return: list of Prize objects
    """
    prizes_data = DataReader.load_lottery_template(TEMPLATES_PATH, template)
    prizes = []
    for prize in prizes_data['prizes']:
        prizes.append(Prize(prize['id'], prize['name'], prize['amount']))
    return prizes


@click.command()
@click.option('-d', '--data', required=True, help='Data source file name')
@click.option('-ft', '--file-type', default='json', help='Data source file type: json or csv',
              type=click.Choice(['json', 'csv'], case_sensitive=True), show_default=True)
@click.option('-t', '--template', help='Lottery template file name')
@click.option('-o', '--output', help='Output file name')
def main(data, file_type, template, output):
    is_weighted = file_type.endswith('2')
    participants = None
    prizes = None

    try:
        participants = get_list_of_participants(data, file_type, is_weighted)
    except FileNotFoundError:
        print('Wrong data source file name')
        quit()

    try:
        prizes = get_list_of_prizes(template)
    except KeyError:
        print('Wrong template file name')
        quit()

    lottery = Lottery(participants, prizes)
    lottery.print_winners(is_weighted, participants, output)


if __name__ == '__main__':
    main()
