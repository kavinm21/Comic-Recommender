import os
import pickle
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

dir = './recommendations'
if not os.path.exists(dir):
    os.mkdir(dir)

def get_recommendations(title):
    tfidf_matrix = pickle.load(open('tfidf.pickle', 'rb'))
    tfidf = pickle.load(open('vector.pickle', 'rb'))
    df = pd.read_csv("Marvel_Comics.csv")
    vect_title = tfidf.transform([title])
    results = cosine_similarity(tfidf_matrix,vect_title).reshape((-1,))
    recommends = df.iloc[results.argsort()[-10:][::-1]]
    name = title+"_recommendations.csv"
    save_path = os.path.join(dir, name)
    recommends.to_csv(save_path)

if __name__ == "__main__":
    get_recommendations("Daredevil")