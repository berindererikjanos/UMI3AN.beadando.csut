#Berinder Erik János UMI3AN Csütörtök 10:00 HB
#EX9
#The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime
#factor of the number 600851475143

import math

#első függvény
def prim_e(n):
    if n == 0 or n == 1:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    return True


#második függvény   
def primtenyezok(n):
    tenyezok = [] 
    for i in range(2,int(math.sqrt(n)+1)):
        while prim_e(i) and n%i == 0:
            tenyezok.append(i) 
            n = n // i 
            if n == 1: 
                return tenyezok

n = 600851475143
lista = primtenyezok(n)
print("----------------------------------------")
print("A megadott szám összes prímtényezője: ",lista)
print("A megadott szám legnagyobb prímtényezője: ",max(lista))
print("A program sikeresen lefutott!")
print("----------------------------------------")

#Beadandófeladatvége

#PÉLDA: n = 60
#i megy 2-től gyök(60): azaz i [2,7] közt fog menni
#1. lépés: i = 2
#   while i prím és n%2 == 0
#   2 prím és 60%2 == 0 ? -> igen :
#       tenyezok = [2]
#       60 = 60 // 2 = 30 ebben a lépésben n = 30
#   2 prím és 30%2 == 0 ? -> igen
#         tenyezok = [2,2]
#         30 = 30 // 2 = 15 ebben a lépésben n = 15
#     2 prím és 15%2==0 ? -> nem
# #2. lépés: i = 3
#     while i prím és n%3==0:
#     3 prím és 15%3 == 0? -> igen:
#         tenyezok = [2,2,3]
#         15 = 15 // 3 = 5 ebben a lépésben már n = 5
#     3 prím és 5%3 == 0 ? -> nem
# 3. lépés: i = 4
#     while i prím és n%4 == 0
#     4 prím és 5%4==0? -#nem
# 4. lépés: i = 5
#     while i prím és n%4 == 0
#     5 prím és 5%5 == 0 -> igen
#         tenyezok = [2,2,3,5]
#         5 = 5 // 5 = 1 ebben a lépésben n = 1
