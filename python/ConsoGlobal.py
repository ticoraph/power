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
#print(data.isnull().sum())

results = {
"Nombres de valeurs (Conso kW par jour)"    : data['Conso'].count(),
"mode (Conso la plus frequente)"     : data['Conso'].mode().iloc[0],
"nombre mode"     : len(data['Conso'].mode()),
"mean (Conso Moyenne)"     : data['Conso'].mean().round(2),
"median (Conso Mediane)"   : data['Conso'].median().round(2),
"Conso Min"      : data['Conso'].min().round(2),
"Conso Max"      : data['Conso'].max().round(2),
"Variance sample"      : data['Conso'].var(ddof=1).round(2),
"Variance population (Valeurs dispersees autour de la moyenne)"  : data['Conso'].var(ddof=0).round(2),
"Ecart Type sample"    : data['Conso'].std(ddof=1).round(2),
"Ecart Type population (les valeurs s’ecartent d’environ x unités de la moyenne)"    : data['Conso'].std(ddof=0).round(2),
"Coeff de variation"       : (data['Conso'].std()/data['Conso'].mean()*100).round(2),
"Skewness (symetrie d’une distribution autour de sa moyenne)" : data['Conso'].skew().round(2),
"Kurtosis" : data['Conso'].kurtosis().round(2),
"GINI (dispersion ou inegalite - 0 a 1)"     : gini(data['Conso']).round(2)
}


with open("../PowerConsoGlobal.md", "w", encoding="utf-8") as f:
    for key, value in results.items():
        f.write(f"- **{key}** : {value}\n")

print(results)

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
plt.savefig('../images/ConsoGlobal.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
plt.show()


