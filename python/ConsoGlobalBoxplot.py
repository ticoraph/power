import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def gini(x):
    total = 0
    for i, xi in enumerate(x[:-1], 1):
        total += np.sum(np.abs(xi - x[i:]))
    return total / (len(x)**2 * np.mean(x))

data = pd.read_csv('../csv/Conso-ByDay.csv')
#print(data.head())

#print(data.dtypes)
data['Date'] = pd.to_datetime(data['Date'],dayfirst=True)
#print(data.dtypes)

data.boxplot(column="Conso", vert=False)
plt.show()

