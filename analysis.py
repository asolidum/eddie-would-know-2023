import pandas as pd

surfers_df = pd.read_csv("surfers.csv")

category_df = surfers_df['Category'].value_counts(normalize=True) * 100
home_df = surfers_df['Home'].value_counts(normalize=True) * 100
stance_df = surfers_df['Stance'].value_counts(normalize=True) * 100
