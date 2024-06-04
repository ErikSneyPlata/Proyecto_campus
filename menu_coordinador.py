import coordinador

def menu_coordi():
    while True:
        print("************************************************************************")
        print("                           MENU CORDINADOR")
        print("************************************************************************\n")
        print("********************************************************")
        print("                   FASE INSCRIPCION")
        print("********************************************************")
        print("1.Registrar camper para el examan de admision")
        print("2.mostrar campers incritos")
        print("3.Modificar camper incrito")
        print("4.Retirar camper inscrito")
        print("5.Presentar pruebas de ingreso")
        print("6.Verificar candidatos rechazados")
        
        print("********************************************************")
        print("                     FASE MATRICULA")
        print("********************************************************")
        print("7.Pasar de inscritos a en espera de ingreso(SOLO APROBADOS EN EL EXAMEN)")
        print("8.Mostrar candidatos en espera de ingreso")
        print("9.Asignar salon a estudiantes en espera")
        
        print("********************************************************")
        print("                     FASE DESARROLLO")
        print("********************************************************")
        print("10. Mostrar grupos existentes")
        print("11. Mostrar estudiantes de un grupo")
        print("12. Asignar ruta para un grupo")
        
        print("***********************************************")
        print("14. REGRESAR --> Menu principal")
        print("***********************************************\n")
        
        opt=int(input("ingrese su opcion: "))
        if opt==1:
            coordinador.registrar_camper()
        elif opt==2:
            coordinador.mostrar_campers_inscritos()
        elif opt==3:
            coordinador.modificar_camper()
        elif opt==4:
            coordinador.retirar_camper()
        elif opt==5:
            coordinador.presentar_pruebas()
        elif opt==6:
            coordinador.rechazados()
        elif opt==7:
            coordinador.esperando_para_ingresar()
        elif opt==8:
            coordinador.mostrar_est_espera()
        elif opt==9:
            coordinador.asignar_salon()
        elif opt==10:
            coordinador.mostrar_grupos()
        elif opt==11:
            coordinador.mostrar_estudiantes_de_un_grupo()
        elif opt==12:
            coordinador.asignar_ruta()
        elif opt==13:
            coordinador.calificar_estudiantes()
        elif opt==14:
            return
        else:
            print("La opcion que ingresaste no esta disponible.")