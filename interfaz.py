#3.1 Interfaz Gráfica (Tkinter)
#La interfaz debe permitir:
#- Registrar el nombre de la persona, edad, taller inscrito y número de clases tomadas.
#Valores por clase:
#Pintura = $6.000-Teatro = $8.000-Danza = $7.000-
# - Guardar los datos en un archivo .txt o .csv.

import tkinter as tk  
from tkinter import ttk, messagebox


ventana = tk.Tk()  # Crea la ventana
ventana.title("Talleres artisticos")  #se pone titulo a la ventana

ventana.mainloop()