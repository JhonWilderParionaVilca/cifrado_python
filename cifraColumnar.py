from tkinter import *

ventana = Tk()
textoSalida = StringVar()


def encrypt():
    matrix = createEncMatrix(len(clave.get()), cadena.get())
    print(matrix)
    keywordSequence = getKeywordSequence(clave.get())
    print(keywordSequence)
    ciphertext = "";
    for num in range(len(keywordSequence)):
        pos = keywordSequence.index(num + 1)
        for row in range(len(matrix)):
            if len(matrix[row]) > pos:
                ciphertext += matrix[row][pos]
    print(ciphertext)
    textoSalida.set(ciphertext)


def decrypt():
    matrix = createDecrMatrix(getKeywordSequence(clave.get()), cadena.get())
    plaintext = "";
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            plaintext += matrix[r][c]
    textoSalida.set(plaintext)


def createEncMatrix(width, message):
    r = 0
    c = 0
    matrix = [[]]
    for pos, ch in enumerate(message):
        matrix[r].append(ch)
        c += 1
        if c >= width:
            c = 0
            r += 1
            matrix.append([])

    return matrix


def createDecrMatrix(keywordSequence, message):
    width = len(keywordSequence)
    height = len(message) // width
    if height * width < len(message):
        height += 1
    matrix = createEmptyMatrix(width, height, len(message))
    pos = 0
    for num in range(len(keywordSequence)):
        column = keywordSequence.index(num + 1)
        r = 0
        while (r < len(matrix)) and (len(matrix[r]) > column):
            matrix[r][column] = message[pos]
            r += 1
            pos += 1
    return matrix


def createEmptyMatrix(width, height, length):
    matrix = []
    totalAdded = 0
    for r in range(height):
        matrix.append([])
        for c in range(width):
            if totalAdded >= length:
                return matrix
            matrix[r].append('')
            totalAdded += 1
    return matrix


def getKeywordSequence(keyword):
    sequence = []
    for pos, ch in enumerate(keyword):
        previousLetters = keyword[:pos]
        newNumber = 1
        for previousPos, previousCh in enumerate(previousLetters):
            if previousCh > ch:
                sequence[previousPos] += 1
            else:
                newNumber += 1
        sequence.append(newNumber)
    return sequence


#################


# ventana


ventana.title("CIFRADO DE TRANSPOCISIÓN COLUMNAR")
ventana.geometry("%dx%d+%d+%d" % (500, 600, 0, 0))
ventana.resizable(0, 0)  # evita la redimención de la ventana

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

cifrarButton = Button(miFrame, text="Cifrar", command=encrypt)
cifrarButton.grid(row=2, column=0, padx=10, pady=10)

descifrarButton = Button(miFrame, text="Descifrar", command=decrypt)
descifrarButton.grid(row=2, column=1, padx=10, pady=10)

salida = Entry(miFrame, text=textoSalida)
salida.grid(row=3, column=1, padx=20, pady=20)
salidaLabel = Label(miFrame, text="Tu texto es: ")
salidaLabel.grid(row=3, column=0, padx=10, pady=10)

ventana.mainloop()

    # print(encrypt("pleasetransferonemilliondollarstomyswissbankaccountsixtwotwo","MEGABUCK"))
