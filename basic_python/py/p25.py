#dataframe with series in pandas
import pandas as pd
d={"one":pd.Series([1,2,3],index=["a","b","c"]),
"two":pd.Series([10,20,30,40],index=["a","b","c","d"]),
   }
df=pd.DataFrame(d)
print(df)