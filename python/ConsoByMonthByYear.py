import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

groupbyyear = data.groupby(data['Date'].dt.year)['Conso'].sum()
df_result = groupbyyear.reset_index()
df_result.columns = ['Year', 'Conso Total']

with open("../ConsoByMonthByYear.md", "w", encoding="utf-8") as f:
    f.write("**[Index](index.md)**\n\n")
    f.write(f"{df_result.to_markdown(index=False)}\n\n")

#print(groupbyyear)

for year,subset in data.groupby(data['Date'].dt.year):

    results = {
        "ANNEE": year,
        "Nombres de valeurs (Conso kW par jour)": subset['Conso'].count(),
        "mode (Conso la plus frequente)": subset['Conso'].mode().iloc[0],
        "nombre mode": len(subset['Conso'].mode()),
        "mean (Conso Moyenne)": subset['Conso'].mean().round(2),
        "median (Conso Mediane)": subset['Conso'].median().round(2),
        "Conso Min": subset['Conso'].min().round(2),
        "Conso Max": subset['Conso'].max().round(2),
        "Variance sample": subset['Conso'].var(ddof=1).round(2),
        "Variance population (Valeurs dispersees autour de la moyenne)": subset['Conso'].var(ddof=0).round(2),
        "Ecart Type sample": subset['Conso'].std(ddof=1).round(2),
        "Ecart Type population (les valeurs s’ecartent d’environ x unités de la moyenne)": subset['Conso'].std(
            ddof=0).round(2),
        "Coeff de variation": (subset['Conso'].std() / subset['Conso'].mean() * 100).round(2),
        "Skewness (symetrie d’une distribution autour de sa moyenne)": subset['Conso'].skew().round(2),
        "Kurtosis": subset['Conso'].kurtosis().round(2),
        "GINI (dispersion ou inegalite - 0 a 1)": gini(subset['Conso']).round(2)
    }
    with open("../ConsoByMonthByYear.md", "a", encoding="utf-8") as f:
        for key, value in results.items():
            f.write(f"- **{key}** : {value}\n")
        f.write(f"\n\n##############################################\n\n")

    monthly_data = subset.groupby(subset['Date'].dt.month)['Conso'].mean()
    monthly_data = monthly_data.reindex(range(1, 13))  # Force tous les mois 1-12

    plt.figure(figsize=(12, 6))
    monthly_data.plot(kind='bar')
    plt.title(f'Consommation moyenne par mois - {year}')
    plt.xlabel('Mois')
    plt.ylabel('Consommation moyenne')

    mean_subset = subset['Conso'].mean()
    median_subset = subset['Conso'].median()
    mode_subset = subset['Conso'].mode().iloc[0]

    plt.axhline(y=mean_subset, color='red', linestyle='--', linewidth=2, label=f'Moyenne subset: {mean_subset:.2f}')
    plt.axhline(y=median_subset, color='green', linestyle='--', linewidth=2, label=f'Médiane subset: {median_subset:.2f}')
    plt.axhline(y=mode_subset, color='orange', linestyle='--', linewidth=2, label=f'Mode subset: {mode_subset:.2f}')

    month_names = ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Jun',
                   'Jul', 'Aoû', 'Sep', 'Oct', 'Nov', 'Déc']

    plt.xticks(range(12), month_names, rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f'../images/ConsoByMonthByYear{year}.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    #plt.show()

