import pandas as pd

def drop_duplicates():
    df1 = pd.read_csv("activity_filter_BMF.csv")
    df2 = pd.read_csv("ntee_filter_BMF.csv")
    full_df = pd.concat([df1,df2])
    unique_df = full_df.drop_duplicates(keep='last')
    unique_df.to_csv("merge_BMF.csv", index=False)
if __name__ == '__main__':
    drop_duplicates()

