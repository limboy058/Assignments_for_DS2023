import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_diabetes

dt=load_diabetes()
print(dt.keys())
print(dt['feature_names'])

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(dt['data'],dt['target'],random_state=0)
lr=LinearRegression()
lr.fit(X_train,y_train)
LinearRegression(copy_X=True,fit_intercept=True,n_jobs=None)

print(lr.coef_)

print(lr.score(X_train,y_train))

print(lr.score(X_test,y_test))
