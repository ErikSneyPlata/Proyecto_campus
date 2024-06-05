import coordinador, menu_coordinador
import reportes
import trainer
import funciones.rec_funcion as reu
import time

def main():
    data={}
    while True:
        print("               Bienvenidos a CAMPUSLANDS\n")
        print("************************************************************")
        print("                     MENU PRINCIPAL")
        print("************************************************************")

        opcion = int(input("Que tipo de usuario eres:\n1.CORDINADOR\n2.TRAINER\n3.CAMPER\n4.SALIR\n\nIngrese su eleccion: "))
        if opcion == 1:
            reu.clear()
            menu_coordinador.menu_coordi()
        elif opcion == 2:
            trainer.menu_trainer()
        elif opcion == 3:
            reu.clear()
            reportes.menu_camper()
        elif opcion == 4:
            reu.clear()
            print("SALIENDO...")
            time.sleep(3)
            reu.clear()
            print("ADIOS.")
            time.sleep(2)
            break 

main()
