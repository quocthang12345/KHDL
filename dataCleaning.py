import pandas as pd
import numpy as np

df = pd.read_excel(r'foody-store-2.xlsx')

df.loc[df['Average Price'] == 'Đang cập nhật','Average Price'] = np.nan

df[['Min Price','Max Price']] = df['Average Price'].str.split('-',expand=True)

del df["Unnamed: 0"], df["Addresses"], df["Average Price"]


for i in range(len(df)):
  if df.at[i,'Types'].find("Nhà hàng") != -1:
    df.at[i,'Types'] = "Nhà hàng"
  if df.at[i,'Types'].find("Ăn chay") != -1:
    df.at[i,'Types'] = "Ăn chay"
  if df.at[i,'Types'].find("Tiệm bánh") != -1:
    df.at[i,'Types'] = "Tiệm bánh"
  if df.at[i,'Types'].find("Quán ăn") != -1:
    df.at[i,'Types'] = "Quán ăn"
  if df.at[i,'Types'].find("Café") != -1:
    df.at[i,'Types'] = "Coffee"
  if df.at[i,'Types'].find("Buffet") != -1:
    df.at[i,'Types'] = "Buffet"
  if df.at[i,'Types'].find("Ăn vặt") != -1:
    df.at[i,'Types'] = "Ăn vặt"
  if df.at[i,'Types'].find("Shop") != -1:
    df.at[i,'Types'] = "Shop Online"
  if df.at[i,'Types'].find("Quán an") != -1:
    df.at[i,'Types'] = "Quán ăn"
  if df.at[i,'Types'].find("Quán nhậu") != -1:
    df.at[i,'Types'] = "Quán nhậu"
  if df.at[i,'Types'].find("Khách sạn") != -1:
    df.at[i,'Types'] = "Nhà hàng"
  if df.at[i,'Types'].find("Bar") != -1:
    df.at[i,'Types'] = "Bar"

for i in range(len(df)):
  if type(df.at[i,'Min Price']) == str:
    df.at[i,'Min Price'] = df.at[i,'Min Price'][:-2]

for i in range(len(df)):
  if type(df.at[i,'Max Price']) == str:
    df.at[i,'Max Price'] = df.at[i,'Max Price'][:-1]

for i in range(len(df)):
  if type(df.at[i,'Min Price']) == str:
    df.at[i,'Min Price'] = df.at[i,'Min Price'].replace(".",'')

for i in range(len(df)):
  if type(df.at[i,'Max Price']) == str:
    df.at[i,'Max Price'] = df.at[i,'Max Price'].replace(".",'')



df.isnull().mean()
median= df["Min Price"].median()
df['Min Price'] = df['Min Price'].fillna(median)

median= df["Max Price"].median()
df['Max Price'] = df['Max Price'].fillna(median)

x = df["Types"].unique()
checkNull = df[df["Max Price"].isnull()]

df.to_excel(r'dataFoodyClean.xlsx', sheet_name='Your sheet name', index = False)