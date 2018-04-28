#Berinder Erik János UMI3AN Csütörtök 10:00 HB
#EX9
#The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime
#factor of the number 600851475143

def is_prim(number):

    if number==2:
            return 'Prim'
    for i in range(2,number):
        if number%i == 0:
            return 'Not Prim'
    return 'Prim'


