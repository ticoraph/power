import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def gini(x):
    total = 0
    for i, xi in enumerate(x[:-1], 1):
        total += np.sum(np.abs(xi - x[i:]))
    return total / (len(x)**2 * np.mean(x))

data = pd.read_csv('csv/Conso-ByDay.csv')
#print(data.head())

#print(data.dtypes)
data['Date'] = pd.to_datetime(data['Date'],dayfirst=True)
#print(data.dtypes)

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


Consommation = data['Conso'].values
n = len(Consommation)
lorenz = np.cumsum(np.sort(Consommation)) / Consommation.sum()
lorenz = np.append([0],lorenz) # La courbe de Lorenz commence à 0
xaxis = np.linspace(0-1/n,1+1/n,n+1)
blue = "#0065D1"  # Lighter blue for the Lorenz curve
orange = "#FF5A1F"  # Bright orange for the line of perfect equality

plt.figure(figsize=(8, 6))
# Add a title to explain what the graph represents
plt.title("Lorenz Curve of Consomation", fontsize=16, color="black", pad=15)

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
plt.savefig('images/ConsoGlobalLorenz.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
plt.show()

