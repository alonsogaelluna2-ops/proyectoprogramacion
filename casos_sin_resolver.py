print ("CASOS SIN RESOLVER")
print ("-------Menú de opciones-------")
print ("(Escribe tu respuesta)")
print ("1. Escoger un caso")
print ("2. Salir")
while True:
    op = int(input ("Ingrese una opción: "))
    if op == 1:
        print ("-------Casos disponibles-------")
        print ("1. El robo del Reloj") 
        print ("2. La desaparición del estudiante") 
        print ("3. El sabotaje del laboratorio")       
    elif op == 2:
        print ("Saliendo del programa...")
        break   
    else:
        print ("Opción inválida. Por favor, ingrese una opción válida.")
        break
       

