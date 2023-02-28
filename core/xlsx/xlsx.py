import pandas as pd

def do_xlsx(users):
    df = pd.DataFrame.to_dict(users)
    print(df)