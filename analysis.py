import pandas as pd

surfers = pd.read_csv("surfers.csv")

category = surfers['Category'].value_counts(normalize=True) * 100
home = surfers['Home'].value_counts(normalize=True) * 100
stance = surfers['Stance'].value_counts(normalize=True) * 100
avg_age = surfers[['Age']].mean()
avg_age_male = surfers.loc[surfers['Category'] == 'M']['Age'].mean()
avg_age_female = surfers.loc[surfers['Category'] == 'F']['Age'].mean()
