# define filename
file = "raw_from_machine/Polysorbate40.csv"

# initialize results variable of type string (empty)
results = ""

# open the file for reading "r" with encoding utf-8
with open(file, "r", encoding="utf-8") as f:
    # read file line by line
    while True:
        # read line
        line = f.readline()
        # append to string
        results = results + line
        # end of file reached?
        if not line:
            print(type(line))
            # break infinite while loop
            break

# %% extract data via regex
#

# pattern as derived via "regex101.com"
pattern = "(.*),(\d+.*)"

# import python regex module
import re

# find pattern in string "results"
findings = re.findall(
                pattern,
                results
            )
# show "findings" variable (list of tuples)
print(findings)

# import pandas module to use the DataFrame with alias pd
import pandas as pd

# initialize empty pandas.DataFrame data
data = pd.DataFrame()

# initialize empty list of concentrations
concentration_g_l = []
# loop through findings to get concentrations
for _finding in findings:
    # info
    print(_finding)
    # get the first element of the "_finding" (string) and convert
    # to float
    _c_g_l = float(_finding[0])
    # append extracted concentration to list of concentrations
    concentration_g_l.append(_c_g_l)
    
# use concentration list as column in the defined DataFrame
data["concentration_g_l"] = concentration_g_l

# use surface tension as colums (via list comprehension)
# type conversion to float via "float()"-function
data["surface_tension_mN_m"] = [float(i[1]) for i in findings]

# print resulting DataFrame
print(data)

# clean variable space
del concentration_g_l, pattern, findings


