# Comic Recommender System
A Recommendation System project for DS course

## Requirements
- API keys (Public & Private) from Marvel
- Python version 3
- Libraries in requirements.txt

## How to Use
- Run preprocess.py if changing the dataset "Marvel_Comics.csv"
- Run Index.py, enter your query terms
- Open the file in result directory to view your comic recommendations

## To Note
- The files in extracts directory and recommendations directory are rewritten each time index.py is run
- The recommender may fail to provide recommendations if the query was not able to give any recommendations from the existing dataset
- The additional results in extracts directory are based on the results in the recommendations directory
