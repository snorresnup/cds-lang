# load packages
import pandas as pd
import matplotlib.pyplot as plt
from transformers import pipeline
import os
from codecarbon import EmissionsTracker

# load data
def load_data():
    datapath = os.path.join("in","Game_of_Thrones_Script.csv")
    df = pd.read_csv(datapath)
    specific_df = df.loc[:, ['Season', 'Sentence']]
    if 'Sentence' in specific_df.columns:
        specific_df['Sentence'] = specific_df['Sentence'].astype(str)
    
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
    specific_df.to_csv(os.path.join("out", "emotions_df.csv"), index=False)
    return specific_df

def plot_season_emotion(specific_df):
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

    plt.tight_layout()
    plt.savefig(os.path.join("out", "each_season_emotions.png"))
    plt.close()

def plot_all_emotion(specific_df):
    label_counts = specific_df['labels'].value_counts()
    
    plt.figure(figsize=(8, 8))
    plt.pie(label_counts, labels=label_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title("Relative Frequency of Emotions Across All Seasons")
    plt.savefig(os.path.join("out", "relative_frequency_emotions.png"))
    plt.close()

def main():
    tracker = EmissionsTracker(project_name=f"a4_emissions", 
        experiment_id=f"a4_emissions",
        output_dir=os.path.join("out","emissions"),
        output_file=f"a4_emissions.csv")
    tracker.start()

    tracker.start_task("a4_load_data")
    specific_df = load_data()
    tracker.stop_task()

    tracker.start_task("a4_classify_data")
    specific_df = process_data(specific_df)
    # specific_df = pd.read_csv(os.path.join("out","emotions_df.csv"))
    plot_season_emotion(specific_df)
    plot_all_emotion(specific_df)

    tracker.stop()

if __name__ == "__main__":
    main()