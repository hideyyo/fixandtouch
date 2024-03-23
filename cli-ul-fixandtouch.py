import pandas as pd
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("filepath", type=Path)
p = parser.parse_args()


def fixcsv(df):
    try:
        df2 = df[~((df['Address1'].str.len() > 25) or df(['City'].str.len() >= 20) or (df['Address2'].str.len() > 1))].copy(True)
        df2 = df2.fillna('')
        df2.to_csv(inputstr, index = False)
        print(f'{inputstr} fixed sucessfully!')
    except:
        print(f'File {inputstr} already fixed!')
    
def touchcsv():
    try:
        df2 = df[(df['Address1'].str.len() > 25) | (df['Address2'].str.len() > 1)].copy(True)
        df2.to_csv('longlabels.csv', index = False)
        print('File touched up successfully!')
    except:
        print(f'File {inputstr} doesn\'t need to be touched!')
            
        

exit = False

extention_name = '.csv'
inputstr = p.filepath.stem + extention_name
while(exit == False):
    try:
        df = pd.read_csv(inputstr)         
        fixcsv(df)
        touchcsv()
        exit = True
    except:
        print(f'File {inputstr} not found, please check for typos and try again.')
        exit = True