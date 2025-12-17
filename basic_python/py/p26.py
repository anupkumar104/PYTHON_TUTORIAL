#pandas DataFrame with NumpyArray:Return Tabular
import pandas as pd
import numpy as np
rec= {"name":["Ram","Joe","Anshu"],
      "Age":np.array([12,18,22]),
      "weight":[55,78,44],
      "height":[5.5,6.6,5.2],
      "Sibling":1}
df= pd.DataFrame(rec)
print("Table-1",df)
df2= pd.DataFrame(rec,index=rec['name'])
print("Table-2",df2)
print("Output-A",df2['weight'])
#To access any column we use df.column_name
print('output-B',df2.height)
#Add new column in dataSet
df2['IQ']=[111,105,109]
print("New Table-",df2)