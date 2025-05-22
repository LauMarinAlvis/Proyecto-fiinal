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

def registrar_proyecto():
    nombre = nombre_proyecto.get()
    longi = longitud.get()

    if not nombre or not longi:
        messagebox.showwarning("Atencion", "Ingres nombre y longitud del proyecto")
        return

    try:
        angulo = random.uniform(30, 60)
        resultado = calcular_resultado(angulo, longi)

        nuevo_proyecto = {
            'nombre': nombre,
            'angulo': round(angulo, 2),
            'longitud': longi,
            'resultado': round(resultado, 2)
        }

        datos.append(nuevo_proyecto)
        guardar_datos(datos)
        mostrar_datos()
        messagebox.showinfo("OK", "Proyecto registrado")

    except ValueError:
        messagebox.showerror("Error", "La longitud debe ser un numero")

def ver_proyecto():
    num = simpledialog.askinteger("Ver Proyecto", "ingrese el número del proyecto:")
    if num is None:
        return
    if num < 1 or num > len(datos):
        messagebox.showwarning("Atención", "numero fuera de rango")
        return

    proyecto = datos[num - 1]
    info = f"""
Proyecto #{num}
Nombre: {proyecto['nombre']}
Ángulo: {proyecto['angulo']}°
Longitud: {proyecto['longitud']}
Resultado: {proyecto['resultado']}
"""
    messagebox.showinfo("Datos del Proyecto", info)

def eliminar_proyecto():
    num = simpledialog.askinteger("Eliminar Proyecto", "ingrese el numero del proyecto a eliminar:")
    if num is None:
        return
    if num < 1 or num > len(datos):
        messagebox.showwarning("Atencion", "Numero fuera de rango")
        return

    eliminado = datos.pop(num - 1)
    guardar_datos(datos)
    mostrar_datos()
    messagebox.showinfo("Eliminado", f"Proyecto '{eliminado['nombre']}' fue eliminado")

def mostrar_datos():
    text_area.delete(1.0, tk.END)
    if not datos:
        text_area.insert(tk.END, "No hay proyectos registrados.")
        return

    encabezado = f"{'#':<5}{'Nombre':<20}{'Angulo':<10}{'Longitud':<15}{'Resultado':<15}\n"
    text_area.insert(tk.END, encabezado)
    text_area.insert(tk.END, "-" * 70 + "\n")

    for i, proyecto in enumerate(datos, 1):
        fila = f"{i:<5}{proyecto['nombre']:<20}{proyecto['angulo']:<10}{proyecto['longitud']:<15}{proyecto['resultado']:<15}\n"
        text_area.insert(tk.END, fila)


ventana = tk.Tk()
ventana.title("Proyectos de Cosntrucción")

datos = cargar_datos()

nombre_proyecto = tk.StringVar()
longitud = tk.StringVar()

tk.Label(ventana, text="mombre del proyecto").grid(row=0, column=0)
tk.Entry(ventana, textvariable=nombre_proyecto).grid(row=0, column=1)

tk.Label(ventana, text="Longitud").grid(row=1, column=0)
tk.Entry(ventana, textvariable=longitud).grid(row=1, column=1)

tk.Button(ventana, text="Registrar Proyecto", command=registrar_proyecto).grid(row=2, column=0)
tk.Button(ventana, text="Ver Proyecto", command=ver_proyecto).grid(row=2, column=1)
tk.Button(ventana, text="Eliminar Proyecto", command=eliminar_proyecto).grid(row=3, column=0)
tk.Button(ventana, text="Mostrar Todos", command=mostrar_datos).grid(row=3, column=1)

text_area = tk.Text(ventana, width=80, height=15)
text_area.grid(row=4, column=0, columnspan=2, pady=10)

mostrar_datos()



ventana.mainloop()
