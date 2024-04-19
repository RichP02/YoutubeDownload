import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from pytube import YouTube

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

# Función para seleccionar archivo
def seleccionar_archivo():
    filetypes = (('text files', '*.txt'), ('All files', '*.*'))
    filename = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)
    # Obtener enlaces del archivo seleccionado
    enlaces = leer_enlaces_desde_txt(filename)
    # Descargar videos
    descargar_videos(enlaces, carpeta_destino)

# Función para leer enlaces desde archivo .txt
def leer_enlaces_desde_txt(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        return archivo.read().splitlines()

# Función para descargar videos desde enlaces
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

# Ventana root
root = tk.Tk()
root.geometry("700x250")
root.title('Descarga de videos de YouTube')
root.resizable(0, 0)

# Variables
link = tk.StringVar(root)
resultado = tk.StringVar(root)
carpeta_destino = "Descargas"

# Configurando grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

# Frame para el ingresar link
frame_link = ttk.Frame(root)
frame_link.pack(side='top', pady=10)

# Label y Entry para el nombre del video
label_nombre = ttk.Label(
    frame_link,
    text='Ingresa el link del video:',
    font=("Arial", 11)
)
label_nombre.pack(
    side='left',
    padx=10,
    pady=10
)
entry_nombre = ttk.Entry(
    frame_link,
    textvariable=link
)
entry_nombre.pack(
    side='left',
    padx=10,
    ipadx=170,
    ipady=5
)

# Frame para los botones de descarga
frame_descarga = ttk.Frame(
    root
)
frame_descarga.pack(
    side='top',
    pady=10,
    padx=10
)

# Botones de descarga
button_mp4 = ttk.Button(
    frame_descarga,
    text="Descargar Mp4",
    width=50,
    command=descarga_video
)
button_mp4.pack(
    side='left',
    padx=10,
    ipady=5
    # pady=10
)
button_mp3 = ttk.Button(
    frame_descarga,
    text="Descargar Mp3",
    width=50,
    command=descarga_audio
)
button_mp3.pack(
    side='left',
    padx=10,
    ipady=5
    # pady=10
)

# Frame para el botón de cargar archivo
frame_cargar_archivo = ttk.Frame(
    root
)
frame_cargar_archivo.pack(
    side='top',
    pady=10,
    padx=10
)

# Botón de cargar archivo .txt
button_file = ttk.Button(
    frame_cargar_archivo,
    text="Cargar Archivo .txt",
    width=50,
    command=seleccionar_archivo
)
button_file.pack(
    side='left',
    # padx=10,
    pady=10,
    ipady=5
)

# Frame para el resultado
frame_resultado = ttk.Frame(
    root
)
frame_resultado.pack(
    side='top',
    pady=10,
    padx=10
)

# Label para el resultado
label_resultado = ttk.Label(
    frame_resultado,
    textvariable=resultado,
    font=("Arial", 11)
)
label_resultado.pack(
    side='left',
    padx=10
)

root.mainloop()