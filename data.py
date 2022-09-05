####before you import make sure u have the modules installed####
import pandas as pd
import datetime as dt
import uuid 
import numpy as np
#import all modules required to start assigment

#1. loading in one of the messiest datasets i've seen in mankind
df = pd.read_csv('Data\School_Learning_Modalities.csv')
#realtive path can be used if directory is sepcified---- 
#if not use the whole path way with FOWARD SLASHES
df #showcases the data

countRows, countColumns = df.shape #2. gets the count of rows and columns 
df.shape #2. this now shows the number of rows and columns
list(df) #3. this shows the columns name

#4/5/6. column names cleaned to to look more coding friendly by removing special charaters and whitespaces from ALL COLUMNS
df.columns = df.columns.str.replace('[^A-Za-z0-9]+', '_') 
list(df) 

#7. converts column types to the correct types
df.dtypes #shows the categories of data types for each column 
df['Week'] = pd.to_datetime(df['Week']) #changed from object to date since where looking at dates
df.Student_Count = df.Student_Count.astype(int) #changed from float to int32 cause you cant have decmial points if your talking about whole individuals


#8 looking for duplicate rows and removing those rows
bool_series = df.duplicated(keep=False) #keep flase makes will consider all the instence of a row to be duplicated
print('Boolean series:')
print(bool_series)
print('\n')
print('DataFrame after removing all the instances of the duplicate rows:')
df[~bool_series] #the ~ sign is used for negation changing the boolean value from false to true

#9. assess missing values per columns
df.isnull().sum()
df.replace(to_replace='', value=np.nan, inplace=True)
df.replace(to_replace=' ', value=np.nan, inplace=True)
# replaces empty cells with Nan 
df.dropna(inplace=True) 
#now cells are replaced with nan we discard them with this line of command to deal with the missing values in the 'student_count' column

#10.New datafield: true/false
list(df)
df['modality_inperson'] = np.where(df['Learning_Modality']!= 'in-person', True, False)
df['modality_inperson']
#this command allows for the addition of a new column nammed 'modality_inperson'
#which and allows us to pick 'learning_modality' as our dataset for the if statement 
