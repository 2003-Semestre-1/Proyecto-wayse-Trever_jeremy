import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
def primera_pantalla():
    inicio = tk.Tk()
    inicio.title("Mini Wase")
    inicio.geometry("600x600")
    inicio.configure(background="white")

    # Función para imprimir un mensaje de despedida
    def salida():
        print("Gracias por usar el Mini Waze")

    # Función para realizar el código de registro
    def registro():
        print("Hacer código que pueda enviar a interfaz de registro")

    # Cargar la imagen y mostrarla en un widget Label
    ruta_imagen = "Fotos\menu.jpg"  # Asegúrate de proporcionar el nombre correcto y la extensión de la imagen
    imagen = Image.open(ruta_imagen)
    imagen = imagen.resize((600, 600))  # Ajusta el tamaño de la imagen según tus necesidades
    img = ImageTk.PhotoImage(imagen)
    lbl_img = Label(inicio, image=img)
    lbl_img.place(x=0, y=0)

    # Crear una funcion que redireccione al usuario a la siguiente ventana de regirtro de usuario
    boton1 = Button(inicio, text="precione aqui si desea ingresar al Waze", command=registro)
    boton1.place(x=240, y=550)

    # Crear una funcion que cierre el programa
    boton2 = Button(inicio, text="Precione aqui si desea cerrar el Waze", command=salida)
    boton2.place(x=270, y=550)

    inicio.mainloop()   