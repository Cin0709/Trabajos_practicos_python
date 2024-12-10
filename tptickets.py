import random, pickle, os, sys


numero = random.randint ( 1000 , 9999 )


numero_ticket = random.randint ( 1000 , 9999 )
cont = 0
control = True
nuevo_ticket = 1 
leer_ticket = 2
salir = 3

print ("           Hola bienvenido al sistema de tickets\n ")

while control : 
    n = int(input("1-Generar un nuevo Ticket\n2-Leer un Ticket\n3-Salir\nSeleccione:  " ))

    if n == 1 : 
        print("\nIngrese los datos para generar un nuevo ticket") 
        nombre = input("ingrese su nombre: Gabriel")
        sector = input("Ingrese su sector:Tecno3f ")
        asunto = input("Ingrese asunto :Pc ")
        mensaje = input("Ingrese un mensaje: No enciende la Pc")
        numero_ticket = random.randint(1000, 9999)
        
        print(f"\n ========================================\n      Se genero el siguiente ticket\n ========================================\n Su nombre: Gabriel         Numero de ticket: {numero_ticket} \n Sector: Tecno3f\n Asunto: Pc\n Mensaje: no enciende la Pc\n\n         Recordar su numero de ticket")
        respuesta = input("\nDesea generar un nuevo ticket? (S/N):   ")
        if respuesta.lower() == "N":
         control = False 
        else:
         respuesta.lower() == "S"
         control = True
    
    
    elif n == 2:  
      print(f"\nIngrese numero de ticket: {numero_ticket}")
      respuesta2 = input("\nDesea leer otro ticket? (S/N):  ")
      if respuesta2.lower() == "N":
         control = False 
      else:
         respuesta2.lower() == "S"
         control = True

    elif n == 3:
        print("\nUsted esta por abandonar el programa")
        respuesta3 = input("\nEsta seguro que desea abandonar el programa? (S/N):  ")
        if respuesta3.lower() == "N":
         control = False 
        else:
         respuesta3.lower() == "S"
         break
        