import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('processed.csv')
pam50 = pd.read_csv('data/PAM50_proteins.csv')

data = data.dropna(axis='columns')

x_pam50 = data[data.columns[data.columns.isin(list(pam50['RefSeqProteinID']))]]

y=data['PAM50 mRNA']
y=y.replace(['Luminal B'],0)
y=y.replace(['Luminal A'],1)
y=y.replace(['Basal-like'],2)
y=y.replace(['HER2-enriched'],3)
y = list(y)

n_neighbors = 3
random_state = 0

X = np.asarray(x_pam50)
y = np.asarray(y)

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5, stratify=y, random_state=random_state
)

dim = len(X[0])
n_classes = len(np.unique(y))

# Reduce dimension to 2 with PCA
pca = make_pipeline(StandardScaler(), PCA(n_components=2, random_state=random_state))

# Use a nearest neighbor classifier to evaluate the methods
knn = KNeighborsClassifier(n_neighbors=n_neighbors)

plt.figure()

# Fit the method's model
pca.fit(X_train, y_train)

# Fit a nearest neighbor classifier on the embedded training set
knn.fit(pca.transform(X_train), y_train)

# Compute the nearest neighbor accuracy on the embedded test set
acc_knn = knn.score(pca.transform(X_test), y_test)

# Embed the data set in 2 dimensions using the fitted model
X_embedded = pca.transform(X)
variance_explained = pca[1].explained_variance_ratio_
pc1=round(variance_explained[0]*100,2)
pc2=round(variance_explained[1]*100,2)

# Plot the projected points and show the evaluation score
plt.scatter(X_embedded[:, 0], X_embedded[:, 1], c=y, s=30, cmap="Set1")
plt.title(
    "{}, KNN (k={})\nTest accuracy = {:.2f}".format('PCA', n_neighbors, acc_knn)
)
plt.xlabel("{}% of variance".format(pc1))
plt.ylabel("{}% of variance".format(pc2))

plt.savefig('figures/figure4.png',format='png')