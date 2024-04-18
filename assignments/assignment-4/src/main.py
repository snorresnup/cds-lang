
# load packages
import pandas as pd
import matplotlib.pyplot as plt
from transformers import pipeline
import os

# load data
def load_data():
    datapath = os.path.join("..","data","Game_of_Thrones_Script.csv")
    df = pd.read_csv(datapath)
    specific_df = df.loc[:, ['Season', 'Sentence']]
    return specific_df

# process data
def process_data(specific_df):
    labels = []
    classifier = pipeline("text-classification", 
                      model="j-hartmann/emotion-english-distilroberta-base", 
                      return_all_scores=False)
    for line in specific_df["Sentence"]:
        label = classifier(line)
        labels.append(label[0]["label"])
    specific_df["labels"] = labels
    return specific_df

# plot analysis
def plot_analysis(specific_df):

    unique_seasons = specific_df['Season'].unique()
    unique_labels = specific_df['labels'].unique()
    
    # plot pie charts together
    fig, axs = plt.subplots(2, 4, figsize=(12, 6))
    axs = axs.flatten()

    for idx, season in enumerate(unique_seasons):
        season_data = specific_df[specific_df['Season'] == season]
        label_counts = season_data['labels'].value_counts()
        axs[idx].pie(label_counts, labels=label_counts.index, autopct='%1.1f%%', startangle=140)
        axs[idx].set_title(season)

    # Adjust layout
    plt.tight_layout()

    # Save the plot
    plt.savefig(os.path.join("..","out", "GoT_emotions.png"))

    # Show the plot
    plt.show()

def main():
    specific_df = load_data()
    specific_df = process_data(specific_df)
    specific_df = plot_analysis(specific_df)

if __name__ == "__main__":
    main()