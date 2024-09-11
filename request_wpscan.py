import subprocess
import re

def leer_urls(archivo):
    """Lee las URLs desde un archivo de texto y las retorna como una lista."""
    with open(archivo, 'r') as file:
        urls = [linea.strip() for linea in file.readlines() if linea.strip()]
    return urls

def limpiar_nombre_archivo(nombre):
    """Limpia caracteres no permitidos para nombres de archivos."""
    nombre_limpio = re.sub(r'[<>:"/\\|?*\s]', '_', nombre)
    return nombre_limpio

def ejecutar_wpscan(url, token):
    """Ejecuta el comando wpscan para una URL específica."""
    nombre_archivo = limpiar_nombre_archivo(url)
    comando = [
        'wpscan',
        '--url', url,
        '--random-user-agent',
        '--api-token', token,
        '-o', f'{nombre_archivo}_wspcan_output'
    ]
    try:
        subprocess.run(comando, check=True)
        print(f"Comando ejecutado para {url}")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando para {url}: {e}")

if __name__ == "__main__":
    archivo_urls = 'urls.txt'  # Reemplaza con la ruta a tu archivo de URLs
    api_token = '7prJZfRk4Kp4Yp2nraPmJZZkA2bZE23ON9thZmgs0Bc'  # Reemplaza con tu token API
    urls = leer_urls(archivo_urls)
    
    for url in urls:
        print(f"Escaneando {url} ... ")
        ejecutar_wpscan(url, api_token)
