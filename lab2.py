# -*- coding: utf-8 -*-
"""
Created on Tue Sep 8 13:21:30 2020
@author: erikr
"""
import math
print('Skriv in längden av sidan a: ')
a = float(input())
while a <= 0:
    print('Skriv in en positiv längd a: ')
    a = float(input())
    print('Skriv in längden av sidan b: ')
    b = float(input())
while b <= 0:
    print('Skriv in en positiv längd b: ')
    b = float(input())
    print('Skriv in vinkeln mellan a och b i grader (mellan 0 och 180 grader): ')
    v = float(input())
while v <= 0 or v >= 180:
    print('Ge relevant vinkel (mellan 0 och 180 grader: ')
    v = float(input())
    v = math.radians(v)
    hyp = math.sqrt((a**2)+(b**2)-(2*a*b)*math.cos(v))
if a != b and a != hyp and b != hyp:
    print('Triangeln är oliksidig')
elif abs(a-b) < 10**-10 and abs(a-hyp) < 10**-10 and abs(b-hyp) < 10**-10:
    print('Triangeln är liksidig')
else:
    print('Triangeln är likbent')
#%%
import math
print('Skriv in ett positivt heltal n: ')
n = int(input())
while n <= 0:
    print('Skriv in ett positivt heltal n: ')
    n = int(input())
    i = 1
s1 = 0.0
s2 = 0.0
for i in range(1, n+1):
    s1 = s1 + 1/i
    s2 = math.log(i)
diff = s1 - s2
print(s1)
print(diff) #Differensen konvergerar mot 0.5772161, med andra ord mot Euler- Mascheronis konstant. Dock divergerar både 1/n och ln(n)
#%%
import math
print('Skriv in ett litet positivt tal epsilon: ')
epsilon = abs(float(input()))
summa = 0.0
i = 0
while abs((math.pi**2/6)-summa) > epsilon:
    i += 1
    summa = summa + 1/(i**2)
print('Antal termer som behövs är: ', i)
print('Den harmoniska serien når summan: ', summa)
#%%
import math
#Skapar lista och lägger till undantagen 0 och 1
fibonacci = [0,1]
for i in range(2, 100):
#nästa element = summan av de föregående två numren
    nästaElement = fibonacci[i-1] + fibonacci[i-2]
#lägg till elementen till listan
    fibonacci.append(nästaElement)
    fibonaccimodtvå = [0,1]
for i in range(2, len(fibonacci)):
    nästaElement = (fibonacci[i-1] + fibonacci[i-2])%2
    fibonaccimodtvå.append(nästaElement)
    fibonaccimodtre = [0,1]
for i in range(2, len(fibonacci)):
    nästaElement = (fibonacci[i-1] + fibonacci[i-2])%3
    fibonaccimodtre.append(nästaElement)
    fibonaccimodfem = [0,1]
for i in range(2, len(fibonacci)):
    nästaElement = (fibonacci[i-1] + fibonacci[i-2])%5
    fibonaccimodfem.append(nästaElement)

fibonaccimodsju = [0,1]
for i in range(2, len(fibonacci)):
    nästaElement = (fibonacci[i-1] + fibonacci[i-2])%7
    fibonaccimodsju.append(nästaElement)
