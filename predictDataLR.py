import pandas as pd
from sklearn import linear_model
from sklearn.svm import SVR
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import numpy as np

df = pd.read_excel("dataStandard.xlsx")

df_test = df.iloc[:200,:]
df_train = df.iloc[201:,:]

X = df_train[['Price Points','Space Points','Placement Points','Min Price','Max Price']]
y = df_train[['Quality Points']]


regr = linear_model.LinearRegression().fit(X, y);

regr.predict(df_test[['Price Points','Space Points','Placement Points','Min Price','Max Price']])

scoreCalLR = regr.score(df_test[['Price Points','Space Points','Placement Points','Min Price','Max Price']],df_test[["Quality Points"]])

print(scoreCalLR)

