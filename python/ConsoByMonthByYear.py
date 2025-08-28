import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
#print(datetime.date.today().year)
#print(datetime.date.today().day)
#print(datetime.date.today().month)

data = pd.read_csv('data/Conso-ByDay.csv')
#print(data.head())

#print(data.dtypes)
data['Date'] = pd.to_datetime(data['Date'],dayfirst=True)
#print(data.dtypes)

groupbyyear = data.groupby(data['Date'].dt.year)['Conso'].sum()
print(groupbyyear)

for year,subset in data.groupby(data['Date'].dt.year):
    print("-" * 20)
    print(f"Year: {year}")
    print(f"Mean: {subset['Conso'].mean():.2f}")
    print(f"Median: {subset['Conso'].median():.2f}")
    print(f"Mode: {subset['Conso'].mode().iloc[0]:.2f}")  # mode() returns a Series

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
    plt.savefig(f'images/ConsoByMonthByYear{year}.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.show()

'''
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
'''



