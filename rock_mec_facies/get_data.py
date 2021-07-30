import pandas as pd
import numpy as np
import lasio
import glob
import os

def get_df():
    """[This functions get all csv files from a specific folder and concatenate into a single Dataframe]

    Returns:
       [Dataframe]: [All CSV file concatenated into an unique dataframe]
    """
    path = input("Insert file folder:\n->")
    header_line = input("Insert how many header lines the file have:\n->")
    files = os.listdir(path)
    file_list = []
    for file in files:
        if file.lower().endswith(".txt"):
            file_list.append(file)
    file_list
    print(file_list)

    alldfs=[]
    df_list=[]
    for file in file_list:
        df = pd.read_csv(f'{path}/{file}',sep="\t",header=int(header_line))
        df_list.append(df)

    alldfs = pd.concat(df_list)
    return alldfs

def las2df(las_folder):
    """[summary]

    Args:
        las_folder ([str]): [caminho completo da pasta com arquivos las]

    Returns:
        [type]: [description]
    """
    list_las_file = [f for f in glob.glob(las_folder + "*\*.las")]
    n = 1
    dfs=[]
    wellname_list = []
    for file in list_las_file:
        las = lasio.read(file)
        wellname = las.well.WELL.value
        wellname_list.append(wellname)
        globals()[f"df_{n}"] = las.df().rename_axis("MD").reset_index()
        dfs.append(f"df_{n}")
        globals()[f"df_{n}"]["WELL"]=f"Well_{n}"
        n+=1
    globals()["df_list"] = dfs
    globals()["well_list"] = wellname_list
    return globals()["df_list"],globals()["well_list"]

def export_csv(df_list):
    os.mkdir("./Exported_Logs")
    n=1
    for df in df_list:
        filename = df
        new_name = f"Well_{n}"
        globals()[f"{filename}"].to_csv(f"./Exported_Logs/{new_name}.txt", sep="\t",header="True",index=None)
        n+=1