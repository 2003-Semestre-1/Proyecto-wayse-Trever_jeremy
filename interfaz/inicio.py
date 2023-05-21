import tkinter as tk
from tkinter import *
def menu():
    inicio = tk.Tk()
    inicio.title("Mini Wase")
    inicio.geometry("600x600")
    inicio.configure(background="white")

    def salida():
        print("gracias por usar el Mini Waze")

    def registro():
        print("hacer código que pueda enviar a interfaz de registro")

    etiqueta = Label(inicio, text="bienvenido al Mini Wase. ¿Desea ingresar?")
    etiqueta.place(x=2, y=550)

    #img = PhotoImage(file="Fotos\menu.jpg")
    #lbl_img = Label(inicio, image=img)
    #lbl_img.place(x=0, y=0)
    
    boton1 = Button(inicio, text="si", command=registro)
    boton1.place(x=240, y=550)

    boton2 = Button(inicio, text="no", command=salida)
    boton2.place(x=270, y=550)

    inicio.mainloop()
