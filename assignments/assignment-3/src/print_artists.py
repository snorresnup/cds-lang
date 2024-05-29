import pandas as pd
import os

def main():
    filepath = os.path.join("in", "Spotify Million Song Dataset_exported.csv")
    df = pd.read_csv(filepath, encoding = "latin-1")
    
    unique_names = df['artist'].unique()
    for name in unique_names:
        print(name)

if __name__ == "__main__":
    main()



