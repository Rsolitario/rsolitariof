import requests
import xml.etree.ElementTree as ET

# --- CONFIGURACIÓN ---
DOMINIO = "https://www.rsolitario.com"
LLAVE = "mi-codigo-secreto-123"
SITEMAP_URL = f"https://{DOMINIO}/sitemap.xml"

def enviar_a_indexnow():
    try:
        # 1. Obtener las URLs de tu sitemap
        r = requests.get(SITEMAP_URL)
        root = ET.fromstring(r.content)
        # Extraer todas las URLs (esto asume formato standard de sitemap)
        urls = [loc.text for loc in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]

        # 2. Preparar el envío para IndexNow
        data = {
            "host": DOMINIO,
            "key": LLAVE,
            "keyLocation": f"https://{DOMINIO}/{LLAVE}.txt",
            "urlList": urls
        }

        # 3. Enviar a Bing / IndexNow
        response = requests.post("https://www.bing.com/IndexNow", json=data)
        
        if response.status_code == 200:
            print(f"Éxito: Se enviaron {len(urls)} URLs a IndexNow.")
        else:
            print(f"Error al enviar: {response.status_code}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    enviar_a_indexnow()