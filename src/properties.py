from pathlib import PurePath

# data source
DATA_DIR = 'data'
TEMPLATES_DIR = 'lottery_templates'
OUTPUT_DIR = 'data'
TEMPLATES_PATH = PurePath(__file__).parent.parent / DATA_DIR / TEMPLATES_DIR

TEMPLATE_FILES = {
    'item_giveaway': 'item_giveaway.json',
    'separate_prizes': 'separate_prizes.json'
}
