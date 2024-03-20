import pandas as pd

def fixcsv(df):
    df2 = df[~((df['Address1'].str.len() > 25) | (df['Address2'].str.len() > 1))].copy(True)
    df2 = df2.fillna('')
    
    df2.to_csv(stringsplit, index = False)
    print(f'{stringsplit} fixed sucessfully!')
    
def touchcsv():
    df2 = df[(df['Address1'].str.len() > 25) | (df['Address2'].str.len() > 1)].copy(True)
    df2.to_csv('longlabels.csv', index = False)
    print('File touched up successfully!')
            
stringsplit = input("Type the name of a csv file in your current directory")
df = pd.read_csv(stringsplit)         
fixcsv(df)
touchcsv()