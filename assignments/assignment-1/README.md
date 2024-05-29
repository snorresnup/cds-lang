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
