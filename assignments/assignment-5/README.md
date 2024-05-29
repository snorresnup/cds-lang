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