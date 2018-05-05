#Berinder Erik János UMI3AN Csütörtök 10:00 HB
#EX9
#The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime
#factor of the number 600851475143


import math


def prim_e(n):
    if n == 0 or n == 1:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    return True

    
    

