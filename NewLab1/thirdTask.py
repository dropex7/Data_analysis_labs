import math
import random

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


def endorsement(data, column_index):
    for index in range(data[column_index].size):
        if math.isnan(data[column_index][index]):
            if math.isfinite(data[column_index][index - 1]):
                data[column_index][index] = data[column_index][index - 1]
                continue
            elif math.isfinite(data[column_index][index + 1]):
                data[column_index][index] = data[column_index][index + 1]
                continue


def linear_recovery(data, column_index):
    for index in range(data[column_index].size):
        if math.isnan(data[column_index][index]):
            missing_value = data[column_index].interpolate()[index]
            data[column_index][index] = missing_value


def correlation_recovery(data, column_index):
    for item in range(data[column_index].size):
        if math.isnan(data[column_index][item]):
            if item + 1 < data[column_index].size:
                if math.isfinite(data[column_index][item + 1]):
                    p1 = data["Макс."][item]
                    p2 = data["Макс."][item + 1]
                    v2 = data[column_index][item + 1]
                    missing_value = (v2 / p1) * p2
            elif math.isfinite(data[column_index][item - 1]):
                p1 = data["Макс."][item - 1]
                v1 = data[column_index][item - 1]
                p2 = data["Макс."][item]
                missing_value = (p1 / p2) * v1

            data[column_index][item] = missing_value


visa = pd.read_csv('visa.csv', sep=';', index_col='Дата')
mastercard = pd.read_csv('mastercard.csv', sep=';', index_col='Дата')
visa_and_mastercard = visa.merge(mastercard, on='Дата')

plt.figure(figsize=(10, 10))
sns.heatmap(visa_and_mastercard.corr(),
            center=0, cmap='Blues', annot=True)
plt.title('Visa and Mastercard', fontsize=17)
plt.show()


missing_pct = int(visa['Цена'].size * 0.1)
i = [random.choice(range(visa['Цена'].shape[0])) for _ in range(missing_pct)]
visa['Цена'][i] = np.NaN
visa['Цена'][visa['Цена'].shape[0] - 1] = np.NaN
visa['Цена'][visa['Цена'].shape[0] - 2] = np.NaN

visa_1 = visa.copy()
visa_2 = visa.copy()
visa_3 = visa.copy()

print(visa_3)

endorsement(visa_1, "Цена")
linear_recovery(visa_2, "Цена")
correlation_recovery(visa_3, "Цена")

print(visa_3)
