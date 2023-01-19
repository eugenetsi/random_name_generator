import random
import pickle

DATAPATH = "./data/"
NOUNS = "nouns/"
ADJ = "adjectives/"

def get_name(sep='_'):
    with open(DATAPATH + NOUNS + 'nouns.pkl', 'rb') as f:
        nouns = pickle.load(f)
    with open(DATAPATH + ADJ + 'adjectives.pkl', 'rb') as f:
        adjectives = pickle.load(f)
    if sep not in ['_', '-', '', '.']:
        raise Exception('Not valid separator')
    return f'{random.choice(adjectives)}{sep}{random.choice(nouns)}'

if __name__ == "__main__":
    print(get_name())
