import os
import numpy as np
import pandas as pd
from marvel import Marvel
from dotenv import load_dotenv

load_dotenv()
public_key = os.getenv('PUBLIC_KEY')
private_key = os.getenv('PRIVATE_KEY')


def get_comics(char_name):
    m = Marvel(public_key, private_key)
    comic_data = m.comics.all(titleStartsWith=char_name, dateRange="2019-01-01,2023-01-01", limit="100")
    if comic_data['data']['total'] == 0:
        print(f"Couldn't Extract ({char_name}) data")
        return None
    extract = comic_data['data']['results']
    data = []
    for i in range(len(extract)):
        obj = extract[i].copy()
        rem = ('id', 'digitalId', 'variantDescription', 'modified', 'isbn', 'upc', 'diamondCode', 'ean', 'issn', 'format', 'pageCount', 'textObjects', 'resourceURI', 'urls', 'variants', 'collections', 'collectedIssues', 'thumbnail', 'images', 'characters', 'stories', 'events')
        for k in rem:
            obj.pop(k, None)
        if type(obj['description']) == type(''):
            if len(obj['description']) < 2:
                obj['description'] = np.NaN
        for x in obj['creators']['items']:
            obj[x['role']] = x['name']
        obj.pop('creators', None)
        obj['series'] = obj['series']['name']
        for x in obj['dates']:
            obj[x['type']] = x['date']
        obj.pop('dates', None)
        for x in obj['prices']:
            obj[x['type']] = x['price']
        keys = obj.keys()
        if 'colorist (cover)' in keys:
            obj['cover artist'] = obj['colorist (cover)']
        elif 'inker (cover)' in keys:
            obj['cover artist'] = obj['inker (cover)']
        elif 'penciler (cover)' in keys:
            obj['cover artist'] = obj['penciler (cover)']
        if 'penciller' in keys and not 'penciler' in keys:
            obj['penciler'] = obj['penciller']
        if 'penciler' not in keys:
            if 'inker' in keys:
                obj['penciler'] = obj['inker']
            elif 'letterer' in keys:
                obj['penciler'] = obj['letterer']
        obj['comic_name'] = obj.pop('series')
        obj['issue_title'] = obj.pop('title')
        obj['issue_description'] = obj.pop('description')
        rem = ('prices', 'editor', 'painter', 'painter (cover)', 'digitalPurchasePrice', 'focDate', 'unlimitedDate', 'digitalPurchaseDate', 'penciller', 'penciller (cover)', 'colorist (cover)', 'inker (cover)', 'penciler (cover)', 'issueNumber', 'inker', 'letterer', 'colorist')
        for k in rem:
            obj.pop(k, None)
        obj['publish_date'] = obj.pop('onsaleDate')
        obj['Price'] = obj.pop('printPrice')
        if 'cover_artist' not in obj.keys():
            obj['cover_artist'] = None
        data.append(obj)
    extract_df = pd.DataFrame(data)
    cols = ['comic_name','issue_title','publish_date','issue_description','penciler','writer','cover_artist','Price']
    extract_df = extract_df[cols]
    print(f'Extracted ({char_name}) data')
    return extract_df

def get_all_comics(st, en):
    m = Marvel(public_key, private_key)
    comic_data = m.comics.all(dateRange=st+","+en, limit="100")
    extract = comic_data['data']['results']
    data = []
    for i in range(len(extract)):
        obj = extract[i].copy()
        rem = ('id', 'digitalId', 'variantDescription', 'modified', 'isbn', 'upc', 'diamondCode', 'ean', 'issn', 'format', 'pageCount', 'textObjects', 'resourceURI', 'urls', 'variants', 'collections', 'collectedIssues', 'thumbnail', 'images', 'characters', 'stories', 'events')
        for k in rem:
            obj.pop(k, None)
        if type(obj['description']) == type(''):
            if len(obj['description']) < 2:
                obj['description'] = np.NaN
        for x in obj['creators']['items']:
            obj[x['role']] = x['name']
        obj.pop('creators', None)
        obj['series'] = obj['series']['name']
        for x in obj['dates']:
            obj[x['type']] = x['date']
        obj.pop('dates', None)
        for x in obj['prices']:
            obj[x['type']] = x['price']
        keys = obj.keys()
        if 'colorist (cover)' in keys:
            obj['cover artist'] = obj['colorist (cover)']
        elif 'inker (cover)' in keys:
            obj['cover artist'] = obj['inker (cover)']
        elif 'penciler (cover)' in keys:
            obj['cover artist'] = obj['penciler (cover)']
        if 'penciller' in keys and not 'penciler' in keys:
            obj['penciler'] = obj['penciller']
        if 'penciler' not in keys:
            if 'inker' in keys:
                obj['penciler'] = obj['inker']
            elif 'letterer' in keys:
                obj['penciler'] = obj['letterer']
        obj['comic_name'] = obj.pop('series')
        obj['issue_title'] = obj.pop('title')
        rem = ('prices', 'editor', 'painter', 'painter (cover)', 'digitalPurchasePrice', 'focDate', 'unlimitedDate', 'digitalPurchaseDate', 'penciller', 'penciller (cover)', 'colorist (cover)', 'inker (cover)', 'penciler (cover)', 'issueNumber', 'inker', 'letterer', 'colorist')
        for k in rem:
            obj.pop(k, None)
        obj['publish_date'] = obj.pop('onsaleDate')
        obj['Price'] = obj.pop('printPrice')
        data.append(obj)
    extract_df = pd.DataFrame(data)
    extract_df.to_csv(st+"_"+en+".csv")
    print(f'Saved date range ({st}, {en})data')


if __name__ == "__main__":
    get_comics("Daredevil")
    get_all_comics("2023-01-01", "2023-05-01")
    get_comics("The Amazing Spider-Man")
    get_comics("Spider-Man")
    get_comics("Hawkeye")