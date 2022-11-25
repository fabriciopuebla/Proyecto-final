import tkinter
from PIL import Image, ImageTk
from tkinter import filedialog, PhotoImage

def buscar_nueva():
    global imagen
    global img
    archivo = filedialog.askopenfilename(filetypes=[("Image", ("*.jpg", "*.png"))])
    img = Image.open(archivo)
    img = img.resize((500,300))
    img = ImageTk.PhotoImage(img)
    imagen = tkinter.Label(ventana, image=img)
    imagen.image = img
    imagen.pack()
    
ventana = tkinter.Tk()
ventana.title("Visor de Imagenes")
ventana.geometry("700x500+20+20")
ventana.resizable(0,0)
ventana.configure(bg="#E80707")

titulo = tkinter.Label(ventana, text="Proyecto Final")
titulo.pack()

btn = tkinter.Button(ventana, text="Buscar imagen", height=3, width=10, command= buscar_nueva)
btn.configure(bg="grey")
btn.pack()


ventana.mainloop()
