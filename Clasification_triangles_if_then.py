#Clasificación de triángulos

a = int(input("medida del lado a = "))
b = int(input("medida del lado b = "))
c = int(input("medida del lado c = "))
if a != b and b != c and a != c :
    print( "El triángulo es escaleno")
elif a==b and b==c :
    print("El triángulo es equlátero")
else:
    print("El triangulo es isósceles")