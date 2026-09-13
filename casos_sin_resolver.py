def mostrar_caso(titulo, descripcion):
    print(titulo)
    print(descripcion)

def mostrar_acciones():
    print("Acciones disponibles:")
    print("1. Investigar la escena del crimen")
    print("2. Interrogar a los sospechosos")
    print("3. Analizar las pruebas")
    print("4. Salir del caso")


print ("CASOS SIN RESOLVER")
print ("-------Menú de opciones-------")
print ("----(Escribe tu respuesta)----")
print ("1. Escoger un caso")
print ("2. Salir")
while True:
    op = int(input ("Ingrese una opción: "))
    if op == 1:
        print ("-------Casos disponibles-------")
        print ("1. El robo del Reloj") 
        print ("2. La desaparición del estudiante") 
        print ("3. El sabotaje del laboratorio")
        op = int(input ("Escoge el caso que deseas resolver: ")) 
        if op == 1:
            mostrar_caso("El robo del Reloj", "El reloj de la joyería ha sido robado. Se sospecha que el ladrón es un empleado de la tienda. Se han encontrado huellas dactilares en la vitrina donde estaba el reloj. ¿Quién es el culpable?")
            mostrar_acciones()
        elif op == 2:
            mostrar_caso("La desaparición del estudiante", "Un estudiante universitario ha desaparecido misteriosamente. Se han encontrado sus pertenencias en su habitación, pero no hay señales de lucha. ¿Qué pudo haber pasado?")
            mostrar_acciones()
        elif op == 3:
            mostrar_caso("El sabotaje del laboratorio", "Un laboratorio de investigación ha sido saboteado. Se han encontrado rastros de sustancias químicas peligrosas y se sospecha que alguien con conocimientos en química está detrás del sabotaje. ¿Quién es el responsable?") 
            mostrar_acciones()
    elif op == 2:
            print ("Saliendo del programa...")
            break   
    else:
            print ("Opción inválida. Por favor, ingrese una opción válida.")
            break
