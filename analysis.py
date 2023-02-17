import pandas as pd
import matplotlib.pyplot as plt

def get_average_ages(surfers):
    avg_ages = dict()

    avg_ages['all'] = round(surfers[['Age']].mean()[0], 1)
    avg_ages['male'] = round(surfers.loc[surfers['Category'] == 'M']['Age'].mean(), 1)
    avg_ages['female'] = round(surfers.loc[surfers['Category'] == 'F']['Age'].mean(), 1)

    return avg_ages

surfers = pd.read_csv("surfers.csv")

category = surfers['Category'].value_counts(normalize=True) * 100
home = surfers['Home'].value_counts(normalize=True) * 100
stance = surfers['Stance'].value_counts(normalize=True) * 100

avg_ages = get_average_ages(surfers)

surfers.plot.hist(column=['Age'], bins=[10,20,30,40,50,60,70])
plt.show()
