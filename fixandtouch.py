import pandas as pd

def fixcsv(df):
    df2 = df[~((df['Address1'].str.len() > 25) | (df['Address2'].str.len() > 1))].copy(True)
    df2 = df2.fillna('')
    
    df2.to_csv(stringsplit[1], index = False)
    print(f'{stringsplit[1]} fixed sucessfully!')
    
def touchcsv():
    df2 = df[(df['Address1'].str.len() > 25) | (df['Address2'].str.len() > 1)].copy(True)
    df2.to_csv('longlabels.csv', index = False)
    print('File touched up successfully!')
            
        

exit = False
while exit==False:
    inputstr = input()
    stringsplit = inputstr.split()
    if stringsplit[0] == "fixcsv":
        try:
            df = pd.read_csv(stringsplit[1])         
            fixcsv(df)
            touchcsv()
        except:
            print(f'Unable to find file {stringsplit[1]}. Please check for typos and try again.')
            continue

    elif stringsplit[0] == "quit" or "exit":
        exit = True
    else:
        print(f'Input {stringsplit} not recognized, please use proper syntax!')
        continue
        
        
