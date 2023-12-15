import pandas as pd
import matplotlib.pyplot as plt
from upsetplot import plot

data = pd.read_csv('processed.csv')

ER_positive = set(data[data['ER Status']=='Positive']['Complete TCGA ID'])
ER_negative = set(data[data['ER Status']=='Negative']['Complete TCGA ID'])
PR_positive = set(data[data['PR Status']=='Positive']['Complete TCGA ID'])
PR_negative = set(data[data['PR Status']=='Negative']['Complete TCGA ID'])
HER2_positive = set(data[data['HER2 Final Status']=='Positive']['Complete TCGA ID'])
HER2_negative = set(data[data['HER2 Final Status']=='Negative']['Complete TCGA ID'])

set_names = ['ER Positive', 'ER Negative', 
             'PR Positive', 'PR Negative',
            'HER2 Positive', 'HER2 Negative']
sets = [ER_positive, ER_negative, PR_positive, PR_negative, HER2_positive, HER2_negative]
all_elems = list(set().union(*sets))
df = pd.DataFrame([[e in st for st in sets] for e in all_elems], columns = set_names)
df_up = df.groupby(set_names).size()
plot(df_up, orientation='horizontal')

plt.savefig('figures/figure2.pdf',format='pdf')