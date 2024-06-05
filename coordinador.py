import json
import os as system
import random
import funciones.rec_funcion as reu
import time
import trainer
        
def registrar_camper():
    while True:        
        data = reu.leer_crear_json()
        print("********************************************************")
        print("                   REGISTRO DE CAMPER")
        print("********************************************************")
        nombres = input("Ingrese sus nombres: ")
        apellidos = input("Ingrese sus apellidos: ")
        
        try:
            documento = int(input("Ingrese el número de documento de identificación: "))
        except ValueError:
            print("Número de documento inválido. Por favor, ingrese un número.")
            continue
        
        if data["campers"].get(str(documento), None) is None:
            direccion = input("Ingrese la dirección de residencia: ")
            acudiente = input("Ingrese el nombre del acudiente del camper: ")
            
            try:
                telefonos_movil = int(input("Ingrese el número de teléfono móvil: "))
            except ValueError:
                print("Número de teléfono móvil inválido. Por favor, ingrese un número.")
                continue
    
            try:
                telefono_fijo = int(input("Ingrese el número de teléfono fijo: "))
            except ValueError:
                print("Número de teléfono fijo inválido. Por favor, ingrese un número.")
                continue
            
            estado = "Inscrito" # (En proceso de ingreso, Inscrito, Aprobado, Cursando, Graduado, Expulsado, Retirado)
            riesgo = False
            data["campers"][str(documento)] = {
                "Nombres": nombres,
                "Apellidos": apellidos,
                "Direccion": direccion,
                "Acudiente": acudiente,
                "Telefonos movil": telefonos_movil,
                "Telefonos fijo": telefono_fijo,
                "Estado": estado,
                "Riesgo": riesgo
            }
            print("***********************************************")
            reu.guardar_actualizar_json(data)
            print("Registro guardado correctamente.")
            time.sleep(2)
            reu.clear()
            print("***********************************************")
        else:
            print("***********************************************")
            print("Este camper ya se encuentra registrado.")
            time.sleep(2)
            reu.clear()
            print("***********************************************")
                  
        while True:
            rep = input("¿Desea agregar otro camper para presentar examen? (1. Si, 2. No): ")
            if rep == '1': 
                time.sleep(0.5)
                reu.clear()
                break
            elif rep == '2': 
                time.sleep(0.5)
                reu.clear()
                return
            else: print("Opción no válida. Por favor, ingrese 1 para Sí o 2 para No.")

def modificar_camper():
    data = reu.leer_crear_json()
    print("********************************************************")
    print("                   MODIFICAR CAMPER")
    print("********************************************************")
    
    doc = input("Ingrese el documento para modificar al camper: ")
    
    if data["campers"].get(doc, None) is not None:
        while True:
            print("\nEstos son los valores actuales del camper:")
            cont_mod_validas = 1
            for key, value in data["campers"][doc].items():
                print(f"{cont_mod_validas}. {key}: {value}")
                cont_mod_validas += 1
                if cont_mod_validas == 7:
                    print("7. Salir")
                    break
            
            try:
                opt = int(input("\n¿Qué deseas modificar? (1-7): "))
            except ValueError:
                print("Por favor, ingresa un número válido.")
                continue

            if opt == 1: data["campers"][doc]["Nombres"] = input("Ingrese sus nombres: ")
            elif opt == 2: data["campers"][doc]["Apellidos"] = input("Ingrese sus apellidos: ")
            elif opt == 3: data["campers"][doc]["Direccion"] = input("Ingrese la dirección de residencia: ")
            elif opt == 4: data["campers"][doc]["Acudiente"] = input("Ingrese el nombre del acudiente del camper: ")
            
            elif opt == 5:
                try: data["campers"][doc]["Telefonos movil"] = int(input("Ingrese el número de teléfono móvil: "))
                except ValueError: 
                    print("Por favor, ingresa un número de teléfono válido.")
                    continue
                
            elif opt == 6:
                try: data["campers"][doc]["Telefonos fijo"] = int(input("Ingrese el número de teléfono fijo: "))
                except ValueError:
                    print("Por favor, ingresa un número de teléfono válido.")
                    continue
            elif opt == 7:
                reu.guardar_actualizar_json(data)
                print("***********************************************")
                print("Modificaciones guardadas.")
                print("***********************************************")
                time.sleep(2)
                reu.clear()
                break
            else:
                print("Opción no válida. Por favor, elige una opción del 1 al 7.")
    else:
        print("***********************************************")
        print("No se encontró un camper con ese documento.")
        print("***********************************************")
        time.sleep(3)
        reu.clear()

def mostrar_campers_inscritos():
    data = reu.leer_crear_json()
    
    print("********************************************************")
    print("                 LISTA CAMPER REGISTRADOS")
    print("********************************************************")    

    cont=1
    lista_de_inscritos=list(data["campers"])
    cantidad_de_inscritos=len(lista_de_inscritos)
    if cantidad_de_inscritos>0:
        for doc, info in data["campers"].items():
            print(f"----------Candidato {cont}----------")
            print(f"documento: {doc}")
            print(f"Nombres: {info["Nombres"]}")
            print(f"Apellidos: {info["Apellidos"]}")
            print(f"Direccion: {info["Direccion"]}")
            print(f"Acudiente: {info["Acudiente"]}")
            print(f"Telefonos movil: {info["Telefonos movil"]}")
            print(f"Telefonos fijo: {info["Telefonos fijo"]}")
            print(f"Estado: {info["Estado"]}\n")
            cont+=1
        reu.wait_for_keypress()
        reu.clear()
        return
    else:
        print("No hay posibles campers incritos para el examen de admision")

def retirar_camper():
    data = reu.leer_crear_json()
    print("************************************************************")
    print("           Retiro de camper para el examen")
    print("************************************************************")
    
    doc = input("Ingrese el documento para retirar al camper: ")
    if data["campers"].get(doc, None) is not None:
        try:
            opt = int(input("\n1. Retiro Voluntario\n2. Expulsar\n\n¿Qué acción quieres realizar?\nIngrese su opción: "))
            if opt == 1:
                data["campers"][doc]["Estado"] = "Retirado"
                reu.guardar_actualizar_json(data)
                print("***********************************************")
                print("\nCambio de estado guardado correctamente.")
                print("***********************************************")
                
            elif opt == 2:
                data["campers"][doc]["Estado"] = "Expulsado"
                reu.guardar_actualizar_json(data)
                print("***********************************************")
                print("\nCambio de estado guardado correctamente.")
                print("***********************************************")
                time.sleep(2)
                reu.clear()
            else:
                print("Opción no válida. Por favor, elige 1 o 2.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    else:
        print("***********************************************")
        print("No se encontró un camper con ese documento.")
        print("***********************************************")
        time.sleep(2)
        reu.clear()
        
def presentar_pruebas():
    print("********************************************************")
    print("              EXAMEN PARA SER UN CAMPER")
    print("********************************************************")
    data=reu.leer_crear_json()
    for doc in data["campers"].keys():
        if data["campers"][doc]["Estado"] == "Inscrito":
            n=random.randint(1,2)
            if n==1: data["campers"][doc]["Estado"] = "Rechazado"
            if n==2: data["campers"][doc]["Estado"] = "En proceso de ingreso"
            reu.guardar_actualizar_json(data)
    time.sleep(1)
            
    print("********************************************************")
    print("              ¡Pruebas finalizadas!")
    print("Ya puede revisar los resultados de los candidatos inscritos")
    print("********************************************************")
    time.sleep(4)
    reu.clear()
    
        
def rechazados():
    data = reu.leer_crear_json()
    print("********************************************************")
    print("                Candidatos rechazados")
    print("********************************************************")
    print("Estos fueron los rechazados:\n")
    
    candidatos_a_eliminar = []

    for doc, info in data["campers"].items():
        if info["Estado"] == "Rechazado":
            print("Nombre: ", info["Nombres"])
            print("Apellidos: ", info["Apellidos"])
            print("Documento: ", doc)
            print("Estado: ", info["Estado"], "\n")
            candidatos_a_eliminar.append(doc)
    opc=input("Desea eliminar los candidatos que no pasaron la prueba de ingreso.\n1.Si\n2.No\nDigite su opcion:")
    if opc=="1":
        for doc in candidatos_a_eliminar:
            print(f"Candidato {data["campers"][doc]["Nombres"]} {data["campers"][doc]["Apellidos"]} con documento {doc} borrado, no aprobó el examen.")
            del data["campers"][doc]
        reu.guardar_actualizar_json(data)
        print("***********************************************")
        print("Todos los candidatos rechazados han sido borrados.")
        print("***********************************************")
        time.sleep(3)
        reu.clear()
    if opc=="2":
        print("********************************************************")
        print("NOTA: Siempre que ingreses a revisar los datos lo podras eliminarlos cuando quieras.")
        print("********************************************************")
        time.sleep(3)
        reu.clear()
        return
    
def esperando_para_ingresar():
    data = reu.leer_crear_json()
    print("********************************************************")
    print("       Transferir a lista de ingreso a CAMPUSLANDS")
    print("********************************************************")
    print("Estos candidatos están en proceso de ingreso:\n")
    
    candidatos_a_eliminar = []

    for doc, info in data["campers"].items():
        if info["Estado"] == "En proceso de ingreso":
            data["en espera"][doc] = info
            print("Nombre: ", info["Nombres"])
            print("Apellidos: ", info["Apellidos"])
            print("Documento: ", doc)
            print("Estado: ", info["Estado"], "\n")
            candidatos_a_eliminar.append(doc)
            
    for doc in candidatos_a_eliminar:
        print(f"Candidato {data['en espera'][doc]['Nombres']} {data['en espera'][doc]['Apellidos']} con documento {doc}")
        print("En lista de espera, aprobó el examen.")
        del data["campers"][doc]
    
    reu.guardar_actualizar_json(data)
    print("********************************************************")
    print("Todos los candidatos en proceso de ingreso han sido movidos a la lista de espera.")
    print("********************************************************")
    reu.wait_for_keypress()
    reu.clear()

def mostrar_est_espera():
    print("********************************************************")
    print("  Estudiantes en espera para ingresar a CAMPUSLANDS")
    print("********************************************************")
    data=reu.leer_crear_json()
    cont=1
    lista_de_inscritos=list(data["en espera"])
    cantidad_de_inscritos=len(lista_de_inscritos)
    if cantidad_de_inscritos>0:
        for doc, info in data["en espera"].items():
            print(f"Estudiante en espera {cont}:")
            print(f"Nombres: {info["Nombres"]}")
            print(f"Apellidos: {info["Apellidos"]}")
            print(f"Direccion: {info["Direccion"]}")
            print(f"Acudiente: {info["Acudiente"]}")
            print(f"Telefonos movil: {info["Telefonos movil"]}")
            print(f"Telefonos fijo: {info["Telefonos fijo"]}")
            print(f"Estado: {info["Estado"]}\n")
            cont+=1
        reu.wait_for_keypress()
        reu.clear()
        return
    else:
        print("********************************************************")
        print("No hay posibles campers en espera para ingresar a estudiar")
        print("********************************************************")
        time.sleep(3)
        reu.clear()
        
def asignar_salon():
    data = reu.leer_crear_json()
    
    print("********************************************************")
    print("    Asignacion de grupos para estudiantes en espera")
    print("********************************************************")
    
    data_list_espera = list(data["en espera"].items())
    cantidad_est_espera = len(data_list_espera)
    print(f"Cantidad de estudiantes en espera: {cantidad_est_espera}")
    nombre_salon = input("Ingrese el nombre del salón (ej: A1, A2): ")
    
    if nombre_salon in data["estudiantes"]:
        print(f"Lo siento, el nombre {nombre_salon} ya está en uso. Inténtalo de nuevo.")
        print("Puedes ir al menú y escoger la opción mostrar los grupos actuales")
        return
    
    #ASIGNACION DE CANTIDAD MINIMA Y MAXIMA DE ESTUDIANTES
    max_estudiantes = 33
    min_estudiantes = 5
    
    if cantidad_est_espera >= min_estudiantes:
        data["estudiantes"][nombre_salon] = {}
        estudiantes_a_asignar = min(cantidad_est_espera, max_estudiantes)
        
        for i in range(estudiantes_a_asignar):
            doc, info = data_list_espera[i]
            data["estudiantes"][nombre_salon][doc] = info
            
        # Eliminar los estudiantes de la lista de espera
        data_filtrada = {}
        for i, (doc, info) in enumerate(data["en espera"].items()):
            if i >= estudiantes_a_asignar:
                data_filtrada[doc] = info
        data["en espera"] = data_filtrada
        
        logistica=trainer.leer_logistica_campus()
        logistica["grupos"].append(nombre_salon)
        trainer.guardar_logistica_campus(logistica)
        reu.guardar_actualizar_json(data)
        print("********************************************************")
        print(f"Se asignaron {estudiantes_a_asignar} estudiantes al salón {nombre_salon}.")
        print("********************************************************")
        reu.wait_for_keypress()
        reu.clear()
    else:
        print("********************************************************")
        print("Aún no hay suficientes estudiantes para asignar un grupo.")
        print("********************************************************")
        time.sleep(3)
        reu.clear()
    
def mostrar_grupos():
    data = reu.leer_crear_json()
    cont = 1
    if "estudiantes" in data and data["estudiantes"]:
        print("Grupos actuales:")
        for grupo in data["estudiantes"].keys():
            print(f"{cont}. Grupo {grupo}")
            cont += 1
        reu.wait_for_keypress()
        reu.clear()
    else:
        print("***********************************************")
        print("No hay grupos registrados.")
        print("***********************************************")
        time.sleep(3)
        reu.clear()
    
def mostrar_estudiantes_de_un_grupo():
    data = reu.leer_crear_json()
    print("********************************************************")
    print("            MOSTRAR ESTUDIANTES DE UN GRUPO")
    print("********************************************************")
    if "estudiantes" not in data or not data["estudiantes"]:
        print("No hay grupos registrados.")
        return
    
    nombre_salon = input("Ingrese el nombre del grupo (ej: A1, A2): ")
    
    if nombre_salon in data["estudiantes"]:
        estudiantes = data["estudiantes"][nombre_salon]
        if estudiantes:
            print(f"Estudiantes en el grupo {nombre_salon}:")
            for doc, info in estudiantes.items():
                print(f"Documento: {doc}")
                print(f"Nombre: {info['Nombres']}")
                print(f"Apellidos: {info['Apellidos']}")
                print(f"Dirección: {info['Direccion']}")
                print(f"Acudiente: {info['Acudiente']}")
                print(f"Teléfono móvil: {info['Telefonos movil']}")
                print(f"Teléfono fijo: {info['Telefonos fijo']}")
                print(f"Estado: {info['Estado']}")
                print(f"Riesgo: {info['Riesgo']}\n")
            reu.wait_for_keypress()
            reu.clear()
        else:
            print(f"No hay estudiantes en el grupo {nombre_salon}.")
    else:
        print("***********************************************")
        print(f"No se encontró el grupo {nombre_salon}.")
        print("***********************************************")
        time.sleep(3)
        reu.clear()

#SE ASIGNA LA RUTA DE APRENDIZAJE BACKEND AL FINALIZAR LOS MODULOS.
def asignar_ruta():
    try:
        data = reu.leer_crear_json()
        
        if "estudiantes" not in data or not data["estudiantes"]:
            raise ValueError("No hay grupos registrados.")
        
        nombre_salon = input("Ingrese el nombre del grupo (ej: A1, A2): ")
        
        if nombre_salon not in data["estudiantes"]:
            raise ValueError(f"No se encontró el grupo {nombre_salon}.")
            time.sleep(0.5)
            reu.clear()
            
        
        print("Rutas de entrenamiento disponibles:")
        print("1. Ruta NodeJS")
        print("2. Ruta Java")
        print("3. Ruta NetCore")
        
        opcion = input("Seleccione la ruta de entrenamiento (1, 2, o 3): ")
        
        if opcion == "1":
            ruta = "Ruta NodeJS"
        elif opcion == "2":
            ruta = "Ruta Java"
        elif opcion == "3":
            ruta = "Ruta NetCore"
        else:
            raise ValueError("Opción no válida.")
        
        for doc, info in data["estudiantes"][nombre_salon].items():
            info["Ruta de aprendizaje"] = ruta
            
        # Asigna los diccionarios para introducir la información de los módulos
        modulos = [
            "Fundamentos de programacion",
            "Programacion Web",
            "Programacion formal",
            "Bases de datos",
            "Ruta de aprendizaje"
        ]

        for grupo in data["estudiantes"].values():
            for estudiante in grupo.values():
                if "Calificaciones" not in estudiante:
                    estudiante["Calificaciones"] = {modulo: {"practico":[],"teorico":[],"otros":[],"total":0} for modulo in modulos}
                if "Progreso" not in estudiante:
                    estudiante["Progreso"] = {modulo: False for modulo in modulos}
                if "Malas Calificaciones" not in estudiante:
                    estudiante["Malas Calificaciones"] = {modulo: 0 for modulo in modulos}
        
        reu.guardar_actualizar_json(data)
        print("***********************************************")
        print(f"Se asignó la {ruta} al grupo {nombre_salon}.")
        print("***********************************************")
        time.sleep(3)
        reu.clear()
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")

# Ejemplo de llamada a la función (puedes comentar esto cuando lo integres en tu sistema)
# asignar_ruta()

    
    
    #ASIGNA LOS DICCIONARIOS PARA INTRODUCIR LA INFORMACION DE LOS MODULOS
        # - Fundamentos de programación (Introducción a la algoritmia, PSeInt y Python)
        # - Programación Web (HTML, CSS y Bootstrap).
        # - Programación formal (Java, JavaScript, C#).
        # - Bases de datos (Mysql, MongoDb y Postgresql). Cada ruta tiene un SGDB principal y un alternativo.

def calificar_estudiantes():
    data = reu.leer_crear_json()

    if "estudiantes" not in data or not data["estudiantes"]:
        print("No hay grupos registrados.")
        time.sleep(3)
        reu.clear()
        return
    
    nombre_salon = input("Ingrese el nombre del grupo (ej: A1, A2): ")

    if nombre_salon not in data["estudiantes"]:
        print(f"No se encontró el grupo {nombre_salon}.")
        time.sleep(2)
        reu.clear()
        return

    print("Módulos disponibles para calificar:")
    print("1. Fundamentos de programacion")
    print("2. Programacion Web")
    print("3. Programacion formal")
    print("4. Bases de datos")
    print("5. Ruta de aprendizaje")

    opcion = input("Seleccione el módulo a calificar (1, 2, 3, 4, 5): ")

    modulos = {
        "1": "Fundamentos de programacion",
        "2": "Programacion Web",
        "3": "Programacion formal",
        "4": "Bases de datos",
        "5": "Ruta de aprendizaje"
    }

    if opcion not in modulos:
        print("Opción no válida.")
        time.sleep(1)
        reu.clear()
        return

    modulo = modulos[opcion]

    estudiantes_a_eliminar = []

    for doc, info in data["estudiantes"][nombre_salon].items():
        if opcion != "5":  # Ruta de aprendizaje no necesita calificación
            calificacion_practico = input(f"Ingrese la calificación práctica de {info['Nombres']} {info['Apellidos']} para {modulo} (0-100): ")
            calificacion_teorico = input(f"Ingrese la calificación teórica de {info['Nombres']} {info['Apellidos']} para {modulo} (0-100): ")
            calificacion_otros = input(f"Ingrese otras calificaciones de {info['Nombres']} {info['Apellidos']} para {modulo} (0-100): ")
            print(" ")
            try:
                calificacion_practico = int(calificacion_practico)
                calificacion_teorico = int(calificacion_teorico)
                calificacion_otros = int(calificacion_otros)
                if not (0 <= calificacion_practico <= 100 and 0 <= calificacion_teorico <= 100 and 0 <= calificacion_otros <= 100):
                    raise ValueError
            except ValueError:
                print(f"Calificación no válida para {info['Nombres']} {info['Apellidos']}.")
                continue

            info["Calificaciones"][modulo]["practico"].append(calificacion_practico)
            info["Calificaciones"][modulo]["teorico"].append(calificacion_teorico)
            info["Calificaciones"][modulo]["otros"].append(calificacion_otros)

            # Calcular la calificación total basada en los pesos
            total_calificacion = (0.60 * calificacion_practico) + (0.30 * calificacion_teorico) + (0.10 * calificacion_otros)
            info["Calificaciones"][modulo]["total"] = total_calificacion
            info["Progreso"][modulo] = True

            if total_calificacion < 60:
                info["Riesgo"] = True
                info["Malas Calificaciones"][modulo] += 1

                if info["Malas Calificaciones"][modulo] == 2:
                    info["Estado"] = "Expulsado"
                    estudiantes_a_eliminar.append(doc)
            else:
                info["Malas Calificaciones"][modulo] = 0  # Resetear si pasa
                info["Riesgo"] = False

        else:
            info["Progreso"][modulo] = True
            if all(info["Progreso"].values()):
                info["Estado"] = "Graduado"

    for doc in estudiantes_a_eliminar:
        del data["estudiantes"][nombre_salon][doc]

    reu.guardar_actualizar_json(data)
    time.sleep(1)
    print(f"Se actualizaron las calificaciones para el grupo {nombre_salon}.")
    time.sleep(3)
    reu.clear()
    
