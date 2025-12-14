#pandas with dataframe
import pandas as pd
d={
    "name":["ravi","suman","amit"],
    "age":[22,24,56],
    "city":["lucknow","delhi","mumbai"]
}
df=pd.DataFrame(d)
print("output-1")
print(df)
print("output-2")
print(df.head())
print("output-3",df["age"])
print("output-4",df[df["age"]>22])
print("output-5",df.describe())