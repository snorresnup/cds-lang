# load packages
import pandas as pd
import os
import argparse
import re
import sys
import gensim.downloader as api
from codecarbon import EmissionsTracker


def load_data():
    filepath = os.path.join("in", "Spotify Million Song Dataset_exported.csv")
    df = pd.read_csv(filepath, encoding = "latin-1")

    return df

def word_embed(search_term):
    model = api.load("glove-wiki-gigaword-50")
    similar_words = []
    for word, _ in model.most_similar(search_term):
        similar_words.append(word)
    
    return similar_words

def process(df, artist, search_term, similar_words):
    
    artist_df = df[df['artist'] == artist]
    
    search_term_df = artist_df[artist_df['text'].str.contains('|'.join(similar_words))]
    search_term_count = len(search_term_df)  
    all_count = len(artist_df)
    percentage = search_term_count/all_count*100
    print(f"{percentage:.2f}% of {artist}'s songs contain words related to: {search_term}. Similar words are {similar_words[:5]}")
    output_path = os.path.join("out", f"{artist.replace(' ', '_')}_{search_term.replace(' ', '_')}_results.txt")
    with open(output_path, 'w') as file:
        file.write(f"{percentage:.2f}% of {artist}'s songs contain words related to: {search_term}. Similar words are {similar_words[:5]}")


def main():
    tracker = EmissionsTracker(project_name=f"a3_emissions", 
        experiment_id=f"a3_emissions",
        output_dir=os.path.join("out","emissions"),
        output_file=f"a3_emissions.csv")
    tracker.start()

    parser = argparse.ArgumentParser(
                    description='Query expansion with word embeddings')
    parser.add_argument('search_term',  help= "Search term")
    parser.add_argument('artist', help= "Name of the artist")
    args = parser.parse_args()

    artist = args.artist
    search_term = args.search_term

    tracker.start_task("a3_load_data")
    df = load_data()
    tracker.stop_task()

    tracker.start_task("a3_load_model")
    similar_words = word_embed(search_term)
    tracker.stop_task()

    tracker.start_task("a3_find_similiar_words")
    process(df, artist, search_term, similar_words)
    tracker.stop_task()

    tracker.stop()

if __name__ == "__main__":
    main()