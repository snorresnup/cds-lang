# load packages
import pandas as pd
import os
import argparse
import re
import sys
import gensim.downloader as api

parser = argparse.ArgumentParser(
                    description='Query expansion with word embeddings')
parser.add_argument('search_term', help= "Search term")
parser.add_argument('artist', help= "Name of the artist")
args = parser.parse_args()

# load data
def load_data():
    filepath = os.path.join("..", "in", "Spotify Million Song Dataset_exported.csv")

    df = pd.read_csv(filepath, encoding = "latin-1")
    return df

# clean text
def clean_text(text):
    # function removes non-alphanumeric characters, removes whitespace and converts to lowercase
    cleaned_text = re.sub(r'\n|\W+', ' ', text).strip().lower()
    return cleaned_text

def word_embed(search_term):
    # function takes a given word and finds most similar words via word embedding
    model = api.load("glove-wiki-gigaword-50")
    similar_words = []
    for word, _ in model.most_similar(search_term):
        similar_words.append(word)
    return similar_words

def process(artist, search_term):
    df = load_data()
    # clean text in data
    df['text'] = df['text'].apply(clean_text)
    # find and list most similar words
    search_terms = word_embed(search_term)
    # create dataframe containing only the of the artist in the argument
    artist_df = df[df['artist'] == artist]
    # filter text column of dataframe to only include words from search_terms list 
    search_term_df = artist_df[artist_df['text'].str.contains('|'.join(search_terms))]
    search_term_count = len(search_term_df)  
    all_count = len(artist_df)
    percentage = search_term_count/all_count*100
    print(f"{percentage}% of {artist}'s songs contain words related to: {search_term}")


def main():
    artist = args.artist
    search_term = args.search_term
    process(artist, search_term)

if __name__ == "__main__":
    main()