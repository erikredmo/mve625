# -*- coding: utf-8 -*-
"""
tenta.py
Converted from annotated-tenta.py.pdf

Original header:
Created on Tue Oct 20 14:52:42 2020
@author: erikr
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Öppnar och "dataframear" csvfil
# Förväntade kolumner i CO2extra.csv:
# country ; CO2 2000 ; CO2 2018 ; BNP/capita ; Befolkningsmängd ; Region ; Medellivslängd
df = pd.read_csv('CO2extra.csv', sep=';')

# Skapar listor av kolonner i df
land_list = df['country'].tolist()
co22000_list = df['CO2 2000'].tolist()
co22018_list = df['CO2 2018'].tolist()
bnpcap_list = df['BNP/capita'].tolist()
befolk_list = df['Befolkningsmängd'].tolist()
region_list = df['Region'].tolist()
medel_list = df['Medellivslängd'].tolist()

# Gör varje lista med tal i till arrays med floats
co22000_arr = np.array(list(map(float, co22000_list)))
co22018_arr = np.array(list(map(float, co22018_list)))
bnpcap_arr = np.array(list(map(float, bnpcap_list)))
befolk_arr = np.array(list(map(float, befolk_list)))
medel_arr = np.array(list(map(float, medel_list)))

# Logaritmerar bnp/capita (naturliga logaritmen i originalet)
bnpcap_arr_log = np.log(bnpcap_arr)

# Bestämmer storleken på cirklarna (proportionell mot roten ur befolkningen)
size = (np.sqrt(befolk_arr)) / 100

# Skillnad mellan 2018 och 2000
increase_arr = co22018_arr - co22000_arr
percent_increase_arr = (increase_arr / co22000_arr) * 100
percent_list = percent_increase_arr.tolist()

# Gör en färglista kopplad till ökning/minskning
# intervall:
#   < -30%        -> 'g' (grön, kraftig minskning)
#   [-30, 0)      -> 'b' (blå, minskning)
#   [0, 30)       -> 'y' (gul, måttlig ökning)
#   [30, 100)     -> 'r' (röd, stor ökning)
#   >= 100        -> 'k' (svart, extrem ökning)
color_list = []
for val in percent_increase_arr:
    if val < -30:
        color_list.append('g')
    elif -30 <= val < 0:
        color_list.append('b')
    elif 0 <= val < 30:
        color_list.append('y')
    elif 30 <= val < 100:
        color_list.append('r')
    else:
        color_list.append('k')

# Plottar scatterploten
plt.figure()
plt.title('BNP/capita vs koldioxidutsläpp 2018')
plt.xlabel('BNP per capita (ln-skala)')
plt.ylabel('Koldioxidutsläpp per capita 2018')
plt.scatter(bnpcap_arr_log, co22018_arr, c=color_list, s=size, alpha=0.6)
plt.tight_layout()

# Sparar som PNG
plt.savefig("BNPco2.png")

# Lägger till ny kolonn i dataframe för att kunna göra nlargest/nsmallest
df['Ökning'] = percent_list

# Lägger till en "fulkolonn" till för att kunna få med procenttecknet i printen
df['Ökning i procent'] = df['Ökning'].astype(str) + ' %'

# Gör dataframes av 10 högsta/lägsta värdena gällande ökning
df_largest = df.nlargest(10, 'Ökning')
df_smallest = df.nsmallest(10, 'Ökning')

# Ändrar index till rank istället (1..10)
new_index = range(1, 11)
df_largest.index = new_index
df_smallest.index = new_index

# Printar rank, land och ökning i procent
print("Störst ökning (topp 10):")
print(df_largest[["country", "Ökning i procent"]])
print()
print("Minst / negativ ökning (botten 10):")
print(df_smallest[["country", "Ökning i procent"]])
