from numpy import random
import matplotlib.pyplot as plt

dt=random.normal(loc=0,scale=1,size=(1000))
plt.figure(figsize=(10, 10), dpi=100)

plt.hist(x=dt,bins=20,edgecolor='white')
plt.show()