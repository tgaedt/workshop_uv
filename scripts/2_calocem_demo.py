#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%%

import calocem.tacalorimetry as ta 
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

calodatapath = Path(__file__).parent.parent / "data" / "calo"
metadatapath = Path(__file__).parent.parent / "data" / "metadata_calo"

processparams = ta.ProcessingParameters()

tam = ta.Measurement(calodatapath, auto_clean=False, cold_start=True, processparams=processparams, new_code=True, processed=True)
tam.add_metadata_source(metadatapath / "metadata.csv", sample_id_column="sample")

df = tam.get_data()
metadata = pd.read_csv(metadatapath / "metadata.csv")

df = pd.merge(df, metadata, left_on="sample_short", right_on="sample")

#%%
# Plotting

for additive, additive_data in df.groupby(["additive_name"]):
    fig, ax = plt.subplots()
    for dosage, dosage_data in additive_data.groupby("dosage_additive_micromol_g_cem"):
        ax.plot(dosage_data["time_s"], dosage_data["normalized_heat_flow_w_g"], label=dosage)
    ax.set_title(f"Additive: {additive}")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Normalized Heat Flow (W/g)")
    ax.legend()
    plt.show()

#%%

# the need to include or inject the reference into additive data

def create_reference_data(df, sample_code, retarders):
    data = df.copy()
    data.loc[data["additive_name"] == sample_code, "additive_name"] = data.loc[
        data["additive_name"] == sample_code, "additive_name"
    ].apply(lambda x: retarders)
    data = data.explode("additive_name")
    return data

retarders = ["sucrose", "glucose"]
df_ref = create_reference_data(df, "reference", retarders)
df_ref = df_ref.explode("additive_name")

#%%
# Plotting

for additive, additive_data in df_ref.groupby(["additive_name"]):
    fig, ax = plt.subplots()
    for dosage, dosage_data in additive_data.groupby("dosage_additive_micromol_g_cem"):
        ax.plot(dosage_data["time_s"], dosage_data["normalized_heat_flow_w_g"], label=dosage)
    ax.set_title(f"Additive: {additive}")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Normalized Heat Flow (W/g)")
    ax.legend()
    plt.show()
#%%

# demonstration with polars

import polars as pl

df_pl = pl.from_pandas(df)

df_pl_ref = (
    df_pl.with_columns(
        pl.when(pl.col("additive_name") == "reference")
        .then(pl.lit(["sucrose", "glucose"]))
        .otherwise(pl.col("additive_name").map_elements(lambda x: [x]))
        .alias("additive_name_new")
    ).explode("additive_name_new")
)

#df_pl_ref
#%%

import altair as alt
alt.data_transformers.enable("vegafusion")
alt.renderers.enable("png")

chart = (
    df_pl_ref.plot.line(
        x="time_s",
        y="normalized_heat_flow_w_g",
        strokeDash="additive_name_new",
        color="dosage_additive_micromol_g_cem",
    )
)
chart.encoding.x.title= "Time / s"
chart.encoding.y.title = r"Normalized Heat Flow / W$g^{-1}$"

chart.show()
# %%

# Altair braucht die Unicode Zeichen
# https://en.wikipedia.org/wiki/Unicode_subscripts_and_superscripts

chart = (
    df_pl_ref.plot.line(
        x=alt.X("time_s", axis=alt.Axis(title="Time / s")),
        y=alt.Y("normalized_heat_flow_w_g", axis=alt.Axis(title=r"Normalized Heat Flow / Wg⁻¹")),
        #strokeDash="additive_name_new",
        color="dosage_additive_micromol_g_cem",
    ).facet(row="additive_name_new")
)

chart.show()