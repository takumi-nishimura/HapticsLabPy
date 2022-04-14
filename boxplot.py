import matplotlib.pyplot as plt
import seaborn as sns
import plot_style
import pandas as pd
import numpy as np

d = pd.read_excel('All_Ownership_sample.xlsx')
print(d)

sns.set_palette('Set2')
sns.boxplot(x='Condition',y='Score',data=d,hue='Cycle')
plt.show()

# wo = d[d['Condition'] == 'without feedback']
# pv = d[d['Condition'] == 'partner velocity']
# rv = d[d['Condition'] == 'robot velocity']
# plt.boxplot([wo['Score'],pv['Score'],rv['Score']])
# plt.show()