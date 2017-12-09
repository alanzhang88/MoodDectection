import pandas as pd
import numpy as np
from sklearn.utils import shuffle
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import roc_auc_score
import sys


INPUT_PATH = "./data.csv"

dataset = pd.read_csv(INPUT_PATH)

dataset = shuffle(dataset)

droplist = ["label"]
if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        print("Dropping feature ",arg)
        droplist.append(arg)

y = dataset["label"].values
x = dataset.drop(droplist,axis=1).values

kf = KFold(n_splits=5)
n_fold = 0
dataLen = y.shape[0]

for train_keys, test_keys in kf.split(range(dataLen)):
    train_x = np.take(x,train_keys,axis=0)
    train_y = np.take(y,train_keys)
    test_x = np.take(x,test_keys,axis=0)
    test_y = np.take(y,test_keys)
    n_fold += 1
    #paramters can be tweaked
    clf = RandomForestClassifier(n_estimators=10, criterion="gini")
    clf.fit(train_x,train_y)
    #this gives a preidiction
    prediction = clf.predict(test_x)
    train_prediction = clf.predict(train_x)
    #this gives probability for each labels
    prediction_proba = clf.predict_proba(test_x)
    
    print("Train Accuracy :: ", accuracy_score(train_y, train_prediction))
    print("Test Accuracy  :: ", accuracy_score(test_y, prediction))
    print("Train Precision :: ", precision_score(train_y, train_prediction))
    print("Test Precision  :: ", precision_score(test_y, prediction))
    print("Train Recall :: ", recall_score(train_y, train_prediction))
    print("Test Recall  :: ", recall_score(test_y, prediction))
    print("Train ROC area under curve :: ", roc_auc_score(train_y, train_prediction))
    print("Test ROC area under curve  :: ", roc_auc_score(test_y, prediction))
    print("Confusion matrix \n", confusion_matrix(test_y, prediction))
