#Berinder Erik János UMI3AN Csütörtök 10:00 HB
#EX12
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
#that the 6th prime is 13. What is the 10 001st prime number?

import math

def primszam_e(n):
    if n==0 or n==1:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    return True

def primszam_10001ig():
    db = 0
    aktualis = 1
    while True:
        if primszam_e(aktualis):
            print(db,". prim: " aktualis)
            if db == 100001:
                return aktualis
print("-------------------------------------------------------------")
print("A 12-es beadandó feladat eredménye a következő:  ")
print("A keresett helyen lévő (10001.helyi) prímszám: ",prim_10001())
print("-------------------------------------------------------------")
            
            
