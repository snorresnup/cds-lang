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