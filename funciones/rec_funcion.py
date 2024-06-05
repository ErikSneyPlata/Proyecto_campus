import json
import random
import os


def lecturaArchivos(ruta): #recibe la ruta del archivo a leer
    with open(ruta, encoding='utf-8') as mostrar:
        print(mostrar.read())

def input_opcion():
    n = input("Ingrese su opcion: ") # En string
    return n
    
def leer_crear_json():
    try:
        with open("json\\datos.json","r") as lectura:
            datos = json.load(lectura)
            return datos
    except FileNotFoundError:
        return { 
                "campers":{
                    },
                "en espera":{
                    },
                "estudiantes":{
                    },
                "trainers":{
                    }
                }

def guardar_actualizar_json(datos):
    with open("json\\datos.json","w") as guardar:
        json.dump(datos,guardar, indent=4)
    print("\nGUARDANDO...\n")
    

def clear():
    if os.name == 'nt':  # Si el sistema es Windows
        os.system('cls')
    else:  # Para sistemas tipo Unix (Linux, Mac)
        os.system('clear')
        
def wait_for_keypress():
    print("Presiona cualquier tecla para continuar...")
    os.system('pause >nul')