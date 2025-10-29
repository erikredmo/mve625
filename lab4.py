# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 18:03:45 2020
@author: erikr
"""
#%% Lab 4 Fråga 1
import numpy as np
import matplotlib.pyplot as plt
övrigt_ovan_fjällnära_gräns = np.array([96400,200,127100,50900,2700,100,1000,2000,0,100,200,0,800,0,0,0,0,0,0,23500,1000,0])
övrigt_nedan_fjällnära_gräns = np.array([13800,3300,22100,2600,7000,900,4200,600,1300,800,2300,1200,2700,900,1100,2300,1000,2800,1600,1200,2200,1000])
öppen_våtmark = np.array([38600,2300,22800,9100,13800,2700,29300,2600,3900,1400,6100,2300,11500,2200,3300,800,4400,2300,3500,4700,8300,6900])
skogsmark_inklusive_låg_fjällskog = np.array([124800,5600,47800,32600,60900,9300,63100,10200,10000,10800,18700,16700,39200,12600,10500,10300,15700,14700,18800,25500,39300,18100])
sjöar_och_vattendrag =np.array([172000,2200,321300,17700,167200,7500,15900,1000,1200,900,2000,700,2300,900,400,1200,1000,1900,1500,3700,3300,2500])
hav =np.array([14000,1700,68100,12900,13100,34400,5100,300,300,200,69000,4900,1400,135000,2300,58100,400,3200,1302800,2700,15400,3800])
totalperår = övrigt_ovan_fjällnära_gräns + övrigt_nedan_fjällnära_gräns +öppen_våtmark + skogsmark_inklusive_låg_fjällskog + sjöar_och_vattendrag + havår = range(1998,2020)
plt.plot(år, totalperår, 'k-h', label='Total')
plt.plot(år, övrigt_ovan_fjällnära_gräns, 'b', label='Övrigt')
plt.title('Skyddad natur i Sverige mätt i hektar 1986-2019')
plt.xlabel('Årtal')
plt.ylabel('Hektar')
plt.legend()
#%% Lab 4 Fråga 2
import matplotlib.pyplot as plt
import numpy as np
def plotta_polynom(polynom, start, slut):
    grad = len(polynom) - 1
    antalpunkter = 2 + grad * 5 * (slut - start)
    polynom.reverse() #polyval väljer första element som högsta grad
    x = np.linspace(start, slut, antalpunkter)
    y = np.polyval(polynom, x)
    return plt.plot(x, y,'k-')

plotta_polynom([0, 0, 1], -1, 1)
#%% Lab 4 Fråga 3
import matplotlib.pyplot as plt
kraftkälla86 = ['Vattenkraft','Pumpkraft','Kärnkraft','Konventionell värmekraft','Importerad el']
kraftkälla18 = ['Vattenkraft','Pumpkraft','Kärnkraft','Konventionellvärmekraft','Vindkraft', 'Solkraft', 'Import']
år_1986 = [60933,567,69951,7200,1835]
år_2018 = [62150,100,68549,15572,16623,391,12202]
plt.subplot(1,2,1)
plt.pie(år_1986, labels=kraftkälla86)
plt.title('Bruttotillförsel av el-energi i Sverige 1986')
plt.subplot(1,2,2)
plt.pie(år_2018, labels=kraftkälla18)
plt.title('Bruttotillförsel av el-energi i Sverige 2018')
plt.subplots_adjust(right = 1.7)
#%% Lab 4 Fråga 4
import matplotlib.pyplot as plt
import numpy as np
import math
n = input('Skriv in ett positiv heltal: ')
test = False
# Får användaren att mata in ett positivt heltal
while test == False:
    try:
        n = float(n)
        if n > 0:
            test = True
        else:
            n = input('Det där var ett negativt tal, skriv in ett positivt heltal:')
    except:
        n = input('Det där var inget tal, skriv in ett positivt heltal: ')
# Utvecklar Maclaurin
def Maclaurin(x,n):
    i = 0
    mc = 0
    x = np.array(x)
    while i <= n/2:
        mc = mc + (-1)**i * (x)**(2*i)/(math.factorial(2*i))
        i += 1
    return mc

x = np.linspace(-np.pi, np.pi, 1000)
plt.plot(x, np.cos(x), 'b-', label='Cosinus') # Plotta cosinus från 0 till 2pi medgröna streck
plt.plot(x, Maclaurin(x,n), 'm--', label='Maclaurin för cosinus')
plt.title('Cosinus & Maclaurinapproximation för cosinus')
plt.legend()
#%% Lab 4 Fråga 5
import numpy as np
import matplotlib.pyplot as plt
south_asia = 'r'
europe_central_asia = 'b'
middle_east_north_africa = 'k'
sub_saharan_africa = 'y'
america = 'm'
east_asia_pacific = 'g'
Land = ["Afghanistan","Albania","Algeria","Angola","Antigua and Barbuda","Argentina","Armenia","Australia","Austria","Azerbaijan","Bahamas",
        "Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bolivia","Bosnia and Herzegovina","Botswana","Brazil","Brunei",
        "Bulgaria","BurkinaFaso","Burundi","Cambodia","Cameroon","Canada","Cape Verde","Central AfricanRepublic","Chad","Chile","China","Colombia",
        "Comoros","Congo. Dem. Rep.","Congo.Rep.","Costa Rica","Cote d'Ivoire","Croatia","Cyprus","CzechRepublic","Denmark","Dominican Republic",
        "Ecuador","Egypt","ElSalvador","EquatorialGuinea","Estonia","Ethiopia","Fiji","Finland","France","Gabon","Gambia","Georgia","Germany",
        "Ghana","Greece","Grenada","Guatemala","Guinea","Guinea-Bissau","Guyana","Haiti","Honduras","Hungary","Iceland","India","Indonesia","Iraq",
        "Ireland","Israel","Italy","Jamaica","Japan","Jordan","Kazakhstan","Kenya","Kiribati","Kuwait","KyrgyzRepublic","Lao","Latvia","Lebanon",
        "Lesotho","Liberia","Libya","Lithuania","Luxembourg","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Mauritania","Mauritius",
        "Mexico","Moldova","Mongolia","Montenegro","Morocco","Mozambique","Myanmar","Namibia","Nepal","Netherlands","New Zealand","Nicaragua","Niger",
        "Nigeria","NorthMacedonia","Norway","Oman","Pakistan","Panama","Papua NewGuinea","Paraguay","Peru","Philippines","Poland","Portugal","Qatar",
        "Romania","Russia","Rwanda","Samoa","Sao Tome and Principe","SaudiArabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","SlovakRepublic",
        "Slovenia","Solomon Islands","South Africa","South Korea","Spain","SriLanka","St. Lucia","St. Vincent and theGrenadines","Sudan","Suriname","Sweden",
        "Switzerland","Tajikistan","Tanzania","Thailand","Timor-Leste","Togo","Trinidad andTobago","Tunisia","Turkey","Uganda","Ukraine","United Arab Emirates","UnitedKingdom","UnitedStates","Uruguay","Uzbekistan","Vanuatu","Vietnam","Zambia","Zimbabwe"]
import numpy as np
import matplotlib.pyplot as plt

# --- Data arrays ---
befolkArr = np.array([
    38000000,2880000,43100000,31800000,97100,44800000,2960000,25200000,8960000,
    10000000,389000,1640000,163000000,287000,9450000,11500000,390000,11800000,
    11500000,3300000,2300000,211000000,433000,7000000,20300000,11500000,16500000,
    25900000,37400000,550000,4750000,15900000,19000000,1430000000,50300000,851000,
    86800000,5380000,5050000,25700000,4130000,1200000,10700000,5770000,10700000,
    17400000,100000000,6450000,1360000,1330000,112000000,890000,5530000,65100000,
    2170000,2350000,4000000,83500000,30400000,10500000,112000,17600000,12800000,
    1920000,783000,11300000,9750000,9680000,339000,1370000000,271000000,39300000,
    4880000,8520000,60600000,2950000,127000000,10100000,18600000,52600000,118000,
    4210000,6420000,7170000,1910000,6860000,2130000,4940000,6780000,2760000,616000,
    27000000,18600000,31900000,531000,19700000,440000,4530000,1270000,128000000,
    4040000,3230000,628000,36500000,30400000,54000000,2490000,28600000,17100000,
    4780000,6550000,23300000,201000000,2080000,5380000,4970000,217000000,4250000,
    8780000,7040000,32500000,108000000,37900000,10200000,2830000,19400000,146000000,
    12600000,197000,215000,34300000,16300000,8770000,97700,7810000,5800000,5460000,
    2080000,670000,58600000,51200000,46700000,21300000,183000,111000,42800000,581000,
    10000000,8590000,9320000,58000000,69600000,1290000,8080000,1390000,11700000,
    83400000,44300000,44000000,9770000,67500000,329000000,3460000,33000000,300000,
    96500000,17900000,14600000
])

bnpArr = np.array([
    571,5210,4710,3100,15700,9730,4730,57100,50700,5880,27500,20900,1290,16100,6680,
    47500,4150,1260,2580,6240,8090,11100,32300,9030,822,208,1270,1520,51600,3910,384,
    814,15100,8250,7840,1410,424,2610,10000,1740,16500,32100,23800,65100,8010,5100,
    3010,3570,9240,20700,602,4810,49200,44300,9130,809,4990,47600,1880,24000,9330,
    3410,921,635,4160,714,2240,17500,51300,2170,4450,5590,79700,35300,35600,4870,
    49200,3280,11500,1240,1790,32700,1120,1840,16700,5860,1380,516,8120,18400,111000,
    500,524,12500,8210,793,28900,1760,10900,10300,3720,4350,8550,3400,587,1610,5770,
    859,55700,39000,1760,558,2390,5630,92600,15000,1190,11900,2510,5310,6490,3340,
    17400,24600,62000,12100,12000,905,3860,1300,20500,1580,7210,15000,488,58800,
    21000,27200,1480,7350,28600,33300,4010,9350,6850,1720,7970,58000,79400,1120,985,
    6500,860,696,15100,4410,15000,957,3220,41400,43700,55700,14600,2460,2870,2080,
    1660,1180
])

Region = [
    "south_asia","europe_central_asia","middle_east_north_africa","sub_saharan_africa","america",
    "america","europe_central_asia","east_asia_pacific","europe_central_asia","europe_central_asia",
    "america","middle_east_north_africa","south_asia","america","europe_central_asia",
    "europe_central_asia","america","sub_saharan_africa","america","europe_central_asia",
    "sub_saharan_africa","america","east_asia_pacific","europe_central_asia","sub_saharan_africa",
    "sub_saharan_africa","east_asia_pacific","sub_saharan_africa","america","sub_saharan_africa",
    "sub_saharan_africa","sub_saharan_africa","america","east_asia_pacific","america",
    "sub_saharan_africa","sub_saharan_africa","sub_saharan_africa","america","sub_saharan_africa",
    "europe_central_asia","europe_central_asia","europe_central_asia","europe_central_asia","america",
    "america","middle_east_north_africa","america","sub_saharan_africa","europe_central_asia",
    "sub_saharan_africa","east_asia_pacific","europe_central_asia","europe_central_asia",
    "sub_saharan_africa","sub_saharan_africa","europe_central_asia","europe_central_asia",
    "sub_saharan_africa","europe_central_asia","america","america","sub_saharan_africa",
    "sub_saharan_africa","america","america","america","europe_central_asia","europe_central_asia",
    "south_asia","east_asia_pacific","middle_east_north_africa","europe_central_asia",
    "middle_east_north_africa","europe_central_asia","america","east_asia_pacific",
    "middle_east_north_africa","europe_central_asia","sub_saharan_africa","east_asia_pacific",
    "middle_east_north_africa","europe_central_asia","east_asia_pacific","europe_central_asia",
    "middle_east_north_africa","sub_saharan_africa","sub_saharan_africa","middle_east_north_africa",
    "europe_central_asia","europe_central_asia","sub_saharan_africa","sub_saharan_africa",
    "east_asia_pacific","south_asia","sub_saharan_africa","europe_central_asia",
    "sub_saharan_africa","sub_saharan_africa","america","europe_central_asia","east_asia_pacific",
    "europe_central_asia","middle_east_north_africa","sub_saharan_africa","east_asia_pacific",
    "sub_saharan_africa","south_asia","europe_central_asia","east_asia_pacific","america",
    "sub_saharan_africa","sub_saharan_africa","europe_central_asia","europe_central_asia",
    "middle_east_north_africa","south_asia","america","east_asia_pacific","america","america",
    "east_asia_pacific","europe_central_asia","europe_central_asia","middle_east_north_africa",
    "europe_central_asia","europe_central_asia","sub_saharan_africa","east_asia_pacific",
    "sub_saharan_africa","middle_east_north_africa","sub_saharan_africa","europe_central_asia",
    "sub_saharan_africa","sub_saharan_africa","east_asia_pacific","europe_central_asia",
    "europe_central_asia","east_asia_pacific","sub_saharan_africa","east_asia_pacific",
    "europe_central_asia","south_asia","america","america","sub_saharan_africa","america",
    "europe_central_asia","europe_central_asia","europe_central_asia","sub_saharan_africa",
    "east_asia_pacific","east_asia_pacific","sub_saharan_africa","america",
    "middle_east_north_africa","europe_central_asia","sub_saharan_africa","europe_central_asia",
    "middle_east_north_africa","europe_central_asia","america","america","europe_central_asia",
    "east_asia_pacific","east_asia_pacific","sub_saharan_africa","sub_saharan_africa"
]

medelArr = np.array([
    64.1,78.5,78.1,65,77.3,77,75.9,82.7,82,71.1,74.1,79.8,73.7,77.3,74.5,81.7,74.4,
    65.3,73.3,77,69.8,75.9,75.6,75.1,62.5,62.3,70.4,63.8,82.2,76.2,52.9,60.6,80,77.5,
    80.5,69.1,63,63.3,79.8,63.3,78.8,82,79.5,81,73.5,77.2,71,74.5,66.3,78.5,69.1,68.3,
    81.8,83.1,69,66.4,73.2,80.9,66.1,81.3,74.1,73.1,61.6,60.7,69.5,65.7,74.3,77.2,83,
    69.5,71.9,77.1,82.3,83.3,83.5,74.9,84.5,79.6,72.8,66.7,62.9,83.3,73,68.2,75.4,
    78.1,56.1,65.2,73.3,75.4,82,64.2,64.2,75,82.1,62.9,81.3,71,75,75.6,73.1,69.3,76.7,
    74.4,59.9,69.1,67.2,71.5,81.8,81.9,79.2,63.2,65.2,76.8,82.6,77.6,67.2,79.7,58.9,
    76.4,80.8,70,78.4,81.8,80.5,75.4,72.5,69.1,73.2,67.3,77.1,68.6,76,73.8,61.3,85.1,
    77.7,81.4,68.9,66.9,83,83.3,77.8,75.8,72.5,70.8,72.3,82.8,84.3,70.8,67.7,78.6,71.3,
    65,74.5,78.7,79.5,66.6,70.8,73.6,81.1,78.6,77.3,70.7,65,74.7,64,62
])

# --- Computations and plot ---
bnpcapitalog = np.log2(bnpArr)
storlek = (np.sqrt(befolkArr)) / 100

plt.figure(figsize=(10,6))
plt.xlabel('BNP per capita (tvålogaritmerad), USD')
plt.ylabel('Medellivslängd (år)')
plt.title('BNP per capita & medellivslängd för världens länder')

plt.scatter(bnpcapitalog, medelArr, c=np.arange(len(Region)), s=storlek, cmap='viridis', alpha=0.7)
plt.colorbar(label='Region index (färgkodad)')
plt.show()
