import pandas as pd

# define filename
file = "raw_from_machine/Polysorbate40.csv"  #  - MESSED WITH

# get data
data = pd.read_csv(
            file,
            header=7,  # get column names from line number 8
            skipfooter=3,  # discard bottom 3 lines
            names=[
                "concentration_g_l",
                "surface_tension_mN_m"
                ],
            engine="python"
            )
# print data
print("Collected DATA:")
print(data)

# get "metadata" (information level)
metadata = pd.read_csv(
            file,
            skiprows=1,  # skip to line
            nrows=5,  # number of lines holding metadata
            sep=": ",  # column separator between parmeter name and 
                       # value
            header=None,  # do not read column names from file
            names=["parameter", "value"],  # specify column names 
                                           # explicitly
            engine="python"
            )
# print information (metadata)
print("Collected INFORMATION:")
print(metadata)



# %% plot

import matplotlib.pyplot as plt

data.plot(
    x="concentration_g_l", 
    y="surface_tension_mN_m", 
    color="#341256", 
    marker=".", 
    linestyle="--"
    )

plt.xscale("log")

