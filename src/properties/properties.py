from pathlib import PurePath

# data source
ROOT_DIR = PurePath(__file__).parent.parent.parent
DATA_DIR = ROOT_DIR / 'data'
TEMPLATES_DIR = 'lottery_templates'
OUTPUT_DIR = 'data'
TEMPLATES_PATH = ROOT_DIR / DATA_DIR / TEMPLATES_DIR
OUTPUT_PATH = ROOT_DIR / OUTPUT_DIR

TEMPLATE_FILES = {
    'item_giveaway': 'item_giveaway.json',
    'separate_prizes': 'separate_prizes.json'
}
