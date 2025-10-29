# -*- coding: utf-8 -*-
"""
Lab 5
Converted from annotated-LAB5.py.pdf
Original author: erikr
"""

# %% Lab 5 Fråga 1

import math
import ast

def solve_second_degree(seconddeglist):
    """
    Löser andragradspolynom ax^2 + bx + c = 0.
    Input-format: [c, b, a]

    Returnerar lista med reella rötter (0, 1 eller 2 st).
    Om diskriminanten < 0 returneras [].
    Om dubbelrot returneras bara ett värde.
    Om input inte är andragradspolynom (fel längd eller a=0) returneras [].
    """
    solvedseconddeglist = []

    # Kontrollera att vi har [c, b, a] och att a != 0
    if len(seconddeglist) == 3 and seconddeglist[2] != 0:
        try:
            a = seconddeglist[2]
            b = seconddeglist[1]
            c = seconddeglist[0]

            # kvadratkompletteringsform av pq-formeln som i originalet
            term = (b / (2 * a)) ** 2 - c / a
            if term < 0:
                # inga reella rötter
                return solvedseconddeglist

            x_1 = -(b / (2 * a)) + math.sqrt(term)
            x_2 = -(b / (2 * a)) - math.sqrt(term)

            solvedseconddeglist.append(x_1)
            solvedseconddeglist.append(x_2)

            # Släng dublett om de är (nästan) lika
            if abs(solvedseconddeglist[0] - solvedseconddeglist[1]) < 1e-10:
                del solvedseconddeglist[1]

            return solvedseconddeglist

        except Exception:
            # Något gick fel (t.ex. sqrt av negativt tal)
            return solvedseconddeglist

    # Inte ett andragradspolynom
    return solvedseconddeglist


# Läser fil och parametriserar innehållet
# Förväntat format i "Andragradspolynom.txt": en Python-lista, t.ex.
# [[c,b,a],[c,b,a],...]
with open('Andragradspolynom.txt', 'r') as f_in:
    FileString = f_in.read()

FileStringList = ast.literal_eval(FileString)  # polynomlistan som listor av [c,b,a]

# Lös varje polynom och spara lösningarna
solvedFileList = []
for poly in FileStringList:
    solvedElement = solve_second_degree(poly)
    solvedFileList.append(solvedElement)

# Gör listan till en enda sträng, typ "[[x1, x2], [...], ...]"
solvedStringList = list(map(str, solvedFileList))
joinedSolvedStringList = ' '.join(solvedStringList)

# Skriv lösningarna till fil
with open('Solved_Equations.txt', 'w') as f_out:
    f_out.write(joinedSolvedStringList)


# %% Lab 5 Fråga 2

import matplotlib.pyplot as plt

def fileplotter(filnamn):
    """
    Läser en fil med två rader:
        rad1: kommateckenseparerad lista av x-värden
        rad2: kommateckenseparerad lista av y-värden
    Plottar dessa, sparar en PNG som <filnamn>_plot.png.
    Returnerar 'OK' eller feltext.
    """
    try:
        filetxt = open(filnamn, 'r')
    except Exception:
        print('The file could not be opened')
        return 'Error when opening file'

    try:
        row1 = filetxt.readline()
        row2 = filetxt.readline()
        filetxt.close()

        # Om saknas någon rad
        if row1 == '' or row2 == '':
            print('Expected 2 rows but given 1')
            return 'Error when reading file'
        else:
            x_list = row1.split(',')
            y_list = row2.split(',')
    except Exception:
        print('The file could not be read')
        return 'Error when reading file'

    try:
        x_list_float = list(map(float, x_list))
        y_list_float = list(map(float, y_list))
    except Exception:
        print('The elements could not be turned into type: float')
        return 'Error when transforming to type: float'

    try:
        plt.figure()
        plt.plot(x_list_float, y_list_float)
    except Exception:
        print('Could not plot the values')
        return 'Error when plotting'

    try:
        plt.savefig(filnamn + '_plot.png')
        print('The plot is saved in files')
        return 'OK'
    except Exception:
        print('Could not save figure to file')
        return 'Error when saving figure'


# Exempelanrop (anpassa filnamn om du kör lokalt)
fileplotter('Testplot.txt')
# fileplotter('C:/Users/erikr/Downloads/Missplot1.txt')
# fileplotter('C:/Users/erikr/Downloads/Missplot2.txt')
# fileplotter('C:/Users/erikr/Downloads/Missplot3.txt')


# %% Lab 5 Fråga 3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
Antagen filstruktur i CO2.csv
(den pdf:ade koden försökte läsa en CSV som egentligen har semikolon som
fältseparator och dessutom en header som är felaktigt sammanslagen till
en kolumn, sen dela upp den med .str.split(';'))

