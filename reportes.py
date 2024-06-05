import json
import funciones.rec_funcion as reu
import coordinador, trainer

def menu_trainer():
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
            
        elif opt==5:
            reu.clear()
            
        elif opt==6:
            reu.clear()
            
        elif opt==7:
            reu.clear()
            return
        

        
        
        
        