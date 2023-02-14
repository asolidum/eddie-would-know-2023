import pandas as pd

def get_average_ages(surfers):
    avg_ages = dict()

    avg_ages['all'] = surfers[['Age']].mean()[0]
    avg_ages['male'] = surfers.loc[surfers['Category'] == 'M']['Age'].mean()
    avg_ages['female'] = surfers.loc[surfers['Category'] == 'F']['Age'].mean()

    return avg_ages

surfers = pd.read_csv("surfers.csv")

category = surfers['Category'].value_counts(normalize=True) * 100
home = surfers['Home'].value_counts(normalize=True) * 100
stance = surfers['Stance'].value_counts(normalize=True) * 100

avg_ages = get_average_ages(surfers)

