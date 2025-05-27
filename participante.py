
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


class Participante: #crear el diccionario con los precios por clase 
    precio_clase = {"Pintura": 6000, "Teatro": 8000, "Danza": 7000} 

    def __init__(self, nombre, edad, taller, clases): #definiendo el metodo q se utilza para la clase es decir donde van los atributos
        self.nombre = nombre
        self.edad = int(edad)
        self.taller = taller
        self.clases = int(clases)

    def calculando_pago(self):  #calcular cuanto debe pagar la persona
        precio = self.precio_clase.get(self.taller, 0) #llamar del init el precio segun el taller, no encuentra pone 0
