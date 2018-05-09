#Berinder Erik János UMI3AN Csütörtök 10:00 HB
#EX12
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
#that the 6th prime is 13. What is the 10 001st prime number?
#Prímszámos feladat: Melyik a 10001. helyen szereplő prímszám?


import math

#első függvény
def prim_e(n):
    if n==0 or n==1:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True



def prim_10001():
    db = 0
    aktualis = 1
    while True:
        if prim_e(aktualis):
            #print(db,". prim: ",aktualis)
            if db == 10001:
                return aktualis
            else:
                db+=1

        aktualis+=1

print("-------------------------------------------------------------")
print("A 12-es beadandó feladat eredménye a következő:  ")
print("A keresett helyen lévő (10001.helyi) prímszám: ",prim_10001())
print("Sikeres!")
print("-------------------------------------------------------------")
            
