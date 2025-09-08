import pandas as pd
from pathlib import Path


# define filename
file = "raw_from_machine/Polysorbate40.csv"

# read
results = pd.Series([Path(file).read_text(encoding="utf-8")])

# pattern as derived via "regex101.com"
pattern = r"(?P<concentration_g_l>.*),(?P<surface_tension_mN_m>\d+.*)"

# extract
data = results.str.extractall(pattern).reset_index(drop=True).astype(float)

# info
print(data)