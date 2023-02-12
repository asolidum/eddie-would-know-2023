import pandas as pd

surfers = pd.read_csv("surfers.csv")

category = surfers['Category'].value_counts(normalize=True) * 100
home = surfers['Home'].value_counts(normalize=True) * 100
stance = surfers['Stance'].value_counts(normalize=True) * 100
