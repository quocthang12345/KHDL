import pandas as pd;
import scipy.stats as stat
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler


data = pd.read_excel('./dataFoodyClean.xlsx')

data['Min Price'] = data['Min Price'].astype('float64')
data['Max Price'] = data['Max Price'].astype('float64')

min_max=MinMaxScaler()
df_minmax=pd.DataFrame(min_max.fit_transform(data.iloc[:,[6,7]]),columns=data.iloc[:,[6,7]].columns)

for i in range(len(data)):
    data.at[i,'Min Price'] = df_minmax.at[i,'Min Price']   # chuan hoa du lieu bang can bac 2 de lay gia tri duy nhat

for i in range(len(data)):
    data.at[i,'Max Price'] = df_minmax.at[i,'Max Price']


for i in range(len(data)):
    if data.at[i,'Types'] == "Nhà hàng":
            data.at[i,'Types'] = 1
    if data.at[i,'Types'] == "Ăn chay":
            data.at[i,'Types'] = 2
    if data.at[i,'Types'] == "Tiệm bánh":
            data.at[i,'Types'] = 3
    if data.at[i,'Types'] == "Quán ăn":
            data.at[i,'Types'] = 4
    if data.at[i,'Types'] == "Coffee":
            data.at[i,'Types'] = 5
    if data.at[i,'Types'] == "Buffet":
            data.at[i,'Types'] = 6
    if data.at[i,'Types'] == "Ăn vặt":
            data.at[i,'Types'] = 7
    if data.at[i,'Types'] == "Shop Online":
            data.at[i,'Types'] = 8
    if data.at[i,'Types'] == "Quán ăn":
            data.at[i,'Types'] = 9
    if data.at[i,'Types'] == "Quán nhậu":
            data.at[i,'Types'] = 10
    if data.at[i,'Types'] == "Khách sạn":
            data.at[i,'Types'] = 1
    if data.at[i,'Types'] == "Bar":
            data.at[i,'Types'] = 12

for i in range(len(data)):
    data.at[i,'Stores'] = i


def plot_data(df,feature):
    plt.figure(figsize=(10,6))
    plt.subplot(1,2,1)
    df[feature].hist() # histogram
    plt.subplot(1,2,2)
    stat.probplot(df[feature],dist='norm',plot=plt)# prob plot
    plt.show()


plot_data(data,'Price Points')

data.to_excel('dataStandard.xlsx', sheet_name='Standard Data', index = False)

