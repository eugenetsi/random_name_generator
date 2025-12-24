import csv
from os import listdir
from os.path import isfile, join
import pickle

DATAPATH = "./data/"
NOUNS = "nouns/"
ADJ = "adjectives/"

adjective_sources = [
    f for f in listdir(DATAPATH + ADJ)
    if isfile(join(DATAPATH + ADJ, f)) and f.endswith(".csv")
]

cummulative = []
for filename in adjective_sources:
    file = open(DATAPATH + ADJ + filename, "r")
    data = list(csv.reader(file, delimiter=","))
    print(filename, len(data[0]))
    cummulative.extend(data[0])
    file.close()

with open(DATAPATH + ADJ + 'adjectives.pkl', 'wb') as f:
    pickle.dump(cummulative, f)
