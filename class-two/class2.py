# -*- coding: utf-8 -*-
# import numpy as np
import pandas as pd
import matplotlib as plt
import os

os.chdir("C:/Users/nsteinm/Documents/python/py-class/class-two")
df1 = pd.read_hdf("hw2_main_part1_limited.h5")
df2 = pd.read_hdf("hw2_main_part2_limited.h5")

df = pd.concat([df1,df2]).drop_duplicates()
df.columns = df.columns.str.strip().str.lower().str.replace(" ","_")
