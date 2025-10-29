# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 21:06:59 2020
@author: erikr
"""
#%% Lab 3 Fråga 1
from math import sqrt
def kvadratrot(n):
    if n == 0:
        print("Roten ur 0 är 0")
    else:
        try:
            xgammal = 1
            xny = 1/2
            räknare = 0 #i räknar antal iterationer (gånger som whileloopenupprepas)
            if n < 0:
                print('Måste vara ett positivt tal!')
                return -1
            while abs(xny - xgammal) >= 10e-10:
                xtemp = xny
                xny = (xgammal + n/xgammal) / 2
                xgammal = xtemp
                räknare += 1
            print('Roten ur', n, ' är', xny, ' och antalet iterationer blev',räknare)
            print("Skillnaden är :", abs(sqrt(n) - xny))
            return xny
        except:
            return -1

n = input("Mata in ett positiv tal: ")
try:
    n = float(n)
except:
    print("Måste vara ett tal!")
kvadratrot(n)
#%% Lab 3 Fråga 2
#import numpy as np
import matplotlib.pyplot as plt
def glid_medvärde(k, n):
    i = 0
    glid_medvärde_lista = []
    while i < len(k) - n + 1:
        fönster = k[i : i + n] # Anger storleken på fönstret
        fönster_medel = sum(fönster) / float(n)
        glid_medvärde_lista.append(fönster_medel)
        i += 1
    return glid_medvärde_lista

döda = [1,0,1,1,2,2,1,6,7,9,8,11,11,21,22,31,32,35,38,45,48,53,70,80,70,85,90,84,115,86,90,
        103,97,85,91,115,111,82,86,88,84,62,77,86,89,73,75,73,82,84,78,78,73,75,84,72,73,80,
        60,69,74,64,61,50,46,58,49,53,61,41,53,54,56,56,44,42,28,39,40,40,39,45,40,37,26,45,
        38,31,33,38,33,40,36,30,33,27,31,28,33,29,29,29,21,21,25,22,24,11,14,22,18,21,17,15,
        8,15,9,16,12,11,15,14,10,9,14,8,6,7,7,11,8,7,7,6,5,3,1,2,6,5,2,0,3,3,1,4,2,3,4,3,1,4,
        2,4,3,6,2,1,0,3,5,1,2,5,1,3,1,1,2,1,1,1,3,1,3,3,2,0,0,2,1,0,0,0]
sjuka = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,8,3,0,5,13,30,25,59,33,46,101,98,196,
         151,152,71,69,83,119,145,143,180,136,118,182,230,314,286,365,300,280,416,475,486,554,
         601,357,340,389,738,654,645,454,395,464,437,479,604,623,688,532,388,461,707,722,758,
         780,473,300,563,742,798,635,532,299,261,476,657,745,784,700,509,279,455,754,698,657,
         688,358,259,430,666,808,610,532,403,210,491,746,800,774,773,432,265,648,901,1046,1039,
         1146,780,462,677,936,1437,1293,1329,1032,418,685,1209,1457,1494,1209,698,321,800,1310,
         1698,1279,1204,755,415,727,803,684,687,694,364,315,251,278,533,334,369,308,106,170,312,
         287,268,284,191,110,131,226,297,220,262,138,42,71,283,301,302,258,303,38,165,333,425,
         378,380,260,73,196,417,444,363,344,226,63,174,314,351,333,298,160,57,174,223,244,202,
         179,131,48,162,172,213,286,262,171,67,185,239,314,201]
#dödaarr = np.array(döda)
#sjukaarr = np.array(sjuka)
n = 7
dödlista = glid_medvärde(döda, n)
sjuklista = glid_medvärde(sjuka, n)
plt.plot(dödlista)
plt.plot(sjuklista)
plt.legend(['Antalet döda', 'Antalet insjukna'])
#k_string = input("Skriv in din lista, separera varje element med mellanslag: ")
#k_string_list = k_string.split()
#k = [float(i) for i in k_string_list]
#n = int(input("Hur stort ska fönstret vara? "))
#print(glid_medvärde(k, n))
#%% Lab 3 Fråga 3
import numpy as np
def standardavv(lista):
    medelvärde = np.sum(lista)/len(lista)
    arr = lista - medelvärde
    upphöjdarr = arr**2
    medelupphöjdarr = np.sum(upphöjdarr)/len(lista)
    standard = np.sqrt(medelupphöjdarr)
    print("Standardavvikelsen är: ", standard)
    templista = [4.7,5.8,4.6,6.2,5.1,6.4,5.7,4.9,6.2,5.7,6.4,5.1,5.1,5.3,5.6,4.7,5.0,
                 7.3,5.2,7.6,6.2,5.3,5.6,7.7,5.6,6.5,4.8,6.8,4.2,4.4,4.2,5.5,4.4,6.8,
                 6.1,7.4,5.7,6.3,7.6,4.7,6.2,6.8,6.9,4.1,4.9,5.8,5.5,4.7,4.7,4.0,5.3,
                 5.5,5.3,4.7,5.0,6.6,3.9,5.7,4.3,5.7,4.8,5.6,6.6,6.9,4.6,5.5,7.5,5.7,
                 6.6,6.2,7.2,5.8,5.3,3.5,4.9,5.4,5.4,5.7,6.6,5.5,4.9,4.7,3.8,5.2,5.2,
                 5.6,6.4,5.7,4.0,5.0,6.4,5.4,5.6,5.0,5.3,5.9,6.0,5.5,6.4,4.8,4.6,6.6,
                 6.9,6.6,4.9,5.5,4.6,6.7,4.5,5.5,5.4,3.2,6.4,5.6,5.1,3.8,6.9,6.4,5.9,
                 4.2,4.8,4.6,6.0,4.6,5.5,3.9,6.5,5.7,5.7,4.8,5.8,5.7,3.7,5.5,6.0,5.8,
                 4.7,4.7,6.7,5.4,6.4,6.0,6.1,5.3,5.3,6.2,3.8,6.0,5.2,6.0,6.4,5.3,5.6,
                 5.0,6.5,6.7,5.6,6.5,7.1,4.3,5.5,5.1,5.9,5.2,6.6,6.6,4.9,4.8,5.6,6.0,
                 5.5,5.4,5.1,5.4,7.2,4.8,6.3,6.1,7.8,6.6,6.7,6.9,7.7,6.8,4.4,4.3,4.1,
                 7.3,6.6,6.5,6.2,5.7,6.5,7.5,6.5,6.4,5.1,7.2,5.8,5.5,4.5,5.9,5.2,7.1,
                 5.9,6.9,5.0,5.3,6.0,5.0,5.1,6.4,5.8,5.7,4.8,6.2,6.9,6.6,6.9,7.7,5.5,
                 5.7,5.2,5.2,5.3,5.3,6.3,6.8,6.6,4.1,5.5,4.2,6.2,7.7,7.6,6.6,7.2,6.3,
                 6.6,6.4,5.7,7.0,6.2,7.5,7.7,6.8,7.4,7.0,6.9,7.2,7.7,7.4,7.8,6.9,5.3,
                 7.8,6.5,7.1,8.1,8.0,7.4,7.2,8.1,7.8]
    temparr = np.array(templista)
    standardavv(temparr)

#%% Lab 3 Fråga 4
import numpy as np
def korsa_x_axeln(k, m):
    if k == 0:
        return "Inget svar"
    else:
        return -m/k

k_string = input("Skriv in din lista med k-värden, separera varje element medmellanslag: ")
m_string = input("Skriv in din lista med m-värden, separera varje element medmellanslag: ")
k_string_list = k_string.split()
m_string_list = m_string.split()
k = [float(i) for i in k_string_list]
m = [float(i) for i in m_string_list]
try:
    korsa_x_axeln = np.frompyfunc(korsa_x_axeln, 2, 1)
    print(korsa_x_axeln(k, m))
    print(type(korsa_x_axeln))
except:
    print("Du måste ha samma antal k-värden som m-värden!")

#%% Lab 3 Fråga 5
import numpy as np
def equalpol(pol1,pol2):
    pol1 = np.array(pol1)
    pol2 = np.array(pol2)
    if np.array_equal(pol1,pol2):
        return True
    else:
        return False
def addpol(pol1,pol2):
    while len(pol1) < len(pol2):
        pol1 = np.append(pol1, 0)
    while len(pol2) < len(pol1):
        pol2 = np.append(pol2,0)
    pol1 = np.array(pol1)
    pol2 = np.array(pol2)
    polsvar = np.add(pol1,pol2)
    return polsvar
def multpol(pol1,pol2):
    pol1 = np.array(pol1)
    pol2 = np.array(pol2)
    multadpol = np.polymul(pol1,pol2)
    return multadpol
def derivatepol(pol1):
    poltoderivate = np.copy(pol1)
    derivated = np.polyder(poltoderivate)
    return derivated
pol1_string = input("Skriv in koefficienterna för det första polynomet och det som ska deriveras, separera med mellanslag: ")
pol2_string = input("Skriv in koefficienterna för det andra polynomet, separera medmellanslag: ")
pol1_string_list = pol1_string.split()
pol2_string_list = pol2_string.split()
pol1 = [float(i) for i in pol1_string_list]

pol2 = [float(i) for i in pol2_string_list]
print("De två polynomen adderade: ", (addpol(pol1,pol2))) # Första elementet ärkonstant, sista högsta grad
print("De två polynomen multiplicerade: ", (multpol(pol1,pol2))) # Första elementetär konstant, sista högsta grad
print("Derivatan av det första polynomet som skrevs in: ", (derivatepol(pol1)))
#Första elementet indikerar högsta graden
print("Är polynomen samma polynom? ", (equalpol(pol1,pol2)))
print(equalpol(derivatepol(multpol(pol1, pol2)), addpol(multpol(pol1,
derivatepol(pol2)), multpol(derivatepol(pol1), pol2))))
print(derivatepol(multpol(pol1, pol2)))
print(addpol(multpol(pol1, derivatepol(pol2)), multpol(derivatepol(pol1), pol2)))