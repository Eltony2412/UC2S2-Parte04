import Funciones_modular

i = 1
while i<3:
    login = input ("Ingresar su login: ")
    clave = input ("Ingresa su clave: ")
    
    archivo1 = open("login.txt", "rt")
    loginTXT = archivo1.read()
    
    archivo2 = open ("clave.txt", "rt")
    claveTXT = archivo2.read()
    
    if login == loginTXT and clave == claveTXT:
        while True:
            print ("\n*MENU*")
            print ("1. Listar personas")
            print ("2. Agregar personas")
            print ("3. Salir")
            
            opc = input ("\nIngrese una opcion: ") 
    
    
            if opc == "1":
                print("\n**DNI**")
                Funciones_modular.listar_personas("dni.txt")
                print("\n**APELLIDOS**")
                Funciones_modular.listar_personas("apellido.txt")
                print("\n**NOMBRES**")
                Funciones_modular.listar_personas("nombre.txt")
            elif opc == "2":
                nombreNew = input ("Nombre nuevo: ")
                apellidoNew = input ("Apellido nuevo: ")
                dniNew = input ("DNI nuevo: ")
                
                Funciones_modular.agregar_personas("nombre.txt", nombreNew)
                Funciones_modular.agregar_personas("apellido.txt", apellidoNew)
                Funciones_modular.agregar_personas("dni.txt", dniNew)
                print("*PERSONA AGREGADA*")
            elif opc == "3":
                break
            else:
                print("\nOPCION INVALIDA")
        break
    else:
        print("\nACCESO DENEGADO \n TIENE UN INTENTO MAS")
        
    i += 1