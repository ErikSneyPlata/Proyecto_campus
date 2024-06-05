import funciones.rec_funcion as reu
import menu_coordinador
import main_coordinacion as principal
import json
import time

def leer_trabajadores_coordinacion():
    try:
        with open("json//empleados_coordinacion.json","r") as leer_coordinacion:
            archivo=json.load(leer_coordinacion)
            return archivo
    except FileNotFoundError:
        users=[
            {
            "usuario":"JefeMaestro",
            "contrasena":"campus2024"
            }
        ]
        return users
        
def guardar_trabajadores_coordinacion(data):
    with open("json//empleados_coordinacion.json","w") as guardar_coordinacion:
            json.dump(data, guardar_coordinacion, indent=4)
    


def security_coordinacion():
    users=leer_trabajadores_coordinacion()
    guardar_trabajadores_coordinacion(users)
    
    bandera=True
    while bandera:
        try:
            print("************************************************************************")
            print(" BIENVENIDO, ESTE ES EL SISTEMA DE INGRESO PARA COORDINACION ACADEMICA")
            print("************************************************************************")
            print("\n¿Deseas ingresar como coordinador? \n1. Si\n2. No\n")
            interaccion = input("Seleccione una opcion: ")
            print("********************************************************")
            if interaccion =="1":
                persona_coordinacion=input("ingrese su usuario de Coordinacion academica: ")
                for verificacion in users:
                    if persona_coordinacion == verificacion["usuario"]:
                        contraseña =input("Digite la clave: ")
                        if contraseña == verificacion["contrasena"]:
                            print("\nCARGANDO SISTEMA...")
                            time.sleep(2)
                            reu.clear()
                            principal.main()
                            
                        else:
                            print("********************************************************")
                            print("\nCONTRASEÑA INCORRECTA, INTENTALO NUEVAMENTE.\n")
                            print("********************************************************")
                            time.sleep(2)
                            reu.clear()
                            
                            
                        
            if interaccion =="2":
                time.sleep(2)
                reu.clear()
                return 
        except Exception as error:
            print("\nla opcion que ingresaste no es valida\n")
            
