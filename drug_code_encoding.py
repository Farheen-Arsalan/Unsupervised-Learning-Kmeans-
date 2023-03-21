from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing


path ='/Users/Arsalan/Desktop/drug200.csv'
data = pd.read_csv(path)
print(data.shape)
origData = data.copy()
# label encoder 

le = preprocessing.LabelEncoder()

data['BP'] = le.fit_transform(data['BP'])

le = preprocessing.LabelEncoder()
data['Cholesterol'] = le.fit_transform(data['Cholesterol'])

le = preprocessing.LabelEncoder()
data['Na_to_K'] = le.fit_transform(data['Na_to_K'])


le = preprocessing.LabelEncoder()
data['Sex'] = le.fit_transform(data['Sex'])

le = preprocessing.LabelEncoder()
data['Drug'] = le.fit_transform(data['Drug'])


print(data)





