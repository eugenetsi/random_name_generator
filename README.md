# Random Name Generator
This is a simple random name generator in the format <{adjective}{seperator} {noun}>, that I find useful in naming ML model versions.
  > Example: **orange_audi**
- The categories that fill `{adjective}` are:  
	- colors 
		-  [source](https://codepen.io/bagaski/full/RwKvybw )  
		- `./data/adjectives/colors.csv`  
	- languages 
		- [source](https://github.com/forxer/languages-list/blob/master/src/Languages.csv )
		- `./data/adjectives/languages.csv`
	- generic adjectives
		- [source](https://gist.github.com/hugsy/8910dc78d208e40de42deb29e62df913 )  
		- `./data/adjectives/generic_adj.csv`
- The categories that fill `{noun}` are:  
	- car brands  
		- [source](https://gist.github.com/OdeToCode/582e9c044eee5882d54a6e5997c0be52)
		- `./data/nouns/cars.csv`
	- animals
		- [source](https://www.kaggle.com/datasets/uciml/zoo-animal-classification)
		- `./data/nouns/animals.csv`
	- names
		-   [source](https://github.com/hadley/data-baby-names)
		- `./data/nouns/names.csv`
	- musical instruments
		- [source](https://simple.wikipedia.org/wiki/List_of_musical_instruments)
		- `./data/nouns/instruments.csv`
	- foods
		- [source](https://github.com/SlobodaStudio/food-nlp/blob/master/generic-food.csv)
		- `./data/nouns/food.csv`
	- alcohols
		- [source](https://github.com/jdmartinho/BartenderExaminer/blob/master/data/cocktails.csv)
		- `./data/nouns/drinks.csv`
- The csv files the serve as input for the random generation are either downloaded or web crawled from their respective sources, parsed and compiled into an easily loaded pickle in `./data`.  
- The `{seperator}` can be: `"-", "_" (default), " ", "."`  
- ## Usage  
	- after import call `get_name(sep='_')`  

## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
