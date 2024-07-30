import pandas as pd

#reading a csv file
df=pd.read_csv("heart.csv")
#display of converted dataframe
print(df.head(5))

#displays total number of values empty
print(df.isnull().sum())
#drops rows wherever null values present
df.dropna()

#groups data according to by condition
df.groupby(by='target')

#filters data of target
print(df[df.target==1])

#sorts value in ascending order
print(df.sort_values(by='age'))
