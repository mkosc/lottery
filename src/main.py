from typing import List

import click

from src.lottery import Lottery
from src.lottery_reader import LotteryReader
from src.participant import Participant
from src.participants_reader import ParticipantsReader
from src.prize import Prize
from src.properties import TEMPLATES_PATH


def get_list_of_participants(data: str, file_type: str) -> List[Participant]:
    """
    :param data: data source file name
    :param file_type: data source file type: json or csv
    :return: list of Participants objects
    """
    participants_data = ParticipantsReader(data, file_type).read_participants_data()
    participants = []
    for participant in participants_data:
        if "weight" in participant:
            participants.append(Participant(participant['first_name'],
                                            participant['last_name'],
                                            int(participant['weight'])))
        else:
            participants.append(Participant(participant['first_name'],
                                            participant['last_name']))
    return participants


def get_list_of_prizes(template: str) -> List[Prize]:
    """
    :param template: lottery template file name
    :return: list of Prize objects
    """
    prizes_data = LotteryReader(TEMPLATES_PATH, template).read_lottery_data()
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

    try:
        participants = get_list_of_participants(data, file_type)
    except FileNotFoundError:
        print('Wrong data source file name')
        return

    try:
        prizes = get_list_of_prizes(template)
    except KeyError:
        print('Wrong template file name')
        return

    lottery = Lottery(participants, prizes)
    lottery.print_winners(output)


if __name__ == '__main__':
    main()
