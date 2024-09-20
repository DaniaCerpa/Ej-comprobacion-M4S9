def guardar_info(archivo, formato):
        """Crea un nuevo archivo con el nombre y formato especificados, escribiendo líneas de información. 
        Si el archivo ya existe, se captura una excepción FileExistsError y se informa al usuario.
        
        Args:
        archivo: nombre del archivo a crear\n
        formato: formato del archivo a crear
        """
        try:
            ruta = "./archivos/"
            nom_archivo = f"{archivo}.{formato}"
            path = ruta + nom_archivo
            
            archivo_nuevo =  open(path, "x")
            
            i=1
            while i<=5:
                archivo_nuevo.write(f"Datos de información en la línea {i}\n")
                i+=1
            archivo_nuevo.close()
        except FileExistsError:
            print(f"No es posible crear el archivo {archivo}.{formato} porque ya existe uno previo con este nombre.\nPorfavor intenta con otro nombre")



def agregar_info(archivo, formato):
        """Agrega nueva informacion a un archivo existente con el nombre y formato especificados. 
        Si el archivo con dicho nombre no existe, entonces lo crea.
        
        Args:
        archivo: nombre del archivo a crear\n
        formato: formato del archivo a crear
        """
        
        nuevas_lineas = ["Hola Mundo", 
                         "Este en una nueva línea en el archivo",
                         "agregando la segunda línea del archivo",
                         "finalizando la línea agregada"]
        
        try:
            ruta = "./archivos/"
            nom_archivo = f"{archivo}.{formato}"
            path = ruta + nom_archivo
            
            archivo_nuevo =  open(path, "a")
            for lineas in nuevas_lineas:
                archivo_nuevo.writelines(f"{lineas}\n")
            
            archivo_nuevo.close()
            
        except FileExistsError:
            print(f"No es posible crear el archivo {archivo}.{formato} porque ya existe uno previo con este nombre.\nPorfavor intenta con otro nombre")
    
    
    
    
def main():
    """Función principal del programa que entrega los parametros necesarios para la posterior ejecución de las funciones guadar_info() y agregar info().
    """
    nombre_archivo = "informacion"
    formato = "dat"    
    
    guardar_info(nombre_archivo, formato)   
    agregar_info(nombre_archivo, formato)
    
#Ejecución de la funcion para correr el programa
main()
        