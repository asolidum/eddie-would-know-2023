import pandas as pd
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

def plot_age_histogram(surfers):
    age_bins = [10,20,30,40,50,60,70]
    alpha=0.6
    mean_line_width=2
    male_color = 'blue'
    female_color = 'yellow'

    avg_ages = get_average_ages(surfers)

    plt.hist(get_male_ages(surfers), bins=age_bins, alpha=alpha, color=male_color, label='Men')
    plt.axvline(avg_ages['male'], color=male_color, linestyle='dashed', linewidth=mean_line_width)
    plt.hist(get_female_ages(surfers), bins=age_bins, alpha=alpha, color=female_color, label='Women')
    plt.axvline(avg_ages['female'], color=female_color, linestyle='dashed', linewidth=mean_line_width)
    plt.legend(loc='upper right')
    plt.show()

def plot_home_towns(surfers):
    x = surfers['Home'].value_counts().values
    labels = surfers['Home'].value_counts().index
    colors = plt.get_cmap('Paired')(np.linspace(0.1, 0.8, len(x)))

    # plot
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.set_title('2022 Tag Breakdown')
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

surfers = pd.read_csv("surfers.csv")

category = surfers['Category'].value_counts(normalize=True) * 100
home = surfers['Home'].value_counts(normalize=True) * 100
stance = surfers['Stance'].value_counts(normalize=True) * 100

avg_ages = get_average_ages(surfers)
plot_age_histogram(surfers)
plot_home_towns(surfers)

