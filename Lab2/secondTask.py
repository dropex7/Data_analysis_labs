import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


gas = pd.read_csv('stock_quotes/gas.csv', sep=';', index_col='Дата')
x = StandardScaler().fit_transform(gas.T)
pca = PCA()
principal_components = pca.fit_transform(x)

per_var = np.round(pca.explained_variance_ratio_ * 100, decimals=1)
labels = ['PC' + str(x) for x in range(1, len(per_var) + 1)]

principal_df = pd.DataFrame(principal_components, index=gas.columns.tolist(), columns=labels)

plt.scatter(principal_df.PC1, principal_df.PC2)
plt.title("PCA gas graph")
plt.xlabel(f'PC1 - {per_var[0]}%')
plt.ylabel(f'PC2 - {per_var[1]}%')

for sample in principal_df.index:
    plt.annotate(sample, (principal_df.PC1.loc[sample], principal_df.PC2.loc[sample]))

plt.show()