print(fibonacci)
print(fibonaccimodtvå)
print(fibonaccimodtre)
print(fibonaccimodfem)
print(fibonaccimodsju)
print(len(fibonacci))
print(len(fibonaccimodtvå))
print(len(fibonaccimodtre))
print(len(fibonaccimodfem))
print(len(fibonaccimodsju))
# Resterna upprepar sig, fast med olika mönster i de olika "modulu"-listorna.
# I den första: 1, 1, 0
# I den andra: 0, 1, 1, 2,0, 2, 2, 1
# I den tredje: 0, 1, 1, 2, 3, 0, 3 ,3 ,1, 4, 0, 4, 4, 3, 2, 0, 2, 2, 4, 1, 0
# I den fjärde: 0, 1, 1, 2, 3, 5, 1, 6, 0, 6, 6, 5, 4, 2, 6, 1, 0, 1, 1, 2, 3, 5
#%%
import math
templista = [4.7,5.8,4.6,6.2,5.1,6.4,5.7,4.9,6.2,5.7,6.4,5.1,5.1,5.3,5.6,4.7,5.0,7.3,5.2,7.6,6.2,
             5.3,5.6,7.7,5.6,6.5,4.8,6.8,4.2,4.4,4.2,5.5,4.4,6.8,6.1,7.4,5.7,6.3,7.6,4.7,6.2,6.8,
             6.9,4.1,4.9,5.8,5.5,4.7,4.7,4.0,5.3,5.5,5.3,4.7,5.0,6.6,3.9,5.7,4.3,5.7,4.8,5.6,6.6,
             6.9,4.6,5.5,7.5,5.7,6.6,6.2,7.2,5.8,5.3,3.5,4.9,5.4,5.4,5.7,6.6,5.5,4.9,4.7,3.8,5.2,
             5.2,5.6,6.4,5.7,4.0,5.0,6.4,5.4,5.6,5.0,5.3,5.9,6.0,5.5,6.4,4.8,4.6,6.6,6.9,6.6,4.9,
             5.5,4.6,6.7,4.5,5.5,5.4,3.2,6.4,5.6,5.1,3.8,6.9,6.4,5.9,4.2,4.8,4.6,6.0,4.6,5.5,3.9,
             6.5,5.7,5.7,4.8,5.8,5.7,3.7,5.5,6.0,5.8,4.7,4.7,6.7,5.4,6.4,6.0,6.1,5.3,5.3,6.2,3.8,
             6.0,5.2,6.0,6.4,5.3,5.6,5.0,6.5,6.7,5.6,6.5,7.1,4.3,5.5,5.1,5.9,5.2,6.6,6.6,4.9,4.8,
             5.6,6.0,5.5,5.4,5.1,5.4,7.2,4.8,6.3,6.1,7.8,6.6,6.7,6.9,7.7,6.8,4.4,4.3,4.1,7.3,6.6,
             6.5,6.2,5.7,6.5,7.5,6.5,6.4,5.1,7.2,5.8,5.5,4.5,5.9,5.2,7.1,5.9,6.9,5.0,5.3,6.0,5.0,
             5.1,6.4,5.8,5.7,4.8,6.2,6.9,6.6,6.9,7.7,5.5,5.7,5.2,5.2,5.3,5.3,6.3,6.8,6.6,4.1,5.5,
             4.2,6.2,7.7,7.6,6.6,7.2,6.3,6.6,6.4,5.7,7.0,6.2,7.5,7.7,6.8,7.4,7.0,6.9,7.2,7.7,7.4,7.8,6.9,5.3,7.8,6.5,7.1,8.1,8.0,7.4,7.2,8.1,7.8]
tempcopy = templista.copy()
templista17 = tempcopy[0:44]
templista18 = tempcopy[44:144]
templista19 = tempcopy[144:244]
templista20 = tempcopy[244:264]
medeltemp = sum(templista)/len(templista)
medeltemp17 = sum(templista17)/len(templista17)
medeltemp18 = sum(templista18)/len(templista18)
medeltemp19 = sum(templista19)/len(templista19)
medeltemp20 = sum(templista20)/len(templista20)

i = -1
summa = 0.0
while i < len(templista)-1:
    i += 1
    summa = summa + (templista[i] - medeltemp)**2
std = math.sqrt(summa/len(templista))
i = -1
summa17 = 0.0
while i < len(templista17)-1:
    i += 1
    summa17 = summa17 + (templista17[i] - medeltemp17)**2
std17 = math.sqrt(summa17/len(templista17))
i = -1
summa18 = 0.0
while i < len(templista18)-1:
    i += 1
    summa18 = summa18 + (templista18[i] - medeltemp18)**2
std18 = math.sqrt(summa18/len(templista18))
i = -1
summa19 = 0.0
while i < len(templista19)-1:
    i += 1
    summa19 = summa19 + (templista19[i] - medeltemp19)**2
std19 = math.sqrt(summa19/len(templista19))
i = -1
summa20 = 0.0
while i < len(templista20)-1:
    i += 1
    summa20 = summa20 + (templista20[i] - medeltemp20)**2
std20 = math.sqrt(summa20/len(templista20))
print('Standardavvikelsen för medeltemperatur under 1700-talet var: ', std17)
print('Standardavvikelsen för medeltemperatur under 1800-talet var: ', std18)
print('Standardavvikelsen för medeltemperatur under 1900-talet var: ', std19)
print('Standardavvikelsen för medeltemperatur hittils under 2000-talet har varit:', std20)
print('Standardavvikelnse för medeltemperaturen under de senaste 264 åren är: ',std)