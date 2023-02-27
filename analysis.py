import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def get_male_ages(surfers):
    return surfers.loc[surfers['Category'] == 'M']['Age']

def get_female_ages(surfers):
    return surfers.loc[surfers['Category'] == 'F']['Age']

def get_average_ages(surfers):
    avg_ages = dict()

    avg_ages['all'] = round(surfers[['Age']].mean()[0], 1)
    avg_ages['male'] = round(get_male_ages(surfers).mean(), 1)
    avg_ages['female'] = round(get_female_ages(surfers).mean(), 1)

    return avg_ages

def get_category_stances(surfers):
    stances = dict()

    grp = surfers.groupby(['Category', 'Stance'], sort=False)['Stance'].count()
    grp.sort_index(ascending=False)
    
    stances['female'] = grp['F'].values
    stances['male'] = grp['M'].values

    return stances

def plot_age_category_distribution(ages, avg_age, color, label):
    age_bins = [10,20,30,40,50,60,70]
    alpha=0.6
    mean_line_width=2

    # Display age distribution
    plt.hist(ages, bins=age_bins, alpha=alpha, color=color, label=label)
    # Display average age as dashed line
    plt.axvline(avg_age, color=color, linestyle='dashed', linewidth=mean_line_width)

def plot_age_distributions(surfers):
    avg_ages = get_average_ages(surfers)

    plot_age_category_distribution(get_male_ages(surfers), avg_ages['male'], 'blue', 'Men')
    plot_age_category_distribution(get_female_ages(surfers), avg_ages['female'], 'yellow', 'Women')

    ax = plt.legend(loc='upper right')
    ax.set_title('Surfer Ages')
    plt.show()

def plot_home_towns(surfers):
    x = surfers['Home'].value_counts().values
    labels = surfers['Home'].value_counts().index
    colors = plt.get_cmap('Paired')(np.linspace(0.1, 0.8, len(x)))

    # plot
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.set_title('Surfer Hometowns')
    patches, texts, pcts  = ax.pie(
        x, colors=colors, labels=labels,
        autopct='%.1f%%', pctdistance=.83,
        labeldistance=1.1,
    wedgeprops={"linewidth": 3, "edgecolor": "white"}, frame=False)
    for i, patch in enumerate(patches):
        texts[i].set_color(patch.get_facecolor())

    plt.setp(texts, fontweight=600)
    plt.setp(pcts, color='white', fontweight=600)

    plt.show()

def add_category_bargraph(ax, stances, bottom, color):
    barWidth = 0.5
    alpha = 0.5
    stance_types = ['Regular', 'Goofy']

    category_bargraph = ax.bar(stance_types, stances, bottom=bottom, width=barWidth, alpha=alpha, color=color)
    ax.bar_label(category_bargraph, label_type='center')

    return category_bargraph

def plot_stances(surfers):
    stances = get_category_stances(surfers)

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.set_title('Surfer Stances')

    # Display stacked bar chart
    female_bargraph = add_category_bargraph(ax, stances['female'], 0, "yellow")
    male_bargraph = add_category_bargraph(ax, stances['male'], stances['female'], "blue")
    ax.legend([male_bargraph, female_bargraph], ["Men", "Women"])
    plt.show()

surfers = pd.read_csv("surfers.csv")

category = surfers['Category'].value_counts(normalize=True) * 100
home = surfers['Home'].value_counts(normalize=True) * 100
stance = surfers['Stance'].value_counts(normalize=True) * 100

plot_age_distributions(surfers)
plot_home_towns(surfers)
plot_stances(surfers)
