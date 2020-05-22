# Acceso de datos a la clase Contacto

# Librería para gestionar la entrada de los datos de la clase Contacto
import re
# Se importa la clase Contacto
from clasepia import Contacto

#Libreria para archivos CSV
import csv

#Aqui abro el archivo ContactosLibreta.
with open('ContactosLibreta.csv') as archivo_csv:
    #Aqui a el lector le digo que me mande los datos hasta que se tope con un "PIPE"
    lector_csv = csv.reader(archivo_csv, delimiter='|')
    #Inicio el contador de lineas, para poderlas  al final.
    contador_lineas = 0
    #Aqui se inicia secuencialmente para que al final me muestre los resultados.
    for linea_datos in lector_csv:
        #Aqui pido solo la primera linea osea, nickname, nombre...
        if contador_lineas == 0:
            print(f'Los nombres de las columnas son {", ".join(linea_datos)}')
        else:
            #Mostrar, dato por dato, los contenidos por linea_datos.
            print(f'\tNICKNAME: {linea_datos[0]}.')
            print(f'\tNOMBRE: {linea_datos[1]}.')
            print(f'\tCORREO: {linea_datos[2]}.')
            print(f'\tTELEFONO: {linea_datos[3]}.')
            print(f'\tFECHANAC: {linea_datos[4]}.')
            print(f'\tGASTOS: {linea_datos[5]}.')
            print(f'\t------------------------------------------')
        #Se incrementa el numero de lineas, pase lo que pase.
        contador_lineas += 1

    print(f'Procesadas {contador_lineas} lineas.')