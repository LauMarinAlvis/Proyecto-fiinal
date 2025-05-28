#3.1 Interfaz Gráfica (Tkinter)
#La interfaz debe permitir:
#- Registrar el nombre de la persona, edad, taller inscrito y número de clases tomadas.
#Valores por clase:
#Pintura = $6.000-Teatro = $8.000-Danza = $7.000-
# - Guardar los datos en un archivo .txt o .csv.

import tkinter as tk  
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText  
from PIL import ImageTk  

# importamos nuestras funciones y clases del archivo participante
from participante import (Participante, guardar_participante_csv, cargar_datos, obtener_estadisticas, generar_grafico_talleres)


def registrar_participante():  #guarda el participante con los datos del formulario
    nombre = entry_nombre.get()  #toma nombre de la caja
    edad = entry_edad.get()  #toma edad
    taller = combo_taller.get()  #toma taller seleccionado
    clases = entry_clases.get()  #toma cantidad de clases

    if not nombre or not edad or not taller or not clases:
        messagebox.showwarning("datos incompletos", "por favor completa todos los campos.")  #si falta algo
        return

    try:
        p = Participante(nombre, edad, taller, clases)   #crear el objeto participante
        guardar_participante_csv(p)   #guarda en el archivo CSV y uso la instacia delsitema
        messagebox.showinfo("OK", f"participante registrado:\n{p}")  #mensaje emegente de aviso
        limpiar_campos()  #limpiando los campos para otro ingreso de participante clase 
    except Exception as e:
        messagebox.showerror("Error", f"no se pudo registrar. \n{e}")  #muestra error si algo sale mal 

#https://www.youtube.com/watch?v=YTqDYmfccQU&t=36s 
#esta funcion me muestra en listado de todos los participantes
def mostrar_tabla_participantes():
    df = cargar_datos()  #cargamos los datos del archivo CSV usando pandas

    if df.empty:  #cuando el dataFrame está vacio sin datos
        messagebox.showinfo("No hay datos", "cero personas registradas.")  #mostramos un aviso
        return  

    ventana_tabla = tk.Toplevel(ventana)  #creamos una nueva ventana que emerge dentro de la ventana principal
    ventana_tabla.title("Participantes registrados")  
    ventana_tabla.geometry("700x500")  #tamaño de la ventana que nos va a mostrar

    tree = ttk.Treeview(ventana_tabla)  #creo un widget tipo tabla Treeview para mostrar los datos
    tree.pack(expand=True, fill="both")  #aqui se ubica y si le da el ancho para que ocupe toda la ventana

    # Agregamos las columnas al Treeview
    tree["columns"] = list(df.columns)   #usamos las columnas del DataFrame como nombres de columnas
    tree["show"] = "headings"  #mostramos los encabezados 

    for col in df.columns:  #por cada columna en los datos
        tree.heading(col, text=col)   #añado un titulo visible a esa columna
        tree.column(col, width=100)   #tambien establesco un ancho fijo para cada columna

    # Agregamos cada fila de datos a la tabla
    for _, row in df.iterrows():   # recorremos cada fila del DataFrame
        tree.insert("", tk.END, values=list(row))   # insertamos los valores de esa fila en la tabla

def mostrar_estadisticas():  #funion de resumen del archivo CSV 
    df = cargar_datos()  #añade o carga los datos del archivo CSV 
    resumen = obtener_estadisticas(df)  #aqui genero un resumen  
    text_area.delete("1.0", tk.END)  #borra texto anterior 
    text_area.insert(tk.END, resumen) #mutro un nuevo resumen
    

def mostrar_grafico():  # aqui el grafico de barras con cantidad por taller
    df = cargar_datos()  
    imagen_pil = generar_grafico_talleres(df)  #se usa pil pa crear grafico como imagen

    if imagen_pil:
        img_tk = ImageTk.PhotoImage(imagen_pil)  #convierte a imagen tkinter
        image_label.configure(image=img_tk)  #pone imagen en etiqueta
        image_label.image = img_tk  #guuarda referencia
    else:
        messagebox.showwarning("Sin datos", "No hay participantes registrados.")  #mensajee emerge

 

ventana = tk.Tk()  # Crea la ventana
ventana.title("Talleres artisticos")   #se pone titulo a la ventana

ventana.geometry("800x500")  
ventana.configure(bg="#FDF6EC")  #Color de fondo de ventana pricnipal


tk.Label(ventana, text="nombre:", bg="#FDF6EC").grid(row=0, column=0, sticky="e") 
entry_nombre = tk.Entry(ventana) 
entry_nombre.grid(row=0, column=1)  

tk.Label(ventana, text="edad:", bg="#FDF6EC").grid(row=1, column=0, sticky="e") 
entry_edad = tk.Entry(ventana)
entry_edad.grid(row=1, column=1)  

tk.Label(ventana, text="Taller/clase:", bg="#FDF6EC").grid(row=2, column=0, sticky="e") 
combo_taller = ttk.Combobox(ventana, values=["Pintura", "Teatro", "Danza"], state="readonly")  
combo_taller.grid(row=2, column=1)   

tk.Label(ventana, text="cclases tomadas:", bg="#FDF6EC").grid(row=3, column=0, sticky="e")          
entry_clases = tk.Entry(ventana) 
entry_clases.grid(row=3, column=1)  

tk.Button(ventana, text="Registrar", command=registrar_participante, bg="#90EE90").grid(row=4, column=0, pady=10)
tk.Button(ventana, text="ver estadisticas", command=mostrar_estadisticas, bg="#ADD8E6").grid(row=4, column=1)
tk.Button(ventana, text="Ver grafico", command=mostrar_grafico, bg="#FFB6C1").grid(row=4, column=2)
tk.Button(ventana, text="Ver inscrito", command=mostrar_tabla_participantes, bg="#DDA0DD").grid(row=4, column=3, padx=20)



ventana.mainloop()  

#https://www.youtube.com/watch?v=-JtyMKhZxXQ