import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def gini(x):
    total = 0
    for i, xi in enumerate(x[:-1], 1):
        total += np.sum(np.abs(xi - x[i:]))
    return total / (len(x)**2 * np.mean(x))

data = pd.read_csv('data/Conso-ByDay.csv')
#print(data.head())
#print(data.dtypes)
data['Date'] = pd.to_datetime(data['Date'],dayfirst=True)
#print(data.isnull().sum())

print("######### Conso Total Stats #########")
print("mode:",data['Conso'].mode())
print("mean:",data['Conso'].mean().round())
print("median:",data['Conso'].median())
print("min:",data['Conso'].min())
print("max:",data['Conso'].max())
print("Variance sample:",data['Conso'].var(ddof=1))
print("Variance population:",data['Conso'].var(ddof=0))
print("Ecart Type sample:",data['Conso'].std(ddof=1))
print("Ecart Type population:",data['Conso'].std(ddof=0))
print("Coeff de variation:",data['Conso'].std()/data['Conso'].mean()*100)
print("Skewness:",data['Conso'].skew())
print("Kurtosis:",data['Conso'].kurtosis())
print("GINI:",gini(data['Conso']))

#data.boxplot(column="Conso", vert=False)
#plt.show()

# Version plus directe
monthly_by_year = data.groupby([data['Date'].dt.year, data['Date'].dt.month])['Conso'].mean().unstack(level=0)
monthly_by_year = monthly_by_year.reindex(range(1, 13))  # Force tous les mois

plt.figure(figsize=(20, 8))
monthly_by_year.plot(kind='bar', width=0.8)
plt.title('Consommation moyenne par mois - Toutes les années')
plt.xlabel('Mois')
plt.ylabel('Consommation moyenne')

month_names = ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Jun',
               'Jul', 'Aoû', 'Sep', 'Oct', 'Nov', 'Déc']
plt.xticks(range(12), month_names, rotation=45)
plt.legend(title='Année')
plt.tight_layout()
plt.savefig('images/ConsoGlobal.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
plt.show()


