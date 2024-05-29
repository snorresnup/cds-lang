# Cultural Data Science - Language Analytics
- Author: Snorre Alsted Søndergaard
- Date: May 31th 2024
- Teacher: Ross Dean Kristensen-MacLachlan

# Assignment 1:
### Short description:
This assignment shows how you can use `spaCy` to extract linguistic information from a large textual dataset. The script extracts linguistic information from the The Uppsala Student English Corpus. The script loops over each text file in the 14 different folders, and extracts the relative frequency of nouns, verbs, adverbs, and adjectives per 10,000 words, and the total number of unique person, location, and organisation names. This information is displayed in a `.csv` file for each folder. The script also uses `CarbonCode` in order to track the code's carbon emissions, which will be expanded on in Assignment 5.

### Data source:
The dataset The Uppsala Student English Corpus (USE) consists of 1,489 essays written by 440 Swedish university students of English at three different levels. The data can be found [here](https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2457).

### Repository structure:
The repository contains:

- `in` folder in which to manually put downloaded data.
- `out` folder containing `.csv` files for each of the assignments, each displaying the extracted linguistic information. Also contains the `emissions` folder containg the outputs from `CarbonCode`.
- `src` folder containg the `main.py` file
- `README.md` file
- `requirements.txt` file containing all required packages 
- `run.sh` file to run the script
- `setup.sh` file to create virtual environment and install required packages prior to running the script

### Reproducing the analysis:

