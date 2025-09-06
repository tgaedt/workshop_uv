import pandas as pd

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url = "https://tinyurl.com/icccm1"
df: pd.DataFrame = pd.read_excel(url) 

df.columns = ["cement", "bfs", "flyash", "water", "sp", "agg_coarse", "agg_fine", "age", "strength"]

#%%

# explain the datatypes and the different modes of accessing the columns

type(df.cement)
print(df.cement)
print(df["cement"])

col1 = df.cement
col2 = df["cement"]
col3 = df.iloc[:,0]
col4 = df.loc[:,"cement"]

print(col1 == col2)
print(col1 == col3)


#%%

# create a new column
df["wc"] = df["water"] / (df["cement"] +df["bfs"] + df["flyash"])

df["wc_high"] = df["wc"] > 0.42

# check dtypes
print(df.dtypes)

#%%

# count high wc instances
nr_high = df.wc_high.sum()

# calculate the means
means = df.mean(numeric_only=True)



#%% 

# filter operations
df_high = df.query("wc_high < 0.42").copy()
df_high2 = df[df["wc_high"]]



#%%

# joining and dataframe creation
exp_names = ["a" + str(i) for i in df.index.values]
df["exp_code"] = exp_names


additional_data = [i**2 for i,j in enumerate(exp_names)]
df2 = pd.DataFrame({"exp_code":exp_names, "new": additional_data})
df3 = pd.DataFrame({"exp":exp_names, "new": additional_data})

# join by index
df_joined = df.join(df2, lsuffix="left")  ## CHECK
df_joined2 = pd.merge(df, df3, left_on="exp_code", right_on="exp")



#%%

# exploratory data analysis

fig, ax = plt.subplots()
ax.scatter(df["age"], df["strength"])
ax.set_xlabel("Age / days")
ax.set_ylabel("Strength / MPa")
plt.show()

#%%

# groupby


# wc contains too many unique values
print(len(df.wc.unique()))

# create bins for w/c values

bins = [0, 0.34, 0.38, 0.42, 0.46, 0.50, 1]
labels = ["0.0-0.34", "0.34-0.38", "0.38-0.42", "0.42-0.46", "0.46-0.50", "0.50-1.0"]

df["wc_bin"] = pd.cut(df["wc"], bins=bins, labels = labels)

#%%

# loop over bins
for name, group in df.groupby(["wc_bin"]):
    fig, ax = plt.subplots()
    ax.scatter(group["age"], group["strength"])
    ax.set_title(name)
    plt.show()
    
#%% 

# demonstrate subplots
fig, axs = plt.subplots(2,3, layout="tight")

for (name, group), ax in zip(df.groupby("wc_bin"), axs.flatten()):
    ax.scatter(group["age"], group["strength"], s=4)
    ax.set_title(name)
    ax.set_ylim(0,90)
plt.show()


#%%

fig, ax = plt.subplots()

for name, group in df.query("age < 60 and age > 1").groupby("age"):
    ax.scatter(group["wc"], group["strength"], alpha =0.2, label=name)
plt.legend()
plt.show()


#%%

from scipy.optimize import curve_fit

# fit an exponential relation to the age groups of 

def exponential(x, a,b,c):
    return c + a * np.exp(-b*x)

def fit_exponential(df, xcol="wc", ycol="strength"):
    f = exponential
    popt, pcov = curve_fit(f, df[xcol], df[ycol])
    out = {"a": popt[0], "b": popt[1], "c": popt[2]}
    return pd.Series(out)
    
fits = df.query("age < 60 and age >1 ").groupby("age").apply(lambda t: fit_exponential(t))

x = np.linspace(0.22, df.wc.max(),100)

fig, ax = plt.subplots()
for index, row in fits.iterrows():
    y = row["c"] + row["a"] * np.exp(-row["b"]*x)
    ax.plot(x,y)
for name, group in df.query("age < 60 and age > 1").groupby("age"):
    ax.scatter(group["wc"], group["strength"], s=8, alpha =0.2, label=name)

plt.legend()
plt.plot()


#%%

# print and save equations
df_html = fits.to_html()

with open("fits.html", "w") as f:
    f.write(df_html)
