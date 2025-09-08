import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

# import module defined before
from surface_tension_tools import parsers

# define root directory
root = Path("raw_from_machine")

# init list
data_all = []

# loop files
for file in root.iterdir():
    
    # skip "bad" file
    if "MESSED" in str(file):
        continue
    
    # show
    print(file)
    
    # read
    data = parsers.get_surface_tension_data(file)
    
    # add source info
    data["source"] = str(file)
    data["key"] = file.stem
    
    # append to "all data" list
    data_all.append(data)
    
    # info
    print(data)
    
    # plot
    plt.plot(
        data["concentration_g_l"],
        data["surface_tension_mN_m"],
        label=file.stem,
        marker="."
        )
    
# show legend
plt.legend()
# log scale
plt.xscale("log")
# labels
plt.ylabel("surface_tension_mN_m")
plt.xlabel("concentration_g_l")


# build over df and save
data_all = pd.concat(data_all)

# save
data_all.to_excel("DATA.xlsx", index=False)