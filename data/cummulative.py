import csv
from os import listdir
from os.path import isfile, join
import pickle

DATAPATH = "./data/"
NOUNS = "nouns/"
ADJ = "adjectives/"

noun_files = [f for f in listdir(DATAPATH + ADJ) if isfile(join(DATAPATH + ADJ, f))]

cummulative = []
for i in noun_files:
    file = open(DATAPATH + ADJ + i, "r")
    data = list(csv.reader(file, delimiter=","))
    print(i, len(data[0]))
    cummulative.extend(data[0])
    file.close()

with open(DATAPATH + ADJ + 'adjectives.pkl', 'wb') as f:
    pickle.dump(cummulative, f)
