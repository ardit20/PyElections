import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.DataFrame({'parties': ['LVV', 'PDK', 'LDK', 'AAK', 'Nisma', 'Guxo', 'PSD'],
                   'votes': [39.6, 21.9, 20.3, 7.0, 1.9, 1.3, 0.7],
                   'colors': ['red', 'orange', 'blue', 'gray', 'gray', 'gray', 'pink']})

sns.set_style("whitegrid")
ax = sns.barplot(x="parties", y="votes", data=df, palette=df['colors'], alpha=0.8)

plt.title('Kosovo Parliamentary Elections')
plt.xlabel('Parties')
plt.ylabel('Votes Percentage')

plt.show()


