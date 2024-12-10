import secrets, string, sys

diccionario = {
  'letras':string.ascii_letters,
  'numeros': string.digits,
  'caracteres': string.punctuation
}
password = ''
control = True

print("\n*++++++++++++ WELCOME ++++++++++++*\n\n\n Generador de contraseñas VO.1\n\n\n**++++++++++++{*+*}+++++++++++**\n\n\n")
print("Seleccione una de las siguientes opciones:\n\n *1. Generar contraseñas solo de letras.\n *2.  Generar contraseñas solo de numeros.\n *3.  Generar contraseñas letras y numeros.\n *4.  Generar contraseñas letras, numeros y caracteres.\n *0. Salir.")
def generar_contraseña(caracteres_disponibles, longitud=12): 
    return ''.join(secrets.choice(caracteres_disponibles) 
for _ in range(longitud)) 
control = True

while control:
    n = input("\n\nEscriba la opcion seleccionada: " )

    if n == "1": 
        contraseña = generar_contraseña(diccionario['letras'])
        print(f"\nSu contraseña es: {contraseña}")
        respuesta = input('\nenter para volver al menu principal  ')
        if respuesta.lower() == " ":
         control = True
        
    elif n == '2': 
        contraseña = generar_contraseña(diccionario['numeros'])
        print(f"\nSu contraseña es: {contraseña}")
        respuesta = input('\nenter para volver al menu principal  ')
        if respuesta.lower() == " ":
         control = True

    elif n == '3': 
        caracteres_disponibles = diccionario['letras'] + diccionario['numeros']
        contraseña = generar_contraseña(caracteres_disponibles)
        print(f"\nSu contraseña es: {contraseña}")   
        respuesta = input('\nenter para volver al menu principal  ')
        if respuesta.lower() == " ":
         control = True

    elif n == '4':
        caracteres_completo = diccionario['letras'] + diccionario['numeros'] + diccionario['caracteres']
        contraseña = generar_contraseña(caracteres_completo)
        print(f'\nSu contraseña es: {contraseña}')
        respuesta = input('\nenter para volver al menu principal  ')
        if respuesta.lower() == " ":
         control = True

    elif n == '0':
        print('Gracias por usar nuestro generador de contraseñas... Hasta pronto')
        break
    

# elif n == 3:
 #       print("Usted esta por abandonar el programa")
  #      respuesta3 = input("\nEsta seguro que desea abandonar el programa? (S/N):  ")
   #     if respuesta3.lower() == "N":
    #     control = False 
     #   else:
      #   respuesta3.lower() == "S"
       #  break
      