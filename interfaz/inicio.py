import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import json

#primera pantalla
def primera_pantalla():
    inicio = tk.Tk()
    inicio.title("Mini Wase")
    inicio.geometry("600x600")
    inicio.configure(background="white")

    # Función para abrir la ventana de registro
    def abrir_registro():
        primera_pantalla.cerrar_ventana()
        registro()

    # Función para validar el inicio de sesión
    def iniciar_sesion():
        nombre = entry_usuario.get()
        contrasena = entry_contrasena.get()
        resultado = analizar(nombre, contrasena)
        if resultado:
            pantalla_menú()
        else:
            ventana_mensaje = tk.Toplevel()
            ventana_mensaje.title("Credenciales inválidas")
            ventana_mensaje.configure(background="white")
            ventana_mensaje.geometry("400x100")
            label_mensaje = Label(ventana_mensaje, text="El usuario o contraseña son incorrectos", background="yellow")
            label_mensaje.place(x=150, y=30)
            ruta_imagen = "Fotos/foto2.jpg"
            imagen = Image.open(ruta_imagen)
            imagen = imagen.resize((60, 60))  # Ajusta el tamaño de la imagen según tus necesidades
            img = ImageTk.PhotoImage(imagen)
            lbl_img = Label(ventana_mensaje, image=img)
            lbl_img.place(x=40, y=15)
            boton_cerrar = Button(ventana_mensaje, text="Cerrar", command=ventana_mensaje.destroy)
            boton_cerrar.place(x=150, y=60)
            ventana_mensaje.mainloop()

    # Cargar la imagen y mostrarla en un widget Label
    ruta_imagen = "Fotos/menu.jpg"
    imagen = Image.open(ruta_imagen)
    imagen = imagen.resize((600, 600))  # Ajusta el tamaño de la imagen
    img = ImageTk.PhotoImage(imagen)
    lbl_img = Label(inicio, image=img)
    lbl_img.place(x=0, y=0)

    # Botón para abrir la ventana de registro
    boton_registro = Button(inicio, text="Ingrese usuario y contraseña", width=25, command=abrir_registro)
    boton_registro.place(x=230, y=440)

    # Botón para iniciar sesión
    boton_iniciar = Button(inicio, text="Iniciar Sesión", command=iniciar_sesion)
    boton_iniciar.place(x=270, y=550)

    # Entradas de usuario y contraseña
    entry_usuario = Entry(inicio)
    entry_usuario.place(x=250, y=470)
    entry_contrasena = Entry(inicio, show="*")
    entry_contrasena.place(x=250, y=500)

    # Etiqueta de mensaje
    label_mensaje = Label(inicio, text="")
    label_mensaje.place(x=250, y=510)

    inicio.mainloop()

# Función para analizar las credenciales y validar el inicio de sesión
def analizar(nombre="", contrasena=""):
    resultado = False
    with open("inicio_sesion\credenciales.json", "r") as datos:
        credenciales = json.load(datos)
    contando = True
    contador = 0
    while contando:
        try:
            if credenciales["usuarios"][contador]["nombre"] == nombre and credenciales["usuarios"][contador]["contrasena"] == contrasena:
                resultado = True
            contador += 1
        except:
            contando = False
    return resultado

# Función para la segunda pantalla
def pantalla_menú():
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("Pantalla de menú")
    ventana_secundaria.geometry("600x600")

    # Cargar la imagen y mostrarla en un widget Label
    ruta_imagen = "Fotos/foto3.jpg"  # Asegúrate de proporcionar la ruta correcta y el nombre de la imagen
    imagen = Image.open(ruta_imagen)
    imagen = imagen.resize((600, 600))  # Ajusta el tamaño de la imagen según tus necesidades
    img = ImageTk.PhotoImage(imagen)
    lbl_img = Label(ventana_secundaria, image=img)
    lbl_img.place(x=0, y=0)
   # Botón para cargar mapa
    boton_crear = Button(ventana_secundaria, text="Cargar Mapa", bg="red")
    boton_crear.place(x=98, y=240)
    # Botón para seleccionar destino
    boton_selec = Button(ventana_secundaria, text="Seleccionar destino", bg="red")
    boton_selec.place(x=85, y=305)
    # Botón para planificar destino
    boton_plan = Button(ventana_secundaria, text="Planificar destino", bg="red")
    boton_plan.place(x=85, y=370)
    # Botón para guardar destino
    boton_save = Button(ventana_secundaria, text="guardar destino", bg="red")
    boton_save.place(x=270, y=240)
    # Botón para borrar destino
    boton_delete = Button(ventana_secundaria, text="Borrar destino", bg="red")
    boton_delete.place(x=270, y=305)
    # Botón para modificar mapa
    boton_mapa = Button(ventana_secundaria, text="Modificar mapa", bg="red")
    boton_mapa.place(x=270, y=370)
    # Botón para salir de menú
    boton_mapa = Button(ventana_secundaria, text="salir", bg="red")
    boton_mapa.place(x=462, y=240)

    ventana_secundaria.mainloop()

# Función para la ventana de registro
def registro():
    ventana_registro = tk.Toplevel()
    ventana_registro.title("Registro de usuario")
    ventana_registro.geometry("400x300")
    # Agrega aquí los elementos de la ventana de registro

# Ejecutar la primera pantalla
primera_pantalla() 