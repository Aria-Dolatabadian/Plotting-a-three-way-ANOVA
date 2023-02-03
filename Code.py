import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv (r'Fertilizer.csv')
#df = pd.read_csv (r'Fertilizer2.csv')

print(df)

sns.set_theme(style="whitegrid")

g = sns.catplot(x="time", y="Plant height", hue="Cultivar", col="Fertilizer",
                capsize=.2, palette="YlGnBu_d", height=6, aspect=.75,
                kind="point", data=df)
g.despine(left=False)
plt.show()
