# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 18:04:42 2023

@author: shuyu
"""
import os
import pandas as pd

folder = r"C:\Users\Shadow\OneDrive - Imperial College London\4th Year\MSci Project\ROI"
os.chdir(folder)
path = folder + "\measurements5.tsv"
df=pd.read_csv(path,sep='\t')
df2538 = df.loc[df["Image"]=="2538.czi"]
df2538.to_csv('2538.tsv', sep="\t")

df2533 = df.loc[df["Image"] == "2533.czi"]
df2533.to_csv('2533.tsv',sep = "\t")

df2487 = df.loc[df["Image"] == "2487.czi"]
df2487.to_csv('2487.tsv',sep = "\t")

df2439 = df.loc[df["Image"] == "2439.czi"]
df2439.to_csv('2439.tsv',sep = "\t")

df2390 = df.loc[df["Image"] == "2390.czi"]
df2390.to_csv('2390.tsv',sep = "\t")

#%%
dir_list = os.listdir(folder)