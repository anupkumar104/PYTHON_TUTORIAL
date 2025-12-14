#key/value object as series with labeled index
import pandas as pd
s={"A":12,"B":15,"C":89,'D':63,"E":56}
x=pd.Series(s,index=["d1","d2","d3","d4","d5"])
print(x)