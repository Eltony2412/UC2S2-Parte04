def listar_personas(nombre):
    archivo = open(nombre, "rt")
    datos = archivo.read()
    print(datos)
    
def agregar_personas(nombre, conteNuevo):
    archivo = open (nombre, "at")
    archivo.write("\n"+conteNuevo)
    archivo.close()