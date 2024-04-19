import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from pytube import YouTube

# ventana root
root = tk.Tk()
root.geometry("700x150")
root.title('Download YouTube videos')
root.resizable(0, 0)
root.configure(background="#43394A")

# configurando grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Variables
link = tk.StringVar(root)
resultado = tk.StringVar(root)
carpeta_destino = "Descargas"

# Funciones
def descarga_video():
    try:
        yt = YouTube(link.get())
        video = yt.streams.get_highest_resolution()
        video.download(output_path=carpeta_destino)
        resultado.set("Descarga completada")
    except Exception as e:
        resultado.set("El link no esta correcto")

def descarga_audio():
    try:
        yt = YouTube(link.get())
        video = yt.streams.filter(only_audio=True).first()
        video.download(output_path=carpeta_destino)
        resultado.set("Descarga completada")
    except Exception as e:
        resultado.set("El link no esta correcto")

# Funcion leer archivo
def leer_enlaces_desde_txt(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        return archivo.read().splitlines()

def descargar_videos(enlaces, carpeta_destino):
    exito = True
    for enlace in enlaces:
        try:
            yt = YouTube(enlace)
            video = yt.streams.get_highest_resolution()
            video.download(output_path=carpeta_destino)
        except Exception as e:
            print(f"Error al descargar el video {enlace}: {e}")
            exito = False
    if exito:
        resultado.set("Descarga completada")
    else:
        resultado.set("Hubo un problema durante la descarga de algunos videos")

def seleccionar_archivo():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    # Obtener enlaces del archivo seleccionado
    enlaces = leer_enlaces_desde_txt(filename)
    # Descargar videos
    descargar_videos(enlaces, carpeta_destino)

# link
link_label = ttk.Label(
    root,
    text="Ingresa el link del video: ",
    background="#43394A",
    foreground="white",
    font=("Arial", 13)
)
link_label.grid(
    column=0,
    row=0,
    sticky=tk.W,
    padx=5,
    pady=20
)

link_entry = ttk.Entry(
    root,
    width=90,
    textvariable=link
)
link_entry.grid(
    column=1,
    row=0,
    sticky=tk.E,
    padx=5,
    pady=5,
    columnspan=2
)

# Botones
button_mp4 = ttk.Button(
    root,
    text="Mp4",
    width=50,
    command=descarga_video
)
button_mp4.grid(
    column=0,
    row=1,
    sticky=tk.W,
    padx=5,
    pady=5
)

button_mp3 = ttk.Button(
    root,
    text="Mp3",
    width=50,
    command=descarga_audio
)
button_mp3.grid(
    column=1,
    row=1,
    sticky=tk.W,
    padx=5,
    pady=5
)

button_file = ttk.Button(
    root,
    text="Cargar Archivo .txt",
    width=35,
    command=seleccionar_archivo
)
button_file.grid(
    column=2,
    row=1,
    sticky=tk.W,
    padx=5,
    pady=5
)

# Resultado
label_resultado = ttk.Label(
    root,
    text="",
    width=25,
    textvariable=resultado,
    background="#43394A",
    anchor="center",
    foreground="white"
)
label_resultado.grid(
    column=0,
    row=2,
    sticky="WE",
    padx=5,
    pady=5,
    columnspan=3
)

root.mainloop()