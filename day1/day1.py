import pandas as pd
import numpy as np

master_df = pd.read_csv("data.csv", skip_blank_lines=False)

df_list = np.split(master_df, master_df[master_df.isnull().all(1)].index)
sums = [df.sum().item() for df in df_list]
sums = sorted(sums)
print(sum(sums[-3:]))
