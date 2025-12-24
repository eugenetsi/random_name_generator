import os
import random
import pickle

# Get the directory of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATAPATH = os.path.join(BASE_DIR, "data/")
NOUNS = "nouns/"
ADJ = "adjectives/"
ALLOWED_SEPARATORS = ['_', '-', '', '.', ' ']

def get_name(sep='_'):
    nouns_path = os.path.join(DATAPATH, NOUNS, 'nouns.pkl')
    adjectives_path = os.path.join(DATAPATH, ADJ, 'adjectives.pkl')

    with open(nouns_path, 'rb') as f:
        nouns = pickle.load(f)
    with open(adjectives_path, 'rb') as f:
        adjectives = pickle.load(f)

    if sep not in ALLOWED_SEPARATORS:
        raise Exception('Not valid separator')

    return f'{random.choice(adjectives)}{sep}{random.choice(nouns)}'

if __name__ == "__main__":
    print(get_name())
