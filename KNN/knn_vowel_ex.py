import numpy as np
import matplotlib.pyplot as plt
import pandas
#from sklearn.datasets import make_classifiaction
#from sklearn.dtatsets import make_blobs

ds=pandas.read_csv('C:/Users/Akankshya/Desktop/pattern recog/pyt/vowe.csv')

datay=ds['ans']

datax=ds[['a','b','c']]

def knn(prop,kn):
    ###different classes division#####

    prop_amt=prop
    l1.append(prop)
    print 'train:test '+str(prop_amt)+':'+str(1-prop_amt)


    values=np.unique(datay)
    #print y
    c=len(values)

    s=[]
    for value in values:
       # print value
        x= np.count_nonzero(datay==value)
        inds=np.nonzero(datay==value)[0]
        #print inds
        np.random.shuffle(inds)
        p=int(prop_amt*x)
        for i in range(0, p,1):
            s.append(inds[i])
           # print s
    #print len(np.array(s))


    ########Train_test#######
    Y_train=datay.loc[ds.index.isin(s)]
    X_train=datax.loc[ds.index.isin(s)]
    #print X_train
    #print Y_train


    X_test=datax.loc[~ds.index.isin(X_train.index)]
    Y_test=datay.loc[~ds.index.isin(Y_train.index)]
    #print X_test
    #print Y_test
    train_x=np.array(X_train)
    train_y=np.array(Y_train)
    x=np.array(X_test,dtype=float)
    y=np.array(Y_test)

    #print y
    #print X_train
    #print X_test
    #print x
    #print np.transpose(x)
    mean1= np.unique(np.array([y])).reshape(c,1)

    #################distance from each#######
    import math
    def eDistance(instance1, instance2, length):
        distance = 0
        for x in range(length):
            distance += pow((instance1[x] - instance2[x]), 2)
        return math.sqrt(distance)

    ########getting neighbor########   
    import operator 
    def getNeighbors(trainingSet, testInstance, k):
        distances = []
        length = len(testInstance)
        #print length
        for x in range(len(trainingSet)):
            #print trainingSet[x]
            dist = eDistance(testInstance, trainingSet[x], length)
            distances.append((train_y[x], dist))
        distances.sort(key=operator.itemgetter(1))
        neighbors = []
        for x in range(k):
            #print distances[x][0]
            ind=np.nonzero(distances[x][0]==values)[0]
            #print ind
            #t=datay.loc[ds.index.isin(ind)]
            #print t
            neighbors.append(ind)
        return neighbors


    ##########main############
    l=[]
    k=kn
    print 'k='+str(k)
    for  i in range(len(x)):
        #print np.array(X_train)[0]
        nb=getNeighbors(train_x,x[i],k)
        #print nb
        #print len(nb)
        #print nb[1][-1]
        
        q=[0]*c
        max=0
        for u in range(len(nb)):
            #print 'u'
            for w in range(c):
                #print w
                #print nb[u]
                if nb[u]==w:
                    #print nb[u]
                    q[w]+=1
                    if(q[w]>max):
                        max=q[w]
                        #print max
                        n=w
        #print mean1[n]               
        l.append(mean1[n])           
        
    r=np.array(l)

    #######printing fitted values####    
    #print  r

    #####printing actual value###
    #print y


    #####getting accuracy#####
    j=0
    temp=0
    for i in range(0,len(x),1):
        if r[j]==y[i]:
            j=j+1
        else :
            j=j+1
            temp=temp+1
    acc=(len(x)-temp)*100/len(x)
    l2.append(acc)
    print 'Accuracy= ' + str(acc)


    ######plotting#####
    #x1,y1=make_classificiation(n_features=2,n_redundant=0,n_informative=2,n_clustres_per_class=1)
    #plt.scatter(X_train[:,0],X_train[:,1],c=Y_train)
    #plt.show()

####tablemaking#####
l1=[]
l2=[]
from pandas import DataFrame
p1=0.4
o=0.1
kn=10
for h in range(0,5,1):
    prop=p1
    p1=p1+o
    knn(prop,kn)
    
df=DataFrame({'prop':l1,'accuracy':l2})
df.to_excel('knn_vowel_table.xlsx',sheet_name='sheet1',index=False)             

   
