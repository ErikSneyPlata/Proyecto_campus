import json
import funciones.rec_funcion as reu
import coordinador, trainer

def menu_reportes():
    while True:
        print("************************************************************")
        print("                     MENU REPORTES")
        print("************************************************************\n")
        print("1.Campers inscritos")
        print("2.Campers admitidos")
        print("3.Trainers actuales")
        print("4.campers en condicional")
        print("5.Campers y trainers en rutas de entrenamiento")
        print("6.cuantos campers perdieron y aprobaron cada uno de los modulos(por ruta y trainer)")
        print("***********************************************")
        print("7. REGRESAR --> Menu principal")
        print("***********************************************\n")        
        
        try:
            opt=int(input("ingrese su opcion: "))
            if opt==1:
                reu.clear()
                coordinador.mostrar_campers_inscritos()
            elif opt==2:
                reu.clear()
                coordinador.mostrar_est_espera()
            elif opt==3:
                reu.clear()
                trainer.mostrar_trainers()
            elif opt==4:
                reu.clear()
                mostrar_campers_condicional()
            elif opt==5:
                reu.clear()
                mostrar_rutas_entrenamiento()
            elif opt==6:
                reu.clear()
                mostrar_resultados_modulos()
            elif opt==7:
                reu.clear()
                return
            
        except ValueError:
            print("Por favor, ingrese un número válido.")
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")
        

def mostrar_campers_condicional():
    data = reu.leer_crear_json()
    print("************************************************************")
    print("              CAMPERS EN CONDICIONAL")
    print("************************************************************")
    
    for grupo, estudiantes in data["estudiantes"].items():
        for doc, info in estudiantes.items():
            if info.get("Estado") == "Condicional":
                print(f"Grupo: {grupo}, Documento: {doc}, Nombre: {info['Nombres']} {info['Apellidos']}")
    print(" ")
    reu.wait_for_keypress()
    reu.clear()

def mostrar_rutas_entrenamiento():
    data = reu.leer_crear_json()
    print("************************************************************")
    print("        CAMPERS Y TRAINERS EN RUTAS DE ENTRENAMIENTO")
    print("************************************************************")
    
    print("\nEstudiantes:")
    for grupo, estudiantes in data["estudiantes"].items():
        for doc, info in estudiantes.items():
            if "Ruta de aprendizaje" in info:
                print(f"Grupo: {grupo}, Documento: {doc}, Nombre: {info['Nombres']} {info['Apellidos']}, Ruta: {info['Ruta de aprendizaje']}")
    
    print("\nTrainers:")
    for trainer_id, info in data["trainers"].items():
        if "Ruta de entrenamiento" in info:
            print(f"Trainer ID: {trainer_id}, Nombre: {info['Nombres']} {info['Apellidos']}, Ruta: {info['Ruta de entrenamiento']}")
    print(" ")
    reu.wait_for_keypress()
    reu.clear()  
        
def mostrar_resultados_modulos():
    data = reu.leer_crear_json()
    print("************************************************************")
    print("  RESULTADOS DE CAMPERS EN MÓDULOS (POR RUTA)")
    print("************************************************************")
    
    resultados = {}

    for grupo, estudiantes in data["estudiantes"].items():
        for doc, info in estudiantes.items():
            ruta = info.get("Ruta de aprendizaje")
            if ruta:
                if ruta not in resultados:
                    resultados[ruta] = {"aprobados": 0, "reprobados": 0}
                for modulo, calificaciones in info.get("Calificaciones", {}).items():
                    if isinstance(calificaciones, dict) and "total" in calificaciones:
                        if calificaciones["total"] >= 60:
                            resultados[ruta]["aprobados"] += 1
                        else:
                            resultados[ruta]["reprobados"] += 1
    
    for ruta, resultado in resultados.items():
        print(f"\nRuta: {ruta}")
        print(f"Aprobados: {resultado['aprobados']}")
        print(f"Reprobados: {resultado['reprobados']}")
        
    reu.wait_for_keypress()
    reu.clear()

