def mostrar_caso(titulo, descripcion):
    print(titulo)
    print(descripcion)

def mostrar_acciones():
    print("Acciones disponibles:")
    print("1. Ver sospechosos")
    print("2. Ver pistas")
    print("3. Acusar a alguien")
    print("4. Regresar al menú")

def mostrar_sospechosos(caso):
    print("Sospechosos:")
    if caso == 1:
        print("1. Carlos, el vendedor")
        print("2. Laura, la gerente")
        print("3. Miguel, el guardia")
    elif caso == 2:
        print("1. Diego, el compañero de cuarto")
        print("2. Elena, la profesora")
        print("3. Raúl, el mejor amigo")
    elif caso == 3:
        print("1. Dra. Ramírez, la investigadora")
        print("2. Julián, el técnico")
        print("3. Sofía, la becaria")

def mostrar_pistas(caso):
    print("Pistas disponibles:")
    if caso == 1:
        print("- Las huellas de la vitrina son de alguien con llaves de la tienda")
        print("- La cámara de seguridad se apagó 10 minutos")
        print("- Laura tenía las llaves de la caja fuerte")
    elif caso == 2:
        print("- La mochila del estudiante sigue en su cuarto")
        print("- Su celular tiene un mensaje sin enviar para Raúl")
        print("- Raúl dijo que no lo veía desde hace una semana, pero lo vieron juntos ayer")
    elif caso == 3:
        print("- Los químicos usados solo están en el almacén de la Dra. Ramírez")
        print("- La puerta no fue forzada")
        print("- Alguien usó una tarjeta de acceso a las 3 a.m.")

def numero_culpable(caso):
    # Regresa el número del sospechoso que es el culpable de cada caso
    if caso == 1:
        return 2
    elif caso == 2:
        return 3
    else:
        return 1

def investigar(caso):
    pistas_vistas = 0
    while True:
        mostrar_acciones()
        acc = int(input("Selecciona una acción: "))
        if acc == 1:
            mostrar_sospechosos(caso)
        elif acc == 2:
            mostrar_pistas(caso)
            pistas_vistas += 1
        elif acc == 3:
            mostrar_sospechosos(caso)
            acusado = int(input("¿A quién acusas? (número): "))
            if acusado == numero_culpable(caso):
                # Cada vez que viste las pistas se restan 10 puntos
                puntos = 100 - (pistas_vistas * 10)
                if puntos < 0:
                    puntos = 0
                print("¡Caso resuelto!")
                print("Puntuación obtenida:", puntos)
            else:
                print("Acusación incorrecta")
                print("El verdadero culpable era el sospechoso número", numero_culpable(caso))
            break
        elif acc == 4:
            break
        else:
            print("Opción no válida")

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
            investigar(1)
        elif op == 2:
            mostrar_caso("La desaparición del estudiante", "Un estudiante universitario ha desaparecido misteriosamente. Se han encontrado sus pertenencias en su habitación, pero no hay señales de lucha. ¿Qué pudo haber pasado?")
            investigar(2)
        elif op == 3:
            mostrar_caso("El sabotaje del laboratorio", "Un laboratorio de investigación ha sido saboteado. Se han encontrado rastros de sustancias químicas peligrosas y se sospecha que alguien con conocimientos en química está detrás del sabotaje. ¿Quién es el responsable?") 
            investigar(3)
        else:
            print ("Opción no válida")
        print ("-------Menú de opciones-------")
        print ("1. Escoger un caso")
        print ("2. Salir")
    elif op == 2:
            print ("Saliendo del programa...")
            break   
    else:
            print ("Opción inválida. Por favor, ingrese una opción válida.")