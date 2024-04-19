# Importa la clase YouTube de la biblioteca pytube
from pytube import YouTube

import grafico
link = grafico.link

def descarga(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.descarga()
    except:
        print("An error has occurred")
    print("Descarga completada")

descarga(link)

# Lee los enlaces de video desde un archivo de texto (cada enlace en una línea)
def leer_enlaces_desde_txt(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        return archivo.read().splitlines()

# Descarga los videos
def descargar_videos(enlaces, carpeta_destino):
    for enlace in enlaces:
        try:
            yt = YouTube(enlace)
            video = yt.streams.get_highest_resolution()
            video.download(output_path=carpeta_destino)
            print(f"Video descargado: {yt.title}")
        except Exception as e:
            print(f"Error al descargar el video {enlace}: {e}")


if __name__ == "__main__":
    archivo_enlaces = "url.txt"  # Nombre del archivo de texto con los enlaces
    carpeta_destino = "descargas"  # Carpeta donde se guardarán los videos

    enlaces = leer_enlaces_desde_txt(archivo_enlaces)
    descargar_videos(enlaces, carpeta_destino)
