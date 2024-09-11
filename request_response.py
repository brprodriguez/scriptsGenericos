import requests

# Definimos el User-Agent que queremos usar en las solicitudes
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0"

def leer_urls(archivo):
    """Lee las URLs desde un archivo de texto y las retorna como una lista."""
    with open(archivo, 'r') as file:
        urls = [linea.strip() for linea in file.readlines() if linea.strip()]
    return urls

def consultar_urls(urls):
    """Realiza solicitudes HTTP a cada URL y muestra el resultado."""
    headers = {'User-Agent': USER_AGENT}
    for url in urls:
        try:
            respuesta = requests.get(url, headers=headers)
            print(f"URL: {url}")
            print(f"Estado: {respuesta.status_code}")
            print(f"Contenido: {respuesta.text[:200]}...")  # Muestra solo los primeros 200 caracteres del contenido
            print("-" * 40)
        except requests.RequestException as e:
            print(f"URL: {url}")
            print(f"Error: {e}")
            print("-" * 40)

if __name__ == "__main__":
    archivo_urls = 'urls.txt'  # Reemplaza con la ruta a tu archivo de URLs
    urls = leer_urls(archivo_urls)
    consultar_urls(urls)

