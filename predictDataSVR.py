import pandas as pd
from sklearn import linear_model
from sklearn.svm import SVR
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
import numpy as np

df = pd.read_excel("dataStandard.xlsx")

df_test = df.iloc[:200,:]
df_train = df.iloc[201:,:]

X = df_train[['Price Points','Space Points','Placement Points','Min Price','Max Price']]
y = df_train[['Quality Points']]

regr = make_pipeline(StandardScaler(), SVR(C=1.0, epsilon=0.2)).fit(X, y)

regr.predict(df_test[['Price Points','Space Points','Placement Points','Min Price','Max Price']])

scoreCalSVR = regr.score(df_test[['Price Points','Space Points','Placement Points','Min Price','Max Price']],df_test[["Quality Points"]])

print(scoreCalSVR)