# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import locale
locale.setlocale(locale.LC_TIME, "ko_KR.UTF-8")

from datetime import datetime

# %%
G_dax = pd.read_csv("DAX 내역.csv", encoding = "utf-8")
G_dax.head()

# %%
def to_date_inv(df):
    df["날짜"] = pd.to_datetime(df["날짜"], format = "%Y년 %m월 %d일")
    df = df.sort_values(by = "날짜", ascending=True)
    df.set_index("날짜", inplace=True)

    return df

def to_numeric_inv(df):
    a = []
    for d in df["종가"]:
        a.append(d.replace(",",""))
    df["종가"] = a
    df["종가"] = pd.to_numeric(df["종가"])

    return df

# %%
G_dax = to_date_inv(G_dax)
G_dax = to_numeric_inv(G_dax)

#%%
dj_metal = pd.read_csv("Dow Jones Commodity All Metals Capped Component 내역.csv", encoding="utf-8")
dj_metal.head()

#%%
dj_metal = to_date_inv(dj_metal)
#dj_metal = to_numeric_inv(dj_metal), dowJones Metal is originally numeric

# %%
plt.figure(figsize=(15,10))
plt.plot(G_dax["종가"], "-", label = "DAX")
plt.legend("DAX 12 years")

#%%
plt.figure(figsize=(15,10))
plt.plot(dj_metal["종가"], "-r", label = "DJM")
plt.legend("DAX 12 years")

# %%
cop_fu = pd.read_csv("구리 선물 내역.csv", encoding="utf-8")
cop_fu = to_date_inv(cop_fu)
cop_fu = to_numeric_inv(cop_fu)
# %%
plt.figure(figsize=(15,10))
plt.plot(cop_fu["종가"], "-r", label = "DJM")
plt.legend("DAX 12 years")

# %%
car_fu = pd.read_csv("탄소배출권 선물 내역.csv", encoding = "utf-8")
car_fu = to_date_inv(car_fu)
#car_fu = to_numeric_inv(car_fu)

plt.figure(figsize=(15,10))
plt.plot(car_fu["종가"], "-r", label = "DJM")
plt.legend("DAX 12 years")

# %%
close_data = pd.concat([G_dax["종가"], cop_fu["종가"], car_fu["종가"]], axis=1)
close_data.columns = ["dax", "coper", "carbon"] 
close_data
# %%
close_data = close_data.dropna()
# %%
close_data.corr()
# %%
