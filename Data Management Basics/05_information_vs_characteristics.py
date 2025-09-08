import pandas as pd
import matplotlib.pyplot as plt

# get data
data = pd.read_excel("DATA.xlsx")

# get minimum surface tension = information
info = data.groupby(by="source").min()

# show
print(info)

# %% get material information as metadata

# read
meta = pd.read_excel("Polysorbate.xlsx")

# rebuild "key"
meta["key"] = meta["Product"].str.replace(" ", "")

# show
print(meta)


# %% combine

# merge
merge = pd.merge(
            info,
            meta,
            left_on="key",
            right_on="key",
            how="outer"
            )


# %% plot

plt.scatter(
    x=merge["Molar Mass"],
    y=merge["surface_tension_mN_m"]    
    )

plt.ylim(40, 50)
plt.xlabel("Molar Mass [g/mol]")
plt.ylabel("Minimum Surface Tension [mN/m]")