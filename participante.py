
#Debe implementar una clase llamada Participante que almacene los datos registrados y
#calcule el total a pagar.
#3.3 Reporte (Pandas + Matplotlib)
#El proyecto debe incluir un pequeño análisis con Pandas que indique:
# Cuántas personas se registraron.- El promedio de edad.
# Cuál fue el taller más popular
#
#
#
import pandas as pd  
import matplotlib.pyplot as plt  
import os  
import io  



# Clase que representa una persona que se registra en un taller 
#https://www.youtube.com/watch?v=JVNirg9qs4M un super video omita los muñequitos profe.
class Participante:#crear el diccionario con los precios por clase 
    precio_clase = {"Pintura": 6000, "Teatro": 8000, "Danza": 7000} 

    def __init__(self, nombre, edad, taller, clases):  #definiendo el metodo q se utilza para la clase es decir donde van los atributos
        self.nombre = nombre  #guarda el nombre
        self.edad = int(edad)  #guarda edad convertida a numero
        self.taller = taller  #guard el taller elegido
        self.clases = int(clases)  #guarda cuantas clases toma, como numero
        self.total = self.calcular_pago()  #calcula el total a pagar por el nuemero de clases

    def calcular_pago(self):  ##calcular cuanto debe pagar la persona
        precio = self.precio_clase.get(self.taller, 0)  #llamar del init el precio segun el taller, no encuentra pone 0
        return self.clases * precio  # Multiplica clases por precio para obtener total

    def to_dict(self):  #convierte el objeto en diccionario para guardarlo como fila en archivo
        return {
            "Nombre": self.nombre, #variables del dicionario
            "Edad": self.edad,
            "Taller": self.taller,
            "Clases": self.clases,
            "Total": self.total
        }

    def __str__(self):  #sto es para cuando imprimimos el objeto en consola
        return f"{self.nombre} ({self.edad} años) - {self.taller}, {self.clases} clases → ${self.total}"

#verifica si existe un archivo real 
def archivo_existe(ruta):
    return os.path.isfile(ruta)  #me envia true si existe el archivo ok

#guardondo un participante nuevo en el archivo CSV
def guardar_participante_csv(participante, ruta="datos_talleres.csv"):
    try:
        df = pd.DataFrame([participante.to_dict()])  #convierte a dataframe
        if not archivo_existe(ruta):  #si no existe el archivo se crea con encabezado
            df.to_csv(ruta, mode='w', header=True, index=False)
        else:  #ya existe entonces agrega sin repetir encabezado
            df.to_csv(ruta, mode='a', header=False, index=False)
    except Exception as e:
        print(f"[ERROR] no se puede guardar: {e}")  #muestra el error 

#cargand los datos desde el archivo CSV
def cargar_datos(ruta="datos_talleres.csv"): #se define la funcion para cargas los dartos al archivo csv con nombre datos_talleres
    try:
        return pd.read_csv(ruta)  #carga el archivo como tabla
    except FileNotFoundError:  
        return pd.DataFrame(columns=["Nombre", "Edad", "Taller", "Clases", "Total"])  #retorna vacio si no hay archivo


#- Cuántas personas se registraron.
# - El promedio de edad.
#- Cuál fue el taller más popular.
# haceun resumen con cantidad de personas edad promedio y taller mas popular
def obtener_estadisticas(df):
    if df.empty:  # Si no hay datos
        return "sin datos registrados" 

    cantidad = len(df)  # Cuantos participantes hay
    promedio_edad = df["Edad"].mean()  # Promedio de edad
    taller_popular = df["Taller"].value_counts().idxmax()  # taller con mas inscritos


    return (f"Participantes registrados: {cantidad}\n"
        f"Edad promedio: {promedio_edad:.2f} años\n"
        f"Taller mas popular: {taller_popular}")

