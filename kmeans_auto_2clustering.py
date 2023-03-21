# random data generation 
import numpy as np
import matplotlib.pyplot as plt

samples = 1000
X = np.random.randint(10,100,size=(samples)) # (low, high, size = )
Y = np.random.randint(10,100,size=(samples))
print(X.shape,Y.shape)



plt.figure(1)
plt.plot(X,Y,'go')
for i in range(X.shape[0]):
    plt.text(X[i],Y[i],str(i+1))
# make use of the markes 
plt.grid('on')

# find the centroid for the data itself 
# dp0  - > centroid 1
C1x = X[0]
C1y = Y[0]
# C1(C1x,C1y)
# dp1 -> centroid 2
C2x = X[1]
C2y = Y[1]
# C2(C2x,C2y)

for it in range(30):
    # traverse the whole set of datapoints 
    Cluster1x=[]
    Cluster1y=[]
    Cluster2x=[]
    Cluster2y=[]
    plt.figure(2)
    plt.subplot(2,1,1)
    plt.plot(X,Y,'go')
   # for i in range(X.shape[0]):
    #    plt.text(X[i],Y[i],str(i+1))
    plt.subplot(2,1,2)
    for i in range(X.shape[0]):
        # distance w.r.t C1
        d1 = np.sqrt((X[i]-C1x)**2 + (Y[i]-C1y)**2)
        #distance w.r.t C2
        d2 =  np.sqrt((X[i]-C2x)**2 + (Y[i]-C2y)**2)
        
        # compare 
        if(d1<d2):
            Cluster1x.append(X[i])
            Cluster1y.append(Y[i])
            plt.plot(X[i],Y[i],'ro')
        elif(d1>=d2):
            Cluster2x.append(X[i])
            Cluster2y.append(Y[i])
            plt.plot(X[i],Y[i],'md')
    #for i in range(X.shape[0]):
        #plt.text(X[i],Y[i],str(i+1))
    plt.plot(C1x,C1y,'ks')
    plt.plot(C2x,C2y,'ks')
    # lets find the new centroid 
    # by applying the averaging step 
    C1xavg = sum(Cluster1x)/(len(Cluster1x))
    C1yavg = sum(Cluster1y)/(len(Cluster1y))
    
    C2xavg = sum(Cluster2x)/(len(Cluster2x))
    C2yavg = sum(Cluster2y)/(len(Cluster2y))
    
    # updated Centroids are 
    C1x = C1xavg
    C1y = C1yavg
    
    C2x = C2xavg
    C2y = C2yavg
    plt.pause(0.3)
    
    


        
    






