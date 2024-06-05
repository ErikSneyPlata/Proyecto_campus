import security_coordi as security
import coordinador
import funciones.rec_funcion as reu
import time

logo = """\033[96m
______________________________________________________________________________________________

 ██████  █████  ███    ███ ██████  ██    ██ ███████ ██       █████  ███    ██ ██████  ███████ 
██      ██   ██ ████  ████ ██   ██ ██    ██ ██      ██      ██   ██ ████   ██ ██   ██ ██      
██      ███████ ██ ████ ██ ██████  ██    ██ ███████ ██      ███████ ██ ██  ██ ██   ██ ███████ 
██      ██   ██ ██  ██  ██ ██      ██    ██      ██ ██      ██   ██ ██  ██ ██ ██   ██      ██ 
 ██████ ██   ██ ██      ██ ██       ██████  ███████ ███████ ██   ██ ██   ████ ██████  ███████ 
                                                                                             
______________________________________________________________________________________________
                                                                                                                                                                                            
        \033[96m"""

def main_principal():
    while True:
        
        print(logo,"\n")
        print("Estas a punto de introducirte en el mundo de la programacion.\n")
        print("¿Quieres ser un futuro programador? INSCRIBETE YA...")
        print("______________________________________________________________________________________________")
        op=input("1. Sistema de campus (INGRESAR)\n2. Registrarte para las pruebas de ingreso\n3. Salir de Campuslands\n\nDIGITA TU OPCION: ")
        if op =="1":
            reu.clear()
            security.security_coordinacion()
        elif op=="2":
            reu.clear()
            coordinador.registrar_camper()
        elif op=="3":
            reu.clear()
            print("GRACIAS POR USAR NUESTROS SERVICIOS.")
            time.sleep(2)
            reu.clear()
            print("Vuelve pronto, te esperamos...")
            time.sleep(1)
            reu.clear()
            print("ADIOS.")
            time.sleep(2)
            reu.clear()
            break
        
main_principal()