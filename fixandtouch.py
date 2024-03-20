import pandas as pd
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("filepath", type=Path)
p = parser.parse_args()


def fixcsv(df):
    df2 = df[~((df['Address1'].str.len() > 25) | (df['Address2'].str.len() > 1))].copy(True)
    df2 = df2.fillna('')
    
    df2.to_csv(inputstr, index = False)
    print(f'{inputstr} fixed sucessfully!')
    
def touchcsv():
    df2 = df[(df['Address1'].str.len() > 25) | (df['Address2'].str.len() > 1)].copy(True)
    df2.to_csv('longlabels.csv', index = False)
    print('File touched up successfully!')
            
        

exit = False

inputstr = p.filepath
while(exit == False):
    try:
        df = pd.read_csv(inputstr)         
        fixcsv(df)
        touchcsv()
        exit = True
    except:
        print(f'Unable to find file {inputstr} or already fixed. Please check for typos and try again.')
        exit = True