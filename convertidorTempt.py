#Convertidor de temperatura de Celsius a Fahrenheit
celsius = int(input())

def conv(c):
    f = 9/5 * c + 32
    return f

fahrenheit = conv(celsius)
print(fahrenheit)