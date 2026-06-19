diccionario={}
 
while True:
    print('''=== MENÚ PRINCIPAL ===
    1. Registrar estudiante
    2. Buscar estudiante
    3. Actualizar nombre de estudiante
    4. Eliminar estudiante
    5. Mostrar todos los estudiantes
    6. Salir
    ''')
    try:
        opcion = int(input("Ingrese opcion de la lista [1-6] : "))
        
        if opcion == 1:
            nombre=input("Ingrese el nombre : ")
            diccionario["nombre"]=nombre
        
        elif opcion == 2:
            nombre_buscar=input("Ingrese el nombre para buscar : ")
            if nombre_buscar in diccionario:
                print("Estudiante", nombre_buscar , "registrado")
            else:
                print("Estudiante no registrado.")
        
        elif opcion == 3:
            nombre_anterior=input("Ingrese nombre a cambiar : ")
            if nombre_anterior in diccionario:
                nuevo_nombre=input("Ingrese nombre nuevo : ")
                diccionario[nuevo_nombre]=diccionario[nombre_anterior]
                del diccionario[nombre_anterior]
            else:
                print("Estudiante no Registrado")
        
        elif opcion ==4:
            eliminar_estudiante=input("Ingrese estudiante a eliminar de la lista: ")
            if eliminar_estudiante in diccionario:
                del diccionario[nombre]
            else:
                print("El estudiante no se encuentra en la lista ")
                
        else:
            print("Caracter invalido")
            
    except ValueError as e:
        print("Error ",e )
        
        
                    
            
            