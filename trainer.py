import json
import coordinador
import funciones.rec_funcion as reu


def menu_trainer():
        print("************************************************************************")
        print("                     MENU TRAINER")
        print("************************************************************************\n")
        print("********************************************************")
        print("              INSCRIPCION TRAINER")
        print("********************************************************")
        print("1.Registrar trainer")
        print("2.Modificar trainer")
        print("3.Retirar trainer")
        print("4.asignar horario y salon de clases a trainer")
        print("5.mostrar trainers")
        
        print("********************************************************")
        print("         FASE DESARROLLO")
        print("********************************************************")
        print("6. Calificar a estudiantes de un grupo (POR MODULO)")
        print("7. Modificar notas de estudiante individualmente")
        print("8. verificar estudiantes retirados por rendimiento academico")
        print("9. Retirar estudiante voluntariamente")
        print("***********************************************")
        print("14. REGRESAR --> Menu principal")
        print("***********************************************\n")

        opt=int(input("ingrese su opcion: "))
        if opt==1:
            registrar_trainer()
        elif opt==2:
            modificar_trainer()
        elif opt==3:
            retirar_trainer()
        elif opt==4:
            asignar_horario_salon()
        elif opt==5:
            mostrar_trainers()
        elif opt==6:
            coordinador.calificar_estudiantes()
        elif opt==7:
            modificar_notas_estudiante()
        elif opt==8:
            estudiantes_expulsados()
        elif opt==9:
            retirar_voluntario_deuda()
        elif opt==10:
            return
        else:
            print("La opcion que ingresaste no esta disponible.")
            
#***************************************************************            
def guardar_logistica_campus(data):
    with open("json//campus.json","r") as guardar:
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
            data["campers"][str(documento)] = {
                "Nombres": nombres,
                "Apellidos": apellidos,
                "Direccion": direccion,
                "Telefonos movil": telefonos_movil,
                "Telefonos fijo": telefono_fijo,
                "Estado": estado,
                "Grupos":[],
                "Horario clases":[]
            }
            print("***********************************************")
            reu.guardar_actualizar_json(data)
            print("Registro guardado correctamente.")
            print("***********************************************")
        else:
            print("***********************************************")
            print("Ya se encuentra registrado.")
            print("***********************************************")
                  
        while True:
            rep = input("¿Desea agregar otro trainer para presentar examen? (1. Si, 2. No): ")
            if rep == '1': break
            elif rep == '2': return
            else: print("Opción no válida. Por favor, ingrese 1 para Sí o 2 para No.")
            
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
                
                break
            else:
                print("Opción no válida. Por favor, elige una opción del 1 al 7.")
    else:
        print("***********************************************")
        print("No se encontró un camper con ese documento.")
        print("***********************************************")
    
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
                
            elif opt == 2:
                data["trainers"][doc]["Estado"] = "Terminacion de contrato"
                reu.guardar_actualizar_json(data)
                print("***********************************************")
                print("\nCambio de estado guardado correctamente.")
                print("***********************************************")
            elif opt == 3: return    
            
            else:
                print("Opción no válida. Por favor, elige 1 o 2.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    else:
        print("***********************************************")
        print("No se encontró un Trainer con ese documento.")
        print("***********************************************")     
        
def asignar_horario_salon():
    data = reu.leer_crear_json()
    logistica = leer_logistica_campus()

    print("********************************************************")
    print("            ASIGNACION DE HORARIOS Y SALONES")
    print("********************************************************")
    coordinador.mostrar_grupos()
    print("\n")
    grupo_selec = input("Ingrese el nombre del grupo a asignar horario y salón: ")

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
        if len(logistica[elec_salon]) > 0:
            for horario in logistica[elec_salon]:
                print(horario)
        else:
            print("No hay horarios disponibles para este salón.")

        print(f"{cc}. Salir")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
    
    
def mostrar_trainers():
    data = reu.leer_crear_json()
    
    print("********************************************************")
    print("                 LISTA CAMPER REGISTRADOS")
    print("********************************************************")    

    cont=1
    lista_de_trainers=list(data["trainers"])
    cantidad_de_trainers=len(lista_de_trainers)
    if cantidad_de_trainers>0:
        for doc, info in data["trainers"].items():
            print(f"TRAINER {cont}:")
            print(f"Nombres: {info["Nombres"]}")
            print(f"Apellidos: {info["Apellidos"]}")
            print(f"Direccion: {info["Direccion"]}")
            print(f"Acudiente: {info["Acudiente"]}")
            print(f"Telefonos movil: {info["Telefonos movil"]}")
            print(f"Telefonos fijo: {info["Telefonos fijo"]}")
            print(f"Estado: {info["Estado"]}\n")
            cont+=1
        return
    else:
        print("No hay trainers registrados")
     

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


def estudiantes_expulsados():
    print("Conteo de estudiantes expulsados por rendimiento")
    
retirar_voluntario_deuda()