1. Download the date from [here](https://ota.bodleian.ox.ac.uk/repository/xmlui/bitstream/handle/20.500.12024/2457/USEcorpus.zip?sequence=5&isAllowed=y), open the `.zip` file and place the `USEcorpus` folder in the `in` folder.

2. In order to do the setup before running the script, create a virtual environment, install the required packages and deactivate the virtual environment again by running `bash setup.sh` in the terminal.

3. In order to run the script, activate the virtual environment, run the script and deactivate the virtual environment by running `bash run.sh` in the terminal.

4. In order to see the results of the script open the `out` folder.

### Discussion/summary:
The script displays how `spaCy` accurately identifies word classes and efffectively extracts linguistic information from a large dataset. Below I have displayed the linguistic information extracted from the first 7 essays of 3 different assignments across the 3 different levels. I have chosen these assignments, because they are all described as literature assignments for better comparability. Looking at the relative frequency of nouns, verbs, adjectives and adverbs it is difficult to see a changing pattern across the levels. The only apparent change is in unique person names, that seem to increase the higher the level. This might indicate some kind of progress in the complexity of the essays, as they include a wider reference to difference names. The description of dataset states that most of the essays are round 800 words, but this is not the case for the essays in `c1`, that are around 2000 words, which my explain why the Unique PER count is higher. Furthermore, the `c1` essays are the only ones with a bibliography, which naturally involves more person names.


`a4: Literature Course Assignment`
|Filename|RelFreq Noun|RelFreq VERB|RelFreq ADJ|RelFreq ADV|Unique PER|Unique LOC|Unique ORGS|
|--------|------------|------------|-----------|-----------|----------|----------|-----------|
|0102.a4.txt|1555.34     |1106.87     |562.98     |343.51     |10        |0         |0          |
|0103.a4.txt|984.37      |1181.24     |411.12     |295.31     |11        |0         |0          |
|0104.a4.txt|1471.14     |1108.01     |642.46     |381.75     |4         |0         |0          |
|0105.a4.txt|1391.69     |1133.56     |538.72     |718.29     |6         |0         |0          |
|0106.a4.txt|1362.32     |1062.8      |705.31     |405.8      |7         |0         |0          |
|0107.a4.txt|1513.03     |1302.61     |651.3      |430.86     |5         |0         |0          |
|0108.a4.txt|1425.99     |1290.61     |613.72     |388.09     |8         |0         |0          |

`b4: English Literature Assignment`
|Filename|RelFreq Noun|RelFreq VERB|RelFreq ADJ|RelFreq ADV|Unique PER|Unique LOC|Unique ORGS|
|--------|------------|------------|-----------|-----------|----------|----------|-----------|
|0103.b4.txt|1330.31     |1133.79     |589.57     |453.51     |7         |0         |0          |
|0105.b4.txt|1196.94     |1154.5      |517.83     |543.29     |12        |0         |0          |
|0107.b4.txt|1791.04     |1229.57     |646.77     |241.65     |10        |0         |0          |
|0139.b4.txt|1504.66     |1071.9      |512.65     |306.26     |9         |0         |0          |
|0140.b4.txt|1151.02     |1118.37     |391.84     |465.31     |10        |0         |0          |
|0158.b4.txt|1366.46     |1193.93     |600.41     |559.01     |14        |0         |0          |
|0165.b4.txt|1157.98     |989.26      |429.45     |368.1      |10        |0         |0          |


`c1: Literature Course Assignments`
|Filename|RelFreq Noun|RelFreq VERB|RelFreq ADJ|RelFreq ADV|Unique PER|Unique LOC|Unique ORGS|
|--------|------------|------------|-----------|-----------|----------|----------|-----------|
|0140.c1.txt|1565.92     |929.01      |470.59     |401.62     |38        |0         |0          |
|0165.c1.txt|1734.03     |812.45      |578.01     |282.94     |27        |0         |0          |
|0200.c1.txt|1170.59     |1015.51     |645.32     |505.25     |17        |0         |0          |
|0219.c1.txt|1368.42     |967.11      |559.21     |480.26     |26        |0         |0          |
|0238.c1.txt|1082.75     |1152.36     |394.43     |286.16     |19        |0         |0          |
|0501.c1.txt|1221.84     |1017.06     |457.34     |423.21     |14        |0         |0          |
|0502.c1.txt|1311.79     |1210.39     |430.93     |405.58     |15        |0         |0          |

### Limitations and improvement
- The script is limited in the sense, that it does not provide much visual illustration of the extracted linguistic information, making it difficult to conclude much about the developement across the levels. 
- An improvement would be to turn the extracted information into more intuitive visualisations and generalising across all essays in each assignment category instead of simply looking at a few examples. 

# Assignment 2:
### Short description:
This project shows how you can use simple classification models on text data. In this case on The Fake News Dataset, in order to test the classifications models accruracy in determening whether a text is "fake news" or not. The first script `LogReg.py` vectorizes the data using `sklearn` and saves it, so the next script `NeuNet.py` does not have to. Then the scripts each train a logistic regression classifier and a neural network classifier on the dataset, and outputs a classification report for each classifier, allowing for comparison of the performance of the different classifiers. The script also uses `CarbonCode` in order to track the code's carbon emissions, which will be expanded on in Assignment 5.

### Data source:
The Fake News dataset consists of 10558 different articles of which one half is "fake news" and the other is "real news". The dataset can be found [here](https://github.com/lutzhamel/fake-news/tree/master/data).

### Repository structure:
The repository contains:

- `in` folder in which to manually put downloaded data.
- `models` folder containing the two classifiers `LR_classifier.joblib` and `MLP_classifier.joblib` and the vectorizer `tfidf_vectorizer.joblib`.
- `out` folder containing each classification report. Also contains the `emissions` folder containg the outputs from `CarbonCode`.
- `src` folder containg the two scripts `LogReg.py` and `NeuNet.py`
- `README.md` file
- `requirements.txt` file containing all required packages 
- `run.sh` file to run the script
- `setup.sh` file to create virtual environment and install required packages prior to running the script

### Reproducing the analysis:

1. Download the date from [here](https://github.com/lutzhamel/fake-news/tree/master/data) and place the `fake_or_real_news.csv` file in the `in` folder.

2. In order to do the setup before running the script, create a virtual environment, install the required packages and deactivate the virtual environment again by running `bash setup.sh` in the terminal.

3. In order to run the script, activate the virtual environment, run the script and deactivate the virtual environment by running `bash run.sh` in the terminal.

4. In order to see the results of the script open the `out` folder.


### Discussion/summary:
The two classifiers perform almost identically. The accuracy is only slightly higher in the neural network with a weighted average of 0.92, while the weighted accuracy for the logistic regression is 0.91. It is therefore difficult to conclude much about how neural network and logistic regression classifiers perform differently on the basis of this project. The overall conclusion is that both models are very accurate in the classification of fake and real news, showcasing how machine learning could be an efficient tool against the proliferation of fake news.

### Limitations and improvement
- While each of the classifiers perform quite well, there is still room for improvement. Tweaking the parameteres for both classifiers might yield better results, and using a more complex neural network will likely perform better, but would also be more computaionally intensive.  

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

# Assignment 4:
### Short description:
This project shows how you can use a pretrained language model to predict the emotion expressed in a line of text. In this case it concerns all the lines from all the seasons of the series Game of Thrones. The script uses the pretrained language model `j-hartmann/emotion-english-distilroberta-base` to predict emotion, saves a .csv file with the emotion of each line and then visualises the results in pie charts. The script also uses `CarbonCode` in order to track the code's carbon emissions, which will be expanded on in Assignment 5.

### Data source:
The dataset consists of all the lines from all the seaons of the series Game of Thrones. The dataset can be found [here](https://www.kaggle.com/datasets/albenft/game-of-thrones-script-all-seasons?select=Game_of_Thrones_Script.csv).

### Repository structure:
The repository contains:

- `in` folder in which to manually put downloaded data.
- `out` folder containing the `each_season_emotions.png`, `emotions_df.csv` and `relative_frequency_emotions.png` files. Also contains the `emissions` folder containg the outputs from `CarbonCode`.
- `src` folder containg the `main.py` script
- `README.md` file
- `requirements.txt` file containing all required packages 
- `run.sh` file to run the script
- `setup.sh` file to create virtual environment and install required packages prior to running the script

### Reproducing the analysis:

1. Download the date from [here](https://www.kaggle.com/datasets/albenft/game-of-thrones-script-all-seasons?select=Game_of_Thrones_Script.csv) open the `.zip` file and place the `Game_of_Thrones_Script.csv` file in the `in` folder.

2. In order to do the setup before running the script, create a virtual environment, install the required packages and deactivate the virtual environment again by running `bash setup.sh` in the terminal.

3. In order to run the script, activate the virtual environment, run the script and deactivate the virtual environment by running `bash run.sh` in the terminal.

4. In order to see the results of the script open the `out` folder.


### Discussion/summary:
The script outputs the following: `emotions_df.csv` file containing the predicted emotion for each line, `each_season_emotions.png` displaying the relative frequency of predicted emotions for each season, and `relative_frequency_emotions.png` displaying the relative frequency of emotions for all seasons. The script seems to be performing well, giving an insight into the emotions being expressed in Game of Thrones. `each_season_emotions.png` reveals that there is very little variation in emotions across the seaons. `relative_frequency_emotions.png` revals that the script defines 48.1% of the lines as neutral, 15.9% as anger, 11.5% as surprise and 10.1% as disgust, which makes sense if you have seen the series, and assume that most lines will naturally be neutral. However, when looking into the `emotions_df.csv` file it becomes apparent that some lines are oddly classified. For example the identical lines 133 and 134: "My queen" are both labeled as "disgust", revealing an odd classification (maybe even revealing a slightly male chauvinist bias in the language model?).

### Limitations and improvement
- While the script works relatively well, it is also apparent that it classifies in slightly odd ways, suggesting a need for a different language model, that does not label "My queen" as disgust, or a more complex model capable of including more context.
- The fact that there is barely any variation between seasons might not mean that the emotions are consistent through the seaons, but instead that the model simply has a tendency to classify most words as neutral and fewest words as joy, and would therefore show similar results regardless of the dataset. Further improvement would therefore be to chech if the distribution of emotions is similar on other textual databases. 

# Assignment 5:
### Short description:
This project shows how you can track the carbon emissions generated when running code. Using `CodeCarbon` to track each assignment and each task in the form of .csv files allows for a visualisation of the carbon generated from running the 4 prior assignments, giving an insight into exactly which tasks the most computationally demanding. 

### Data source:
The dataset consists of all the emission.csv files from each assignment and each task within produced by `CodeCarbon`. The dataset can be found in the `in` folder.

### Repository structure:
The repository contains:

- `in` folder containg the emission file for each assignment, and the `tasks` folder containg the emission file for each task in the assignments.
- `out` folder containing the `assignment_emission.png` and `task_emission.png` files
- `src` folder containg the `main.py` script
- `README.md` file
- `requirements.txt` file containing all required packages 
- `run.sh` file to run the script
- `setup.sh` file to create virtual environment and install required packages prior to running the script

### Reproducing the analysis:

1. In order to do the setup before running the script, create a virtual environment, install the required packages and deactivate the virtual environment again by running `bash setup.sh` in the terminal.

2. In order to run the script, activate the virtual environment, run the script and deactivate the virtual environment by running `bash run.sh` in the terminal.

3. In order to see the results of the script open the `out` folder.


### Discussion/summary:
The script outputs the `assignment_emission.png` file showing the carbon emission of each assignment, revealing that the most computationally intensive assignments are Assignment 1 and 4. The `task_emission.png` file showing the carbon emission of each task, reveals that in Assignment 4 it is the task `a4_classify_data` that classifies each line in the huge `Game_of_Thrones_Script.csv` dataset with an emotion score using a pretrained language model. While Assignemt 1 only has one task, it also includes text classification of a huge dataset based on a language model. This reveals, that while these language models are very effective, they are also very computationally intensive. Looking at the carbon emission from training a logstic regression classifier in the `a2_train_logreg_classifer` task in comparison to the neural network classifier `a2_train_neunet_classifer` task, reveals that the logistic regression task emits much less carbon, and as stated in Assignment 2, it performs almost exactly as well. Furthermore the amount of carbon emitted from the most demanding Assignemnt 4 is 0.003 KgCO2eq, which is only 3 grams. The US Environmental Protection Agency states that an average car emits 400 grams of CO2 per mile [source](https://www.epa.gov/greenvehicles/greenhouse-gas-emissions-typical-passenger-vehicle), making 3 grams seem insignificant. On the other hand, the computational tasks in this portfolio are indeed insignificant in comparison to the immensely intensive tasks involved in the many huge AI models around today. One study [source](https://arxiv.org/ftp/arxiv/papers/2104/2104.10350.pdf) reveals that the training of OpenAI's GPT-3 model resulted in the emisson of around 502,000 kg CO2. It is therefore necessary to think critically in regards to the carbon footprint of seemingly innocent computational tasks.

### Limitations and improvements
- The `CarbonCode` is limited in the sense that it calculates the amount of required electricity for the task and approximates the resulting emission of CO2, meaning that the outputs should be considered as giving insight into the matter, rather than precise and actual carbon emissions.
- An improvement would be to use the insights provided by `CarbonCode` to test different ways of improving the code in this portfolio in order to acieve a more efficient code with a smaller carbon footprint

