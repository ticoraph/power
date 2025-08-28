import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

data = pd.read_csv('csv/Conso-ByDay.csv')
datatemp = pd.read_csv('csv/TempChamberyByMonth.csv')
#print(data.head())
#print(datatemp.head())

data['Date'] = pd.to_datetime(data['Date'],dayfirst=True)
datatemp['Date'] = pd.to_datetime(datatemp['Date'],format='%Y%m')
#print(datatemp.dtypes)
#print(datatemp.head())

groupbyyear = data.groupby(data['Date'].dt.year)['Conso'].sum()
print(groupbyyear)
print("-" * 20)
#tempgroupbyyear = datatemp.groupby(datatemp['Date'].dt.year)['Temp'].mean()
#print(tempgroupbyyear)

data["DateMonth"] = pd.to_datetime(data["Date"].dt.to_period("M").astype(str))
#print(data.head())
datatemp["DateTempMonth"] = pd.to_datetime(datatemp["Date"].dt.to_period("M").astype(str))
#print(datatemp.head())
datamerge = pd.merge(data, datatemp, left_on='DateMonth', right_on='DateTempMonth', how='left')
print(datamerge)
print(datamerge.dtypes)

for year,subset in datamerge.groupby(datamerge['DateMonth'].dt.year) :
    print("-" * 20)
    print(f"Year: {year}")
    print(f"Conso Mean: {subset['Conso'].mean():.2f}")
    print(f"Conso Median: {subset['Conso'].median():.2f}")
    print(f"Conso Mode: {subset['Conso'].mode().iloc[0]:.2f}")
    print(f"Temp Mean: {subset['Temp'].mean():.2f}")

    monthly_data = subset.groupby(subset['DateMonth'].dt.month)['Conso'].mean()
    print (monthly_data)
    monthly_dataTemp = subset.groupby(subset['DateTempMonth'].dt.month-1)['Temp'].mean()
    print(monthly_dataTemp)

    month_names = ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Jun',
                   'Jul', 'Aoû', 'Sep', 'Oct', 'Nov', 'Déc']

    #x = np.arange(len(month_names))

    monthly_data = monthly_data.reindex(range(1, 13))  # Force tous les mois 1-12
    monthly_dataTemp = monthly_dataTemp.reindex(range(0, 12))  # Force tous les mois 1-12

    plt.figure(figsize=(12, 6))
    monthly_data.plot(kind='bar')
    monthly_dataTemp.plot(kind="line",linewidth='2',color="magenta")
    plt.title(f'Consommation moyenne par mois - {year}')
    plt.xlabel('Mois')
    plt.ylabel('Consommation moyenne')

    mean_subset = subset['Conso'].mean()
    median_subset = subset['Conso'].median()
    mode_subset = subset['Conso'].mode().iloc[0]

    plt.axhline(y=mean_subset, color='red', linestyle='--', linewidth=2, label=f'Moyenne subset: {mean_subset:.2f}')
    plt.axhline(y=median_subset, color='green', linestyle='--', linewidth=2, label=f'Médiane subset: {median_subset:.2f}')
    plt.axhline(y=mode_subset, color='orange', linestyle='--', linewidth=2, label=f'Mode subset: {mode_subset:.2f}')

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

    DateYYYYMM = subset['Date'].dt.strftime("%Y%m")
    print(DateYYYYMM)
    DateYYYYMMTemp = datatemp['Date'].dt.strftime("%Y%m")
    print(DateYYYYMMTemp)
    if DateYYYYMM.unique == DateYYYYMMTemp.unique:
        print(f"Temp: {datatemp['Temp']}")
        
'''



