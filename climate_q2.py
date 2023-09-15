import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r".\climate.csv")

years = []
co2 = []
temp = []

for year in df['Year']:
    years.append(year)
    
for CO2 in df['CO2']:
    co2.append(CO2)

for temperature in df['Temperature']:
    temp.append(temperature)

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_2.png") 
