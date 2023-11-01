import pickle
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

path = "Marvel_Comics.csv"

def preprocess():
    df = pd.read_csv(path)
    df.drop(columns=["active_years", 'Imprint', 'Format', 'Rating'], inplace=True)
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['issue_description'].values.astype('U'))
    pickle.dump(tfidf_matrix, open('tfidf.pickle', 'wb'))
    pickle.dump(tfidf, open('vector.pickle', 'wb'))

if __name__ == "__main__":
    preprocess()