import pandas as pd
x=[12,15,89,63,56]
# df= pd.Series(x)
# print(df)


#labeled series
df=pd.Series(x,index=['A','B','C','D','E'])
print(df)