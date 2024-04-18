import tkinter as tk
from tkinter import ttk
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

# Funciones
def descarga():
    try:
        youtubeObject = YouTube(link.get())
        youtubeObject.streams.get_highest_resolution().download()
        print("Descarga completada")
    except Exception as e:
        print("Error:", e)

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
    command=descarga
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
    width=50
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
    width=35
)
button_file.grid(
    column=2,
    row=1,
    sticky=tk.W,
    padx=5,
    pady=5
)


root.mainloop()
