import os
import sys
import pandas as pd
import utils.classifier_utils as clf
from sklearn.model_selection import train_test_split, ShuffleSplit
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn import metrics
import matplotlib.pyplot as plt
from codecarbon import EmissionsTracker

def load_data():
    filename = os.path.join("in","fake_or_real_news.csv")
    data = pd.read_csv(filename, index_col=0)

    X = data["text"]
    y = data["label"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 
    return X_train, X_test, y_train, y_test

def vectorizer(X_train, X_test):
    import joblib
    vectorizer = joblib.load("models/tfidf_vectorizer.joblib")
    X_train_feats = vectorizer.fit_transform(X_train)
    X_test_feats = vectorizer.transform(X_test)

    return X_train_feats, X_test_feats

def create_classifier(X_train_feats, y_train, X_test_feats):
    classifier = MLPClassifier(activation = "logistic",
                           hidden_layer_sizes = (20,),
                           max_iter=1000,
                           random_state = 42)
    
    classifier = classifier.fit(X_train_feats, y_train)
    y_pred = classifier.predict(X_test_feats)
    return classifier, y_pred

def classification_report(classifier, y_test, y_pred):
    classifier_metrics = metrics.classification_report(y_test, y_pred)
    from joblib import dump, load
    dump(classifier, "models/MLP_classifier.joblib")
    
    # save classification report
    f = open("out/Classification_Report_NeuNet.txt", "w")
    f.write(classifier_metrics)
    f.close()
    
    
def main():
    tracker = EmissionsTracker(project_name=f"a2_neunet_emissions", 
        experiment_id=f"a2_neunet_emissions",
        output_dir=os.path.join("out","emissions"),
        output_file=f"a2_neunet_emissions.csv")
    
    tracker.start()

    X_train, X_test, y_train, y_test = load_data()
    X_train_feats, X_test_feats = vectorizer(X_train, X_test)
    
    tracker.start_task("a2_train_neunet_classifier")
    classifier, y_pred = create_classifier(X_train_feats, y_train, X_test_feats)
    tracker.stop_task()

    classification_report(classifier, y_test, y_pred)

    tracker.stop()

if __name__=="__main__":
    main()