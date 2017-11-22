#import pandas as pd
import numpy as np
import math
from sklearn.cluster import DBSCAN
from sklearn.utils import shuffle
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix



#load csv file, need to put data.csv and DBSCAN.py in the same folder
data_with_label = np.loadtxt('sample.csv',delimiter=',',skiprows=1)
data_with_label = shuffle(data_with_label)
#print(data)

# store data 
data = data_with_label[:,:-1]

#store ground truth label 
#label = data_with_label[:,[26]]
label = []
for line in data_with_label:
    label.append(line[-1])
label = np.array(label)

#print(data)
#print(label)

# this function calculates the euclideanDist between two data 
def getEuclideanDist(data1, data2):
    array1 = np.array(data1)
    array2 = np.array(data2)
    array3 = pow((array2 - array1), 2)
    array_sum  = sum(array3)
    dist = math.sqrt(array_sum) 
    return dist

# this function computes the center of the cluster
def getCenter(cluster,training_data):
    center = [0] * len(training_data[0]-1)
    #print(center)
    #center = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
        #temp.append(data[index])
    for attribute in range (0,len(training_data[0]-1)):
        for index in cluster:
        #for item in temp:
            center[attribute]+=training_data[index][attribute]
        center[attribute]=center[attribute] / len(cluster)
    return center


# this function predicts the mood for a given test dataset
def predict (train_data,test_data,train_label):
    # Do DESCAN, can tune parameters
    db = DBSCAN(eps=0.5,min_samples = 3).fit(train_data)
    cluster_label = db.labels_
    n_clusters  = len(set(cluster_label)) - (1 if -1 in cluster_label else 0)

    #print(cluster_label)

    # this dictionary store each cluster and a list of all the data's indices in that cluster
    # key: cluster number
    # value: a list of data's indices
    index_dic = {}
    count = 0

    for i in range(0, n_clusters):
        index_dic[i] = []

    for j in cluster_label:
        if(j != -1):
            index_dic[j].append(count) 
            count += 1

        else:
            count += 1

    #print(index_dic)


    # this dictionary store each cluster and the mood associate with the cluster
    # key: cluster number
    # value: mood index
    label_dic = {}

    for j in index_dic.keys():
        temp = []
        for index in index_dic[j]:
            temp.append(train_label[index])
        #print (temp)
        temp2 = max(temp,key=temp.count)
        #print(temp2)
        label_dic[j] = temp2

    #print(label_dic)




    # this dictionary store each cluster and the cluster's center
    # key: cluster number
    # value: cluster's center
    center_dic = {}

    for j in index_dic.keys():
        temp = getCenter(index_dic[j],train_data)
        center_dic[j] = temp

    #print(center_dic)

    # prediction: for each test data, find it's nearest cluster and return the nearest cluster's mood label
    pred_label = []
    for data in test_data:
        distance = 10000000
        index = -1
        result = 10
        for key in center_dic.keys():
            temp_dist = getEuclideanDist(data,center_dic[key])
            #print(temp_dist)
            if(temp_dist<distance):
                distance = temp_dist
                #print(distance)
                index = key
                result = label_dic[index]
                #print(result)
        #print(result)
        pred_label.append(result)
    #print(pred_label)

    return pred_label




kf = KFold(n_splits=5)
n_fold = 0
dataLen = len(label)

for train_index, test_index in kf.split(range(dataLen)):
    #print(train_index)
    train_data = data[train_index]
    #print(train_data)
    train_label = label[train_index]
    #print(train_label)
    test_data = data[test_index]
    test_label = label[test_index]
    print(test_label)
    n_fold += 1
    
    #this gives a preidiction
    test_prediction = predict(train_data,test_data, train_label)
    train_prediction = predict(train_data, train_data, train_label)
    #print(prediction)
  
    # compute and evaluate accuracy: compare test data's ground truth mood label and assigned mood label
    print("Test Accuracy :: ", accuracy_score(test_label, test_prediction))
    print("Train Accuracy  :: ", accuracy_score(train_label, train_prediction))
    print("Confusion matrix \n", confusion_matrix(test_label, test_prediction))

    print('end!!!!')




