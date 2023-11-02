import os
import re
import enhance
import recommender
import pandas as pd

dir = './result'
if not os.path.exists(dir):
    os.mkdir(dir)

def create_result(text):
    print('Creating Result for query')
    df1 = pd.read_csv("./recommendations/" + text + "_recommendations.csv")
    df2 = pd.read_csv("./extracts/" + text + ".csv")
    df2 = df2.astype({"cover_artist": type('')})
    merge_cols = ['comic_name','issue_title','publish_date','issue_description','penciler','writer','cover_artist','Price']
    for x in df1.columns:
        if df1.dtypes[x] != df2.dtypes[x]:
            print("Column: ", x)
    result = pd.merge(df1, df2, how="outer", on = merge_cols)
    cols_rem = []
    for x in result.columns:
        if 'Unnamed' in x:
            cols_rem.append(x)
    result.drop(cols_rem, axis=1, inplace=True)
    result.drop_duplicates(subset=merge_cols, inplace=True)
    result.to_csv("./result/" + text +".csv")

def clear_folders():
    for filename in os.listdir('./extracts'):
        if os.path.isfile(os.path.join('./extracts', filename)):
            os.remove(os.path.join('./extracts', filename))
    for filename in os.listdir('./recommendations'):
        if os.path.isfile(os.path.join('./recommendations', filename)):
            os.remove(os.path.join('./recommendations', filename))            
    for filename in os.listdir('./result'):
        if os.path.isfile(os.path.join('./result', filename)):
            os.remove(os.path.join('./result', filename))  
    print('Cleared extracts, recommendations and result directories')

if __name__ == "__main__":
    clear_folders()
    text = input("Enter text to search comic for: ")
    recommender.get_recommendations(text)
    enhance.make_extracts()
    create_result(text)
    print(f'The file {text}.csv contains the recommended comics for your input')
    
