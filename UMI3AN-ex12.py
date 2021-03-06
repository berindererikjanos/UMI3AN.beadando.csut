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
    for i in range(2,int(math.sqrt(n)+1)): #példa a 1001
        if n%i==0:
            return False
    return True


#második függvény
def prim_10001():
    db = 0  #sorsz
    aktualis = 1
    while True:
        if prim_e(aktualis):
            #print(db,". prim: ",aktualis)
            if db == 10001:  #ide azt a számot írom, ahanyadik helyen lévő prímszámot keresem
                return aktualis
            else:
                db+=1

        aktualis+=1

print("-------------------------------------------------------------")
print("A 12-es beadandó feladat eredménye a következő:  ")
print("A keresett helyen lévő (10001.helyi) prímszám: ",prim_10001())
print("A program sikeresen lefutott!")
print("-------------------------------------------------------------")

#Beadandófeladatvége


#Példa
#1. lépés: aktualis = 1: 1 prím? -> nem akkor aktualis = 2
#2. lépés: aktualis = 2: 2 prím? -> igen és db == 10001 ? -->nem akkor db = 1 és aktualis = 3
#3. lépés: aktualis = 3: 3 prím? -> igen és db == 10001 ? -->nem akkor db = 2 és aktualis = 4
#4. lépés : aktualis = 4: 4 prím? -> nem és db ==10001? --> nem akkor db = 2 és aktualis = 5
#5. lépés : aktuális = 5 : 5 prím? -> igen és db == 10001 --> nem akkor db= 3 és aktualis = 6
#....
#10001. lépés: aktualis = 104759: 104759 prím? -> igen és db = 104759 ? -> igen akkor vége
            
