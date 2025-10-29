# -*- coding: utf-8 -*-
"""
Created on Tue Sep 1 13:26:10 2020
@author: erikr
"""
#%%
import math
import numpy
#Låter användaren mata in tal och gör om dem till heltal
a = int(input("Mata in första heltalet: "))
b = int(input("Mata in andra heltalet: "))
c = int(input("Mata in tredje heltalet: "))
x = [a, b, c]

maxvärde = max(x)
minvärde = min(x)
medelnp = numpy.mean(x)
#medelvärde = (a+b+c)/len(x) #Räknar ut medelvärdet med hjälp av antal element i x
print("Maxvärdet är ", maxvärde)
print("Minvärdet är ", minvärde)
#print("Medelvärdet är ",medelvärde)
print(medelnp)
#%%
import math
#Välj godtyckligt n för att hitta andra lösningar till de ekvationer med oändligt många lösningar
n = int(input("Välj godtyckligt heltal n: "))
x1 = round(math.asin(0.4)+(2*math.pi*n), 4)
x2 = round(math.atan(5)+(math.pi*n), 4)
print("Ur funktion 1 fås x1 = ", x1)
print("Ur funktion 2 fås x2 = ", x2)
# x3 = round(math.acos(3)*n, 4) arccos(3) ej definierad!
x4 = round(math.sqrt((math.e**3)/2), 4)
print("Ur funktion 4 fås x4 = ", x4)
u1 = 5/2 + math.sqrt(1/4)
u2 = 5/2 - math.sqrt(1/4)
x51 = round(math.log(u1), 4)
x52 = round(math.log(u2), 4)
print("Ur funktion 5 fås x51 = ", x51, "och x52 ", x52)
#%%
import math
r = float(input("Mata in radien: "))
omkrets = 2*r*math.pi
area = (r**2)*math.pi
volym = (4*math.pi*r**3)/3
ytarea = 4*math.pi*(r**2)
print("Omkretsen av cirkeln är ", omkrets)
print("Arean av cirkeln är ", area)
print("Volymen av klotet ", volym)
print("Ytarean av sfären är ", ytarea)
#%%
import math
x = int(input("För punkten p i planet, välj x-koordinat: "))
y = int(input("För punkten p i planet, välj y-koordinat: "))
r = math.sqrt(x**2 + y**2)
if x == 0 and y > 0: #Specialfall 90 grader
    phi = math.pi/2
elif y == 0 and x < 0: #Specialfall 180 grader
    phi = math.pi
elif x == 0 and y < 0: #Specialfall 270 grader
    phi = (3*math.pi)/2
elif x < 0 and y < 0: #Hanterar tredje kvadranten
    phi = math.pi + math.atan(y/x)
elif y < 0: #Hanterar fjärde kvadranten
    phi = 2*math.pi + math.atan(y/x)
else: #Hanterar första och andra kvadranterna
    phi = math.atan(y/x)
print("De polära koordinaterna för p är r =", r, " och phi =", phi)
#%%
from sympy import *
x = symbols('x')
ekv1 = sin(x)/x
print("Ekvation 1 : {}".format(ekv1))
gv1 = limit(ekv1, x, 0)
print("Gränsvärdet när x går mot 0 är {}".format(gv1))
ekv2 = (log(1+x))/x
print("Ekvation 2 : {}".format(ekv2))
gv2 = limit(ekv2, x, 0)
print("Gränsvärdet när x går mot 0 är : {}".format(gv2))
ekv3 = sin(1/x)
print("Ekvation 3 : {}".format(ekv3))
gv3 = limit(ekv3, x, 0)
print("Gränsvärdet när x går mot 0 är : {}".format(gv3)) #AccumBounds(-1,1) tyder på divergens
ekv4 = (1-cos(x))/x**2
print("Ekvation 4 : {}".format(ekv4))
gv4 = limit(ekv4, x, 0)
print("Gränsvärdet när x går mot 0 är : {}".format(gv4))