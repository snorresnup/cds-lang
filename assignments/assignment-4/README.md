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
