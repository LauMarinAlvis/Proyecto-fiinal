import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import math
import pandas as pd
import csv
import os 


archivo_csv = 'proyectos_construccion.csv'

def calcular_resultado(angulo, longitud):
    return math.tan(math.radians(angulo)) * float(longitud)

def cargar_datos():
    if os.path.isfile(archivo_csv):
        with open(archivo_csv, 'r') as f:
            reader = csv.DictReader(f)
            return list(reader)
    return []


def guardar_datos(datos):
    if datos:
        with open(archivo_csv, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=datos[0].keys())
            writer.writeheader()
            writer.writerows(datos)

def registrar_proyecto(datos, nombre, longitud):
    try:
        if not nombre or not longitud:
            messagebox.showwarning("Atencion", "ingrese nombre y longitud del proyecto")
            return datos
        
        angulo = random.uniform(30, 60)
        resultado = calcular_resultado(angulo, longitud)
        
        nuevo_proyecto = {
            'nombre': nombre,
            'angulo': round(angulo, 2),
            'longitud': longitud,
            'resultado': round(resultado, 2)
        }
        
        datos.append(nuevo_proyecto)
        guardar_datos(datos)
        messagebox.showinfo("OK", "Proyecto registrado")
        return datos
        
    except ValueError:
        messagebox.showerror("Atencion", "longitud debe ser un numerica")
        return datos
#siempre poner en los show dos cmentarios
def ver_proyecto(datos, num):
    try:
        if num < 1 or num > len(datos):
            messagebox.showwarning("atencion", f"no existe el numero {num}")  
            return
            

        proyecto = datos[num-1]
        info = (f"Proyecto #{num}\n"
            f"Nombre: {proyecto['nombre']}\n"
            f"Angulo: {proyecto['angulo']}°\n"
            f"Longitud: {proyecto['longitud']}\n"
            f"Resultado: {proyecto['resultado']}")
        

        messagebox.showinfo("info. del Proyecto", info)
        
    except ValueError:
        messagebox.showerror("atencion", "ingrese un dato numerico")

def eliminar_proyecto(datos, num):
    try:
        if num < 1 or num > len(datos):
            messagebox.showwarning("Atencon", f"No existe el proyecto numero {num}")
            return datos
            
        proyecto_eliminado = datos.pop(num-1)
        guardar_datos(datos)
        messagebox.showinfo(f"Proyecto '{proyecto_eliminado['nombre']}' eliminado")
        return datos
        
    except ValueError:
        messagebox.showerror("Error", "Debe ingresar un número valido")
        return datos

def mostrar_datos(datos, text_area):
    text_area.delete(1.0, tk.END)
    
    if not datos:
        text_area.insert(tk.END, "No hay proyectos registrados")
        return
    
    encabezados = ["#", "Nombre", "Angulo", "Longitud", "Resultado"]
    text_area.insert(tk.END, "\t".join(encabezados) + "\n")
    text_area.insert(tk.END, "-"*70 + "\n")
    
    for i, proyecto in enumerate(datos, 1):
        fila = [
            str(i),
            proyecto['nombre'],
            str(proyecto['angulo']),
            proyecto['longitud'],
            str(proyecto['resultado'])
        ]
        text_area.insert(tk.END, "\t".join(fila) + "\n")




ventana = tk.Tk()
ventana.title("Proyectos de construcción")

nombre_proyecto = tk.StringVar()
longitud = tk.StringVar()
datos = cargar_datos()

tk.Label(ventana, text="Nombre del proyecto").grid(row=0, column=0)
tk.Entry(ventana, textvariable=nombre_proyecto).grid(row=0, column=1)

tk.Label(ventana, text="Longitud").grid(row=1, column=0)
tk.Entry(ventana, textvariable=longitud).grid(row=1, column=1)

tk.Button(ventana, text="Registrar Proyecto", command=registrar_proyecto).grid(row=2, column=0)
tk.Button(ventana, text="Ver Proyecto", command=ver_proyecto).grid(row=2, column=1)
tk.Button(ventana, text="Eliminar Proyecto", command=eliminar_proyecto).grid(row=3, column=0)
tk.Button(ventana, text="Mostrar Todos", command=mostrar_datos).grid(row=3, column=1)

text_area = tk.text_area(ventana, width=80, height=15)
text_area.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

mostrar_datos()









ventana.mainloop()