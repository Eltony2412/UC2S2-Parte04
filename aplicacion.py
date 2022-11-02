i = 1
while i<3:
    login = input ("Ingresar su login: ")
    clave = input ("Ingresa su clave: ")
    
    archivo1 = open("login.txt", "rt")
    loginTXT = archivo1.read()
    
    archivo2 = open ("clave.txt", "rt")
    claveTXT = archivo2.read()
    
    if login == loginTXT and clave == claveTXT:
        print ("Acceso aceptado")
        print ("*MENU*")
        print ("1. Listar personas")
        print ("2. Agregar personas")
        print ("3. Salir")
        break
        
    else:
        print("Acceso denegado")
        
    i += 1
    