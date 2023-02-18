import pandas as pd
import matplotlib.pyplot as plt

def get_average_ages(surfers):
    avg_ages = dict()

    avg_ages['all'] = round(surfers[['Age']].mean()[0], 1)
    avg_ages['male'] = round(surfers.loc[surfers['Category'] == 'M']['Age'].mean(), 1)
    avg_ages['female'] = round(surfers.loc[surfers['Category'] == 'F']['Age'].mean(), 1)

    return avg_ages

def plot_age_histogram(surfers):
    age_bins = [10,20,30,40,50,60,70]
    alpha=0.6
    mean_line_width=2
    male_color = 'blue'
    female_color = 'yellow'

    avg_ages = get_average_ages(surfers)

    plt.hist(surfers.loc[surfers['Category'] == 'M']['Age'], bins=age_bins, alpha=alpha, color=male_color, label='Men')
    plt.axvline(avg_ages['male'], color=male_color, linestyle='dashed', linewidth=mean_line_width)
    plt.hist(surfers.loc[surfers['Category'] == 'F']['Age'], bins=age_bins, alpha=alpha, color=female_color, label='Women')
    plt.axvline(avg_ages['female'], color=female_color, linestyle='dashed', linewidth=mean_line_width)
    plt.legend(loc='upper right')
    plt.show()

surfers = pd.read_csv("surfers.csv")

category = surfers['Category'].value_counts(normalize=True) * 100
home = surfers['Home'].value_counts(normalize=True) * 100
stance = surfers['Stance'].value_counts(normalize=True) * 100

avg_ages = get_average_ages(surfers)
plot_age_histogram(surfers)

