import os
import api_ends
import pandas as pd

dir = './extracts'
if not os.path.exists(dir):
    os.mkdir(dir)

def make_extracts():
    for x in os.listdir('./recommendations/'):
        name = x.split('_')[0]
        df = api_ends.get_comics(name)
        if df is None:
            names = pd.read_csv('./recommendations/'+x)['comic_name']
            names = list(set(names))
            print(names)
            extract = []
            for x in names:
                df = api_ends.get_comics(x)
                if df is not None:
                    extract.append(df)
            print(len(extract))
            continue
        else:
            path = name + ".csv"
            df.to_csv(os.path.join(dir, path))
            print(f'Saved character({name}) data')

if __name__ == "__main__":
    make_extracts()