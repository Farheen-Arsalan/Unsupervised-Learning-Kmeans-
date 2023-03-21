from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


path ='/Users/Arsalan/Desktop/Mall_Customers.csv'
data = pd.read_csv(path)
print(data.shape)

X = data.loc[:, ['Annual Income (k$)','Spending Score (1-100)']]
print(X.shape)

# convert the dataframe into numpy array 
X = X.values


inertia=[]
cluster=[]
# create the Kmeans model 
for i in range(2,13,1):
    kmModel = KMeans(n_clusters=i)
    kmModel=kmModel.fit(X)
    inertia.append(kmModel.inertia_)
    cluster.append(i)

plt.figure(1)
plt.plot(cluster,inertia)

# from the graph 5 is the elbow point 
# finalise 5 number of cluster
kmModel = KMeans(n_clusters=5)
kmModel=kmModel.fit(X)
labels = kmModel.labels_

# visualise the data 
plt.figure(101)
plt.subplot(2,1,1)
plt.scatter(X[:,0],X[:,1])
plt.subplot(2,1,2)
plt.scatter(X[:,0],X[:,1],c=labels)

# save the catergories
data['Label'] = labels
print(data.shape)

# lets save it in csv file 
path1 ='/Users/Arsalan/Desktop/Mall_Customers1.csv'

data.to_csv(path1)






