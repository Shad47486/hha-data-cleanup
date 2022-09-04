####before you import make sure u have the modules installed####
import pandas as pd
import datetime as dt
import uuid 
import numpy as np
#import all modules required to start assigment

#loading in one of the messiest datasets i've seen in mankind
df = pd.read_csv('Data\School_Learning_Modalities.csv')
#realtive path can be used if directory is sepcified---- 
#if not use the whole path way with FOWARD SLASHES
df #showcases the data

countRows, countColumns = df.shape #gets the count of rows and columns 
df.shape #this now shows the number of rows and columns

list(df) #this shows the columns name

df.columns = df.columns.str.replace('[^A-Za-z0-9]+', '_') 
list(df) #column names are revamped to look more coding friendly


