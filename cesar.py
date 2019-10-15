from tkinter import *

ventana = Tk()

#variables
abc = "abcdefghijklmnopqrstuvwxyz"
textoSalida = StringVar()


#funciones
def cifrarCadena():
    text_cifrado = ''
    for letra in cadena.get():
        suma = abc.find(letra) + int(clave.get())
        modulo = int(suma) % len(abc)
        text_cifrado = text_cifrado + str(abc[modulo])
    textoSalida.set(text_cifrado)

def descifrarCadena():
    text_cifrado = ''
    for letra in cadena.get():
        suma = abc.find(letra) - int(clave.get())
        modulo = int(suma) % len(abc)
        text_cifrado = text_cifrado + str(abc[modulo])
    textoSalida.set(text_cifrado)



#ventana
ventana.title("CIFRADO DE CESAR")
ventana.geometry("%dx%d+%d+%d" %(500,600,0,0))
ventana.resizable(0, 0) #evita la redimención de la ventana

miFrame = Frame(ventana)
miFrame.pack()

cadena = Entry(miFrame)
cadena.grid(row=0, column=1, padx=20, pady=20)
cadenaLabel = Label(miFrame, text="Ingrese la cadena: ")
cadenaLabel.grid(row=0, column=0, padx=10, pady=10)



clave = Entry(miFrame)
clave.grid(row=1, column=1, padx=20, pady=20)
claveLabel = Label(miFrame, text="Ingrese la clave: ")
claveLabel.grid(row=1, column=0, padx=10, pady=10)



cifrarButton = Button(miFrame, text="Cifrar", command = cifrarCadena)
cifrarButton.grid(row=2, column=0, padx=10, pady=10)

descifrarButton = Button(miFrame, text="descifrar", command = descifrarCadena)
descifrarButton.grid(row=2, column=1, padx=10, pady=10)

salida = Entry(miFrame,text=textoSalida)
salida.grid(row=3, column=1, padx=20, pady=20)
salidaLabel = Label(miFrame, text="Tu texto es: ")
salidaLabel.grid(row=3, column=0, padx=10, pady=10)


ventana.mainloop()
