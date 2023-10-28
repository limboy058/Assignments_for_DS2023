import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


noise=np.random.normal(loc=0,scale=10,size=(30))

dt=[]
for i in range(0,30):
    dt.append([i,9*i+8+noise[i]])
    
dtx=[]
dty=[]
for it in dt:
    dtx.append(it[0])
    dty.append(it[1])

X_train=np.array(dtx).reshape((len(dtx),1))
Y_train=np.array(dty).reshape((len(dty),1))

lr=LinearRegression()
lr.fit(X_train,Y_train)
k=lr.coef_[0][0]
b=lr.intercept_[0]




plt.plot(dtx,dty)
plt.plot(X_train,lr.predict(X_train))
plt.annotate('k=%f,b=%f'%(k,b), xy=(2,5), xytext=(2, 10))
            
plt.show()