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


C3x = X[2]
C3y = Y[2]
# C3(C3x,C3y)

C4x = X[3]
C4y = Y[3]
# C4(C4x,C4y)


for it in range(30):
    # traverse the whole set of datapoints 
    Cluster1x=[]
    Cluster1y=[]
    Cluster2x=[]
    Cluster2y=[]
    Cluster3x=[]
    Cluster3y=[]
    Cluster4x=[]
    Cluster4y=[]
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
        #distance w.r.t C2
        d3 =  np.sqrt((X[i]-C3x)**2 + (Y[i]-C3y)**2)
        #distance w.r.t C2
        d4 =  np.sqrt((X[i]-C4x)**2 + (Y[i]-C4y)**2)
        
        # compare 
        if(d1<d2 and d1<d3 and d1<d4):
            Cluster1x.append(X[i])
            Cluster1y.append(Y[i])
            plt.plot(X[i],Y[i],'ro')
        elif(d2<d1 and d2<d3 and d2<d4 ):
              Cluster2x.append(X[i])
              Cluster2y.append(Y[i])
              plt.plot(X[i],Y[i],'md')
        elif(d3<d4 and d3<d1 and d3<d2):
             Cluster3x.append(X[i])
             Cluster3y.append(Y[i])
             plt.plot(X[i],Y[i],'c*')
        elif(d4<d1 and d4<d2 and d4<d3):
              Cluster4x.append(X[i])
              Cluster4y.append(Y[i])
              plt.plot(X[i],Y[i],'yd')
        
    #for i in range(X.shape[0]):
        #plt.text(X[i],Y[i],str(i+1))
    plt.plot(C1x,C1y,'ks')
    plt.plot(C2x,C2y,'ks')
    plt.plot(C3x,C3y,'ks')
    plt.plot(C4x,C4y,'ks')
    # lets find the new centroid 
    # by applying the averaging step 
    C1xavg = sum(Cluster1x)/(len(Cluster1x))
    C1yavg = sum(Cluster1y)/(len(Cluster1y))
    
    C2xavg = sum(Cluster2x)/(len(Cluster2x))
    C2yavg = sum(Cluster2y)/(len(Cluster2y))
    
    C3xavg = sum(Cluster3x)/(len(Cluster3x))
    C3yavg = sum(Cluster3y)/(len(Cluster3y))
    
    C4xavg = sum(Cluster4x)/(len(Cluster4x))
    C4yavg = sum(Cluster4y)/(len(Cluster4y))
    
    # updated Centroids are 
    C1x = C1xavg
    C1y = C1yavg
    
    C2x = C2xavg
    C2y = C2yavg
    
    C3x = C3xavg
    C3y = C3yavg
    
    C4x = C4xavg
    C4y = C4yavg
    plt.pause(0.1)
    
    


        
    






