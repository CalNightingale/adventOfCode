import pandas as pd
import numpy as np

master_df = pd.read_csv("data.csv", skip_blank_lines=False)
big3Tot = sum(sorted([df.sum().item() for df in np.split(master_df, master_df[master_df.isnull().all(1)].index)])[-3:])
print(big3Tot)
