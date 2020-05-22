#Programa que lea archivos CSV, y lo carga en un objeto, y lo almacena en una lista.

# Librería para acceder a archivos CSV
import csv
# Librería para manejar datos de tipo datetime
import datetime

# Clase para almacenar los incidentes
class  Contactos:
      def __init__(self,NICKNAME,NOMBRE,CORREO,TELEFONO,FECHANAC,GASTOS):
            self.NICKNAME = NICKNAME
            self.NOMBRE = NOMBRE
            self.CORREO = CORREO
            self.TELEFONO = TELEFONO
            self.datetime = FECHANAC
            self.GASTOS = GASTOS

# Lectura secuencial del archivo
with open('ContactosLibreta.csv') as archivo_csv:
    lector_csv = csv.reader(archivo_csv, delimiter='|')
    contador_lineas = 0
    # Creando una lista vacía.
    lista_contactos = []
    # Lectura secuencial.
    for linea_datos in lector_csv:
        if contador_lineas == 0:
            # Si es la primer línea, muestro los nombres de campo y no guardo nada
            # en la lista.
            print(f'Los nombres de columna son {", ".join(linea_datos)}')
        else:
            # Si son datos (línea uno y posteriores)...
            # Genero una instancia de la clase Incidente, y le proporciono al constructor
            # los valores leidos del archivo.
            # RETO: Aquí se convierte el primer valor a su equivalente datetime
            objeto_temporal = Contactos({linea_datos[0]},{linea_datos[1]},{linea_datos[2]},{linea_datos[3]},{linea_datos[4]},{linea_datos[5]})
            lista_contactos.append(objeto_temporal)

        # Se incrementa el número de líneas, pase lo que pase.
        contador_lineas += 1

    print(f'Procesadas {len(lista_contactos)} lineas.')

    # RETO: Modificar la clase para que la propiedad FECHA sea datetime, y no string. Proporcionar
    # la información contenida en {linea_datos[0]} como fecha al objeto. Todo lo demás queda igual.