Vi gör det robust genom att:
1. läsa filen rått med sep=';' och header=None
2. tolka första raden som header
3. skapa snygg DataFrame
"""

# Läs hela filen som semikolonseparerad, utan att låta pandas gissa header
raw = pd.read_csv('CO2.csv', sep=';', header=None, dtype=str)

# Första rad = kolumnnamn
header = raw.iloc[0].tolist()
data = raw.iloc[1:].reset_index(drop=True)
data.columns = header

# Nu bör vi ha kolumner som: 'Stat','CO2','BNP/capita','Befolkningsmängd','Region'
df = data.copy()

# Parametriserar Sverige, tar reda på index och tar bort Sverige ur DataFrame
Sweden = df[df["Stat"] == 'Sweden']
df = df.drop(Sweden.index)

# Gör Sverige till sin egen lilla cirkel
Swebnp = float(Sweden['BNP/capita'].iloc[0])
Sweco2 = float(Sweden['CO2'].iloc[0])
Swepop = float(Sweden['Befolkningsmängd'].iloc[0])
Swesize = (np.sqrt(Swepop)) / 100
Swecol = 'yellow'

# Plocka ut serier
co2_series = df['CO2']
bnp_series = df['BNP/capita']
pop_series = df['Befolkningsmängd']
region_series = df['Region']

# Gör listor
co2_list_float = list(map(float, co2_series.tolist()))
bnp_list_float = list(map(float, bnp_series.tolist()))
pop_list_float = list(map(float, pop_series.tolist()))
region_list = region_series.tolist()

# Arrays
co2_arr = np.array(co2_list_float)
bnp_arr = np.array(bnp_list_float)
pop_arr = np.array(pop_list_float)

# Cirkeldiameter ~ sqrt(population)
size = (np.sqrt(pop_arr)) / 100

# Gör en färglista baserat på region
def region_to_color(region_name):
    if region_name == 'south_asia':
        return 'r'
    elif region_name == 'europe_central_asia':
        return 'b'
    elif region_name == 'middle_east_north_africa':
        return 'k'
    elif region_name == 'sub_saharan_africa':
        return 'y'
    elif region_name == 'america':
        return 'm'
    else:
        return 'g'  # east_asia_pacific eller övrigt

color_list = [region_to_color(r) for r in region_list]

# Plotta scatterdiagrammet
plt.figure()
plt.title('BNP/capita vs Emitted CO2 (Sweden in bright yellow)')
plt.xlabel('BNP per capita')
plt.ylabel('Emitted CO2')
plt.scatter(bnp_arr, co2_arr, c=color_list, s=size)
plt.scatter(Swebnp, Sweco2, c=Swecol, s=Swesize)


# %% Lab 5 Fråga 4

import numpy as np
import matplotlib.pyplot as plt

"""
Idén:
- Läs de första 1000 primtalen från en fil.
- Varje primtal skrivs som en 4-siffrig sträng, t.ex. '0002', '0037', '1021'.
- Dela upp varje sträng i (tiotal, ental) och (tusental, hundratal),
  men i koden valde de namnen x/y lite omvänt:
    x_list = sista två siffror
    y_list = första två siffror
- Plotta som scatter.

PDF-koden hade:
    prime_numbers = open('C:/Users/erikr/Downloads/primes (1).txt').read()
    prime_list = prime_numbers.split()
    while len(prime_list[i]) < 4:
        prime_list[i] = prime_list[i].zfill(4)
        i += 1
Men den loopen bryter när prime_list[i] redan är 4 tecken, så vi gör det säkrare.
"""

# Läs in primtalen (lägg filen "primes.txt" bredvid scriptet)
# Om din fil heter annorlunda, byt här.
with open('primes.txt', 'r') as f_pr:
    prime_numbers = f_pr.read()

prime_list = prime_numbers.split()

# Gör alla tal till 4-siffriga strängar med nollutfyllnad
prime_list_padded = [p.zfill(4) for p in prime_list]

# Skapa x_list = de sista två siffrorna, y_list = de första två
x_list = [int(p[2:4]) for p in prime_list_padded]
y_list = [int(p[0:2]) for p in prime_list_padded]

# Generera färger (en färg per punkt). Här: slumpa 0..255
num_points = len(prime_list_padded)
color = list(np.random.choice(range(256), size=num_points))

# Storlek på punkterna
size = 0.5

plt.figure()
plt.title('Tusental, hundratal, tiotal och ental i de tusen första primtalen')
plt.ylabel('Ental och tiotal i de 1000 första primtalen')
plt.xlabel('Tusental och hundratal i de 1000 första primtalen')
plt.scatter(x_list, y_list, c=color, s=size, alpha=1.0)

# Done.
if __name__ == "__main__":
    # You can optionally plt.show() here if running interactively
    plt.show()
