# Acceso de datos a la clase Contacto

# Librería para gestionar la entrada de los datos de la clase Contacto
import re
# Se importa la clase Contacto
from clasepia import Contacto

# Módulo para poder ejecutar tareas directas en el sistema operativo.
import os
# Módulo para trabajar con expresione regulares
import re

# Se establece una función para borrar pantalla.
# Se usa, expresión lambda, que es equivalente a:
# def clear():
#   os.system('cls')
LimpiarPantalla = lambda: os.system('cls') #on Windows System
linea_datos=[]

# Validador de expresiones regulares
# _txt es el texto a vlidar.
# _regex es el patrón de expresión regular a validar.
# Retorna True si _txt cumple con el patrón definido en _regex
# Retrona False si no es así.
def RegEx(_txt,_regex):
    coincidencia=re.match(_regex, _txt)
    return bool(coincidencia)

def principal():
    while (True):
        LimpiarPantalla()
        print("LISTA DE COTACTOS")
        print(" ")
        print("[1] Agregar un contacto.")
        print("[2] Buscar un contacto.")
        print("[3] Eliminar un contacto.")
        print("[4] Mostrar contactos.")
        print("[5] Serializar datos.")
        print("[0] Salir.")
        opcion_elegida = input("¿Que deseas hacer?  > ")
        if RegEx(opcion_elegida,"^[123450]{1}$"):
            if opcion_elegida=="0":
                print("GRACIAS POR UTILIZAR EL PROGRAMA")
                break
            if opcion_elegida=="1":
                print("Llamar procedimiento para la acción")
            if opcion_elegida=="2":
                print("Llamar procedimiento para la acción")
            if opcion_elegida=="3":
                print("Llamar procedimiento para la acción")
            if opcion_elegida=="4":
                print("Llamar procedimiento para la acción")
                import re
                from clasepia import Contacto

                import csv

                with open('ContactosLibreta.csv') as archivo_csv:
                    lector_csv = csv.reader(archivo_csv, delimiter='|')
                    contador_lineas = 0
                    for linea_datos in lector_csv:
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
                        contador_lineas += 1
                    print(f'Procesadas {contador_lineas} lineas.')
            if opcion_elegida=="5":
                print("Llamar procedimiento para la acción")

            input("Pulsa enter para contunuar...")
        else:
            print("Esa respuesta no es válida.")
            input("Pulsa enter para contunuar...")

principal()

#AVANCE DEL PIA