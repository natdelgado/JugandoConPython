#Calculadora

"""Calculadora sencilla que al ingresar dos numeros 
y una operacion muestra el resultado"""

x = int(input("Ingrese el primer numero: "))
y = int(input("Ingrese el segundo numero: "))
operacion = int(input("Eliga la operacion: 1(*) 2(/) 3(+) 4(-) "))

def Operar():
   if operacion == 1 :
      resultado = x * y
      
   elif operacion == 2 :
      resultado = x / y
      
   elif operacion == 3 :
      resultado = x + y
      
   elif operacion == 4 :
      resultado = x - y
   print("Resultado " + str(resultado))
   """else :
      print("Escribe el numero de una operacion existente")"""
Operar()        
