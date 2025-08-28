import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import probplot
from statsmodels.iolib import summary


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
    f.write("**[Index](index.md)**\n")
    for key, value in results.items():
        f.write(f"- **{key}** : {value}\n")

#print(results)

###############################################
# HISTOGRAM CONSO GLOBAL
###############################################

monthly_by_year = data.groupby([data['Date'].dt.year, data['Date'].dt.month])['Conso'].mean().unstack(level=0)
monthly_by_year = monthly_by_year.reindex(range(1, 13))  # Force tous les mois

plt.figure(figsize=(20, 8))
monthly_by_year.plot(kind='bar', width=0.8)
plt.title('Home Energy Consumption (kW)')
plt.xlabel('Month')
plt.ylabel('Consumption Mean (kW)')

month_names = ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Jun',
               'Jul', 'Aoû', 'Sep', 'Oct', 'Nov', 'Déc']
plt.xticks(range(12), month_names, rotation=45)
plt.legend(title='Year')
plt.tight_layout()
plt.savefig('../images/ConsoGlobal.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
#plt.show()

###############################################
# HISTOGRAM CONSO GLOBAL SKEWNESS
###############################################

plt.figure(figsize=(8, 5))
sns.histplot(data['Conso'], kde=True, bins=30, color='skyblue')
plt.title('Home Energy Consumption Skewness')
plt.suptitle('Values smaller or larger than the average')
plt.xlabel('Consumption')
plt.ylabel('Frequency')
plt.grid(False)
plt.savefig('../images/ConsoGlobalSkewness.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
#plt.show()

###############################################
# COURBE CONSO GLOBAL kurtosis
###############################################

# Q-Q plot to check normality
plt.figure(figsize=(6, 6))
probplot(data['Conso'], dist="norm", plot=plt)
plt.title('Home Energy Consumption Kurtosis')
plt.suptitle('Scattered values or many extreme values')
plt.xlabel('Kurtosis')
plt.ylabel('Consumption')
plt.grid(True)
plt.savefig('../images/ConsoGlobalKurtosis.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
#plt.show()

##############################################
# COURBE CONSO GLOBAL LORENZ
###############################################

Consommation = data['Conso'].values
n = len(Consommation)
lorenz = np.cumsum(np.sort(Consommation)) / Consommation.sum()
lorenz = np.append([0],lorenz) # La courbe de Lorenz commence à 0
xaxis = np.linspace(0-1/n,1+1/n,n+1)
blue = "#0065D1"  # Lighter blue for the Lorenz curve
orange = "#FF5A1F"  # Bright orange for the line of perfect equality

plt.figure(figsize=(8, 6))
plt.title("Home Energy Consumption Lorenz")
plt.suptitle('Values with inequalities')

plt.plot([0, 1], [0, 1], label="Line of Perfect Equality", color=orange, linewidth=2)
plt.plot(xaxis,lorenz,drawstyle='steps-post',label="Lorenz Curve",color=blue,)

# Label the x-axis to show what the horizontal axis represents
plt.xlabel("X", fontsize=12, color="black", labelpad=10)
# Label the y-axis to show what the vertical axis represents
plt.ylabel("Y", fontsize=12, color="black", labelpad=10)

# Add a legend to explain the two lines
plt.legend(fontsize=12, loc="lower right", frameon=False)

plt.grid(False)
plt.gca().set_facecolor("white")
plt.savefig('../images/ConsoGlobalLorenz.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
#plt.show()

###############################################
# BOXPLOT CONSO GLOBAL
###############################################

# Plot box plot
plt.figure(figsize=(8, 4))
sns.boxplot(x=data['Conso'], color='lightgreen')
plt.title("Home Energy Consumption BoxPlot")
plt.suptitle('Distribution of a dataset')
plt.xlabel('Consumption')
plt.grid(True)
plt.savefig('../images/ConsoGlobalBoxPlot.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
#plt.show()
