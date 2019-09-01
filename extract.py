import pandas as pd

f = pd.read_csv("BMF.csv")
keep_col = ['EIN', 'NAME', 'STREET', 'CITY', 'ZIP', 'ACTIVITY', 'NTEE_CD', 'REVENUE_AMT']
new_f = f[keep_col]
new_f.to_csv("new_BMF.csv", index=False)
