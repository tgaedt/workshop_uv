import pandas as pd


def get_surface_tension_data(file):
    
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
    
    # retunr
    return data