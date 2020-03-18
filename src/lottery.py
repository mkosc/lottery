from typing import List, Dict
from numpy import random
import click

from src.datareader import read_data, load_lottery_template
from src.datawriter import save_results_to_file


def print_winners(weighted: bool, participants: List[Dict[str, str]], template: Dict[str, Dict[int, str]],
                  output_file=None) -> None:
    """
    :param weighted: weighted or not
    :param participants: lottery participants
    :param template: dictionary with selected lottery prize template
    :param output_file: output file name
    :return: none
    """
    number_of_winners = 0

    for prize in template['prizes']:
        number_of_winners += prize['amount']

    if weighted:
        weights = [int(d['weight']) for d in participants]
        probabilities = [w / sum(weights) for w in weights]
    else:
        probabilities = None

    winners_ids = list(random.choice(range(len(participants)), size=number_of_winners, replace=False, p=probabilities))

    winners_data = {'prizes': []}
    print('Lottery winner(s):')
    for i, prize in enumerate(template['prizes']):
        print(prize['name'] + ":")
        for winner in range(prize['amount']):
            winner_name = participants[winners_ids[0]]['first_name'] + " " + participants[winners_ids[0]]['last_name']
            print(winner_name)
            winners_data['prizes'].append({
                'name': prize['name'],
                'winner': winner_name
            })
            winners_ids.pop(0)

    if output_file is not None:
        save_results_to_file(winners_data, output_file)


@click.command()
@click.option('-d', '--data', required=True, help='Data source file name')
@click.option('-ft', '--file-type', default='json', help='Data source file type: json or csv', show_default=True)
@click.option('-t', '--template', help='Lottery template file name')
@click.option('-o', '--output', help='Lottery template file name')
def main(data, file_type, template, output):
    is_weighted = file_type.endswith('2')
    participants = read_data(data, file_type)
    template = load_lottery_template(template)
    print_winners(is_weighted, participants, template, output)


if __name__ == '__main__':
    main()
