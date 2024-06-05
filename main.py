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
        print("¿Que tipo de usuario eres?\n1. MODULO CAMPERS\n2. MODULO TRAINERS\n3. MODULO REPORTES\n4. SALIR")
        try:
            opcion = int(input("\n\nIngrese su eleccion(1-4): "))
            if opcion == 1:
                reu.clear()
                menu_coordinador.menu_coordi()
            elif opcion == 2:
                reu.clear()
                trainer.menu_trainer()
            elif opcion == 3:
                reu.clear()
                reportes.menu_reportes()
            elif opcion == 4:
                reu.clear()
                print("SALIENDO...")
                time.sleep(3)
                reu.clear()
                print("ADIOS.")
                time.sleep(2)
                break 
            else: 
                print("Opcion no valida")
                time.sleep(1)
                reu.clear()
        except Exception:
            print("Error introducciste un valor no valido")
            time.sleep(1)
            reu.clear()
main()
