primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def its_prime():
    """Elige un número entre 1 y 100 y te digo si es primo"""
    continuo = True
    while continuo:
        n = input("Escriba un número entero entre 1 y 100: \n")
        try:
            if int(n) > 1 and int(n) < 100 and int(n) in primes :
                print(str(n) + " es un número primo")
            elif int(n) > 1 and int(n) < 100:     
                print(str(n) + " no es un número primo")
            elif int(n) == -1:     
                print(str(n) + " Estoy Saliendo")
                continuo = False
            else :
                print(str(n) + " no es un número entero entre 1 y 100")
        except: 
            print(str(n) + " no es un número entero entre 1 y 100")

its_prime()