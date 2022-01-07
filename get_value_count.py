from numpy import unicode_
import pandas as pd
df = pd.read_csv('sample.csv',header = None)
df2 = pd.DataFrame(columns=['Number','Count'])
first_value = df.iloc[0][0]
count = 0
offset = 0
for i in range(len(df.iloc[:,1].unique())):
    next_value = df.iloc[offset][0]
    have_next = False
    while first_value == next_value:
        count += 1
        try:
            next_value = df.iloc[offset+count][0]
        except Exception:
            have_next = True
            break
    offset += count
    print(count)
    df2.loc[i,['Number','Count']] = [first_value, count]
    first_value = next_value
    count = 0
    if have_next == True:
        break
df2.to_csv('output.csv')