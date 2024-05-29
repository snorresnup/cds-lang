# Assignment 3:
### Short description:
This project shows how you can use word embeddings to do query expansion. The script uses a pretrained model from `gensim` to take a given word as an input and finds the most similar words through word embeddings. The script performs this query expansion on the Spotify Million Song Dataset, finding all songs containing lyrics related to the given search term for a given artist. The script also uses `CarbonCode` in order to track the code's carbon emissions, which will be expanded on in Assignment 5.

### Data source:
The Spotify Million Song Dataset contains the lyrics of 57,650 songs. [here](https://www.kaggle.com/datasets/joebeachcapital/57651-spotify-songs).

### Repository structure:
The repository contains:

- `in` folder in which to manually put downloaded data.
- `out` folder containing `.txt` files for each query expansion performed. Also contains the `emissions` folder containg the outputs from `CarbonCode`.
- `src` folder containg the `main.py` file and the `print_artists.py` file
- `README.md` file
- `requirements.txt` file containing all required packages 
- `run_print_artists.sh` file to print all the different artists in the dataset
- `run.sh` file to run the script
- `setup.sh` file to create virtual environment and install required packages prior to running the script

### Reproducing the analysis:

1. Download the date from [here](https://www.kaggle.com/datasets/joebeachcapital/57651-spotify-songs) and place the `Spotify Million Song Dataset_exported.csv` file in the `in` folder.

2. In order to do the setup before running the script, create a virtual environment, install the required packages and deactivate the virtual environment again by running `bash setup.sh` in the terminal.

3. In order to see which artists are included in the dataset and can be searched for run the `run_print_artists.sh` script.

4. In order to run the script, activate the virtual environment, run the script and deactivate the virtual environment by running `bash run.sh "search_term" "artist"` in the terminal, and replacing "search_term" and "artist" with desired search term and artist.

5. In order to see some results of the script open the `out` folder.

### Discussion/summary:
The script seems to perform quickly and effectively. The scripts then prints the percentage of the artists songs related to the search term, and prints the 5 most similar words to the given search term, in order to get insight into which words the model considers similar. Furthermore, the printed result is saved as a `.txt` file in the `out` folder. I have saved 5 examples in said folder, illustrating how the model performs. Taylor_Swift_love_results.txt shows that `98.77%` of `Taylor Swift's` songs contains words related to `love`, wheras the words 'dream', 'life', 'dreams', 'loves', 'me' are considered similar. These results make immediate sense. However, in regards to the results from `ABBA` there is large difference between querying for the search terms `girl` with `89.38%` and `girls` with only `26.55%`, while these words are arguably semantically interchangable. Furthermore, querying for `drug` in `The Beatles` songs show `0%`, where some would argue that many of the songs and lyrics are indirectly referring to drugs.

### Limitations and improvement
- Overall the script performs well, but there seems to be some patterns in the word embeddings, that do not correspond exactly with how people consider words to be semantically similar. Furthermore the model is limited to very literal word embeddings and unable to catch more complex metaphors and references.
- An improvement would be a more complex model that is trained on sentences rather than words, in order 'read between the lines', and catch the less literal word relations. 