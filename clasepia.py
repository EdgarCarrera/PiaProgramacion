# Define una clase.

# En una aplicación de tipo Agenda Personal, se tiene una entidad de datos
# llamada Contacto, mismo que será manejado a través de una clase.
# La clase tiene las siguientes propiedades.
# telefono: Es el número telefónico del contacto, y actúa como PK.
# nombre: Es el nombre completo del Contacto.
# correo: Es el correo electrónico del contacto.
# registro: Es la fecha de registro en que el contacto se registró.

# Debido a que la clase maneja un dato de tipo date, se importa la librería requerida.
import datetime

# Se declara una clase llamada contacto donde guardaremos 6 datos por cada usuario.
class Contacto:
  # Se declara un procedimiento constructor.
  # Aqui pondremos los datos que almacenaremos de nuestro contacto.
  def __init__(self,NICKNAME,NOMBRE,CORREO,TELEFONO,FECHANAC,GASTOS):
    self.NICKNAME = NICKNAME
    self.NOMBRE = NOMBRE
    self.CORREO = CORREO
    self.TELEFONO = TELEFONO
    self.datetime = FECHANAC
    self.GASTOS = GASTOS

print(Contacto)