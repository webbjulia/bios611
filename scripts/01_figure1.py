import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('processed.csv')

plt.hist(data['PAM50 mRNA'])
plt.savefig('figures/figure1.pdf',format='pdf')