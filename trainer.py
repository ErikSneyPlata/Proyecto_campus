import json
import coordinador
import funciones.rec_funcion as reu
import time


def menu_trainer():
    while True:
        print("************************************************************************")
        print("                     MENU TRAINER")
        print("************************************************************************\n")
        print("********************************************************")
        print("              INSCRIPCION TRAINER")
        print("********************************************************")
        print("1. Registrar trainer")
        print("2. Modificar trainer")
        print("3. Retirar trainer")
        print("4. Asignar grupo a trainer")
        print("5. Mostrar trainers")
        
        print("********************************************************")
        print("         FASE DESARROLLO")
        print("********************************************************")
        print("6. Calificar a estudiantes de un grupo (POR MODULO)")
        print("7. Modificar notas de estudiante individualmente")
        print("8. Verificar estudiantes retirados por rendimiento académico")
        print("9. Retirar estudiante voluntariamente")
        print("***********************************************")
        print("10. REGRESAR --> Menu principal")
        print("***********************************************\n")

        try:
            opt = int(input("Ingrese su opción: "))
            if opt == 1:
                reu.clear()
                registrar_trainer()
            elif opt == 2:
                reu.clear()
                modificar_trainer()
            elif opt == 3:
                reu.clear()
                retirar_trainer()
            elif opt == 4:
                reu.clear()
                asignar_grupo_trainer()
            elif opt == 5:
                reu.clear()
                mostrar_trainers()
            elif opt == 6:
                reu.clear()
                coordinador.calificar_estudiantes()
            elif opt == 7:
                reu.clear()
                modificar_notas_estudiante()
            elif opt == 8:
                reu.clear()
                estudiantes_expulsados()
            elif opt == 9:
                reu.clear()
                retirar_voluntario_deuda_expulsion()
            elif opt == 10:
                reu.clear()
                return
            else:
                reu.clear()
                print("La opción que ingresaste no está disponible.")
        except ValueError:
            reu.clear()
            print("Por favor, ingrese un número válido.")
        except Exception as e:
            reu.clear()
            print(f"Ocurrió un error: {e}")
            
#datos de salones y horarios de salones de campus
#***************************************************************            
def guardar_logistica_campus(data):
    with open("json//campus.json","w") as guardar:
        json.dump(data,guardar,indent=4)
    print("\nGUARDANDO...\n")

def leer_logistica_campus():
    
    try:
        with open("json//campus.json","r") as file:
            archivo = json.load(file)
            return archivo
    except FileNotFoundError:
        #CREAR SALONES PARA REGISTRAR QUE GRUPO LO VA A USAR SIN REPETIRSE Y CUANDO SE MUESTRE LA INFORMACION DEL TRAINER SE MUESTRE
        return {
            "artemis":{
                "6AM":None,
                "10AM":None,
                "2PM":None
                       },
            "sputnik":{
                "6AM":None,
                "10AM":None,
                "2PM":None
                       },
            "kepler":{
                "6AM":None,
                "10AM":None,
                "2PM":None
                       }
        }
            
#***************************************************************
            
def registrar_trainer(): 
    while True:        
        data = reu.leer_crear_json()
        print("********************************************************")
        print("                   REGISTRO DE TRAINER")
        print("********************************************************")
        nombres = input("Ingrese los nombres: ")
        apellidos = input("Ingrese los apellidos: ")
        
        try:
            documento = int(input("Ingrese el número de documento de identificación: "))
        except ValueError:
            print("Número de documento inválido. Por favor, ingrese un número.")
            continue
        
        if data["trainers"].get(str(documento), None) is None:
            direccion = input("Ingrese la dirección de residencia: ")            
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
            
            estado = "Contratado"
            data["trainers"][str(documento)] = {
                "Nombres": nombres,
                "Apellidos": apellidos,
                "Direccion": direccion,
                "Telefonos movil": telefonos_movil,
                "Telefonos fijo": telefono_fijo,
                "Estado": estado,
                "Grupos":[],
            }
            print("***********************************************")
            reu.guardar_actualizar_json(data)
            print("Registro guardado correctamente.")
            print("***********************************************")
            time.sleep(2)
            reu.clear()
        else:
            print("***********************************************")
            print("Ya se encuentra registrado.")
            print("***********************************************")
            time.sleep(2)
            reu.clear()
            
        try:      
            rep = input("¿Desea agregar otro trainer? (1. Si, 2. No): ")
            if rep == '1': 
                reu.clear()
                continue
            elif rep == '2': 
                reu.clear()
                return
        except Exception: print("Opción no válida. Por favor, ingrese 1 para Sí o 2 para No.")
            
def modificar_trainer():
    data = reu.leer_crear_json()
    print("********************************************************")
    print("                   MODIFICAR CAMPER")
    print("********************************************************")
    
    doc = input("Ingrese el documento para modificar al trainer: ")
    
    if data["trainers"].get(doc, None) is not None:
        while True:
            print("\nEstos son los valores actuales del Trainer:")
            cont_mod_validas = 1
            for key, value in data["trainers"][doc].items():
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

            if opt == 1: data["trainers"][doc]["Nombres"] = input("Ingrese sus nombres: ")
            elif opt == 2: data["trainers"][doc]["Apellidos"] = input("Ingrese sus apellidos: ")
            elif opt == 3: data["trainers"][doc]["Direccion"] = input("Ingrese la dirección de residencia: ")
            elif opt == 4: data["trainers"][doc]["Acudiente"] = input("Ingrese el nombre del acudiente del camper: ")
            
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
    
def retirar_trainer():
    data = reu.leer_crear_json()
    print("************************************************************")
    print("                       RETIRAR TRAINER")
    print("************************************************************")
    
    doc = input("Ingrese el documento para retirar al camper: ")
    if data["trainers"].get(doc, None) is not None:
        try:
            opt = int(input("\n1. Renuncia\n2. Terminacion de contrato\n3. Cancelar\n\n¿Qué acción quieres realizar?\nIngrese su opción: "))
            if opt == 1:
                data["trainers"][doc]["Estado"] = "Renuncio"
                reu.guardar_actualizar_json(data)
                print("***********************************************")
                print("\nCambio de estado guardado correctamente.")
                print("***********************************************")
                time.sleep(2)
                reu.clear()
                
            elif opt == 2:
                data["trainers"][doc]["Estado"] = "Terminacion de contrato"
                reu.guardar_actualizar_json(data)
                print("***********************************************")
                print("\nCambio de estado guardado correctamente.")
                print("***********************************************")
                time.sleep(2)
                reu.clear()
            elif opt == 3: return    
            
            else:
                print("Opción no válida. Por favor, elige 1 o 2.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    else:
        print("***********************************************")
        print("No se encontró un Trainer con ese documento.")
        print("***********************************************")
        time.sleep(3)
        reu.clear()     
        
def asignar_horario_salon():
    data = reu.leer_crear_json()
    logistica = leer_logistica_campus()

    print("********************************************************")
    print("            ASIGNACION DE HORARIOS Y SALONES")
    print("********************************************************")
    coordinador.mostrar_grupos()
    print("\n")
    grupo_selec = input("Ingrese el nombre del grupo para asignar horario y salón: ")

    try:
        if grupo_selec not in data["estudiantes"]:
            raise ValueError(f"No se encontró el grupo '{grupo_selec}'.")

        cc = 1
        for salon, horarios in logistica.items():
            print(f"{cc}. Salon {salon}")
            cc += 1
        print(f"{cc}. Salir")

        while True:    
            elec_salon = ""
            elecccion = input("¿En qué salón deseas añadir un grupo? (1-3) ")
            if elecccion == "1": 
                elec_salon = "artemis"
                break
            elif elecccion == "2": 
                elec_salon = "sputnik"
                break
            elif elecccion == "3": 
                elec_salon = "kepler" 
                break
            elif elecccion == "4":
                return
            else: 
                print("Ingrese una opción válida.")

        print("Los horarios disponibles son:")
        if any(grupo is None for grupo in logistica[elec_salon].values()):
            for hora, grupo in logistica[elec_salon].items():
                if grupo is None:
                    print(f" - {hora}")
            elec_horario = input("¿Cuál horario deseas asignar para ese grupo (6AM, 10AM, 2PM)?: ")
            if elec_horario in logistica[elec_salon] and logistica[elec_salon][elec_horario] is None:
                logistica[elec_salon][elec_horario] = grupo_selec
                guardar_logistica_campus(logistica)
                print(f"Horario {elec_horario} asignado al grupo {grupo_selec} en el salón {elec_salon}.")
                time.sleep(3)
                reu.clear()
            else:
                print("La opción indicada no es válida o el horario ya está ocupado.")
        else:
            print("No hay horarios disponibles para este salón.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
    
    
def mostrar_trainers():
    data = reu.leer_crear_json()
    
    print("********************************************************")
    print("                LISTA TRAINERS REGISTRADOS")
    print("********************************************************")    

    cont=1
    lista_de_trainers=list(data["trainers"])
    cantidad_de_trainers=len(lista_de_trainers)
    if cantidad_de_trainers>0:
        for doc, info in data["trainers"].items():
            print(f"TRAINER {cont}:")
            print(f"Documento: {doc}")
            print(f"Nombres: {info["Nombres"]}")
            print(f"Apellidos: {info["Apellidos"]}")
            print(f"Direccion: {info["Direccion"]}")
            print(f"Telefonos movil: {info["Telefonos movil"]}")
            print(f"Telefonos fijo: {info["Telefonos fijo"]}")
            print(f"Estado: {info["Estado"]}\n")
            cont+=1
        reu.wait_for_keypress()
        reu.clear()
        return
    else:
        print("No hay trainers registrados")
        time.sleep(3)
        reu.clear()
     

def modificar_notas_estudiante():
    data = reu.leer_crear_json()

    if "estudiantes" not in data or not data["estudiantes"]:
        print("No hay grupos registrados.")
        return
    
    print("Grupos disponibles:")
    for grupo in data["estudiantes"]:
        print(grupo)
    
    grupo_seleccionado = input("Ingrese el nombre del grupo: ")
    
    if grupo_seleccionado not in data["estudiantes"]:
        print(f"No se encontró el grupo {grupo_seleccionado}.")
        return
    
    id_estudiante = input("Ingrese el número de identificación del estudiante: ")
    
    if id_estudiante not in data["estudiantes"][grupo_seleccionado]:
        print(f"No se encontró al estudiante con el número de identificación {id_estudiante} en el grupo {grupo_seleccionado}.")
        return
    
    estudiante = data["estudiantes"][grupo_seleccionado][id_estudiante]
    
    print(f"Información del estudiante:\nNombre: {estudiante['Nombres']} {estudiante['Apellidos']}\n")
    
    modulos = [
        "Fundamentos de programacion",
        "Programacion Web",
        "Programacion formal",
        "Bases de datos",
        "Ruta de aprendizaje"
    ]
    
    print("Módulos disponibles para calificar:")
    for i, modulo in enumerate(modulos, start=1):
        print(f"{i}. {modulo}")
    
    opcion = input("Seleccione el módulo a modificar (1-5): ")
    
    try:
        modulo_index = int(opcion) - 1
        if not 0 <= modulo_index < len(modulos):
            raise ValueError
    except ValueError:
        print("Opción no válida.")
        return
    
    modulo = modulos[modulo_index]
    
    calificacion = input(f"Ingrese la nueva calificación para {modulo} (0-100): ")
    
    try:
        calificacion = int(calificacion)
        if not 0 <= calificacion <= 100:
            raise ValueError
    except ValueError:
        print("Calificación no válida.")
        return
    
    estudiante["Calificaciones"][modulo] = calificacion
    
    reu.guardar_actualizar_json(data)
    
    print(f"Se actualizó la calificación del estudiante {estudiante['Nombres']} {estudiante['Apellidos']} en el módulo {modulo}.")

    time.sleep(3)
    reu.clear()

def estudiantes_expulsados():
    data = reu.leer_crear_json()  # Leer los datos del JSON
    expulsados = []

    for grupo, estudiantes in data["estudiantes"].items():
        for doc, info in estudiantes.items():
            if info.get("Estado") == "Expulsado" and info.get("Riesgo", False):
                expulsados.append({
                    "Documento": doc,
                    "Nombres": info["Nombres"],
                    "Apellidos": info["Apellidos"],
                    "Grupo": grupo
                })

    print("************************************************************")
    print("           Estudiantes expulsados por rendimiento")
    print("************************************************************")
    
    if expulsados:
        for estudiante in expulsados:
            print(f"Documento: {estudiante['Documento']}")
            print(f"Nombres: {estudiante['Nombres']}")
            print(f"Apellidos: {estudiante['Apellidos']}")
            print(f"Grupo: {estudiante['Grupo']}")
            print("------------------------------------------------------------")
        reu.wait_for_keypress()
        reu.clear()
    else:
        print("No hay estudiantes expulsados por rendimiento académico.")
        time.sleep(3)
        reu.clear()
        
    print("************************************************************")
    
def retirar_voluntario_deuda_expulsion():
    data = reu.leer_crear_json()
    print("************************************************************")
    print("           Retiro de camper de CAMPUSLANDS")
    print("************************************************************")
    
    doc = input("Ingrese el documento para retirar al camper: ")
    
    estudiante_encontrado = None
    grupo_encontrado = None
    
    # Buscar al estudiante en todos los grupos
    for grupo, estudiantes in data["estudiantes"].items():
        if doc in estudiantes:
            estudiante_encontrado = estudiantes[doc]
            grupo_encontrado = grupo
            break
    
    if estudiante_encontrado is not None:
        try:
            opt = int(input("\n1. Retiro Voluntario\n2. Expulsar\n3. Cancelar\n\n¿Qué acción quieres realizar?\nIngrese su opción: "))
            if opt == 1:
                estudiante_encontrado["Estado"] = "Retirado, tiene deuda"
                estudiante_encontrado["Deuda"] = 12000000
                
                reu.guardar_actualizar_json(data)
                print("***********************************************")
                print("\nCambio de estado guardado correctamente.")
                print("\nSe ha generado una deuda por el retiro voluntario.")
                
                print("***********************************************")
                time.sleep(2)
                reu.clear()
            elif opt == 2:
                estudiante_encontrado["Estado"] = "Expulsado"
                
                reu.guardar_actualizar_json(data)
                print("***********************************************")
                print("\nCambio de estado guardado correctamente.")
                print("***********************************************")
                time.sleep(2)
                reu.clear()
            elif opt == 3:
                return
                
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
    
def asignar_grupo_trainer():
    while True:
        mostrar_trainers()
        
        logistica=leer_logistica_campus()
        data=reu.leer_crear_json()
        try:
            doc=int(input("ingrese el documento del trainer al cual quiere agregarle grupo: "))
        except ValueError:
            print("Digita por favor un documento de id valido de numeros.")
        doc=str(doc)
        if doc in data["trainers"]:
            print("Lo siguiente son los grupos disponibles:")
            if len(logistica["grupos"]) !=0:
                for i in range(len(logistica["grupos"])):
                    print(f"{i+1}. {logistica["grupos"][i]}")
                    
                print(f"¿Cual grupo quiere asignar para el trainer verificado? (1-{(len(logistica["grupos"]))})")
                try:
                    elec_grupo=int(input("\nDigite su opcion: "))
                except ValueError:
                    print("Digita por favor numeros para que sea valido.")
                    
                data["trainers"][doc]["grupos"]=logistica["grupos"][elec_grupo-1]
                
                logistica["grupos"].pop(elec_grupo-1)
                
                guardar_logistica_campus(logistica)
                reu.guardar_actualizar_json(data)
                
                print(f"Se asigno el grupo a el trainer {data["trainers"][doc]["Nombres"]}")
                print(f"Grupos a su disposicion: {data["trainers"][doc]["grupos"]}\n")
                time.sleep(3)
                reu.clear()
                return
            else:
                print("\nNo hay grupos disponibles para agregar\n")
                time.sleep(3)
                reu.clear()
        else:
            print(f"Trainer con documento {doc} no fue encontrado o no existe.")
            time.sleep(3)
            reu.clear()
        

        
            
        
        
    