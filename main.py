import requests
comuna_destino = 'LA SERENA'  # comuna asociada al envío
url = 'https://midas.minsal.cl/farmacia_v2/WS/getLocalesTurnos.php'
respuesta = requests.get(url, timeout=10)

farmacias = respuesta.json()
farmacias_comuna = []

for farmacia in farmacias:
    if farmacia['comuna_nombre'] == comuna_destino:
        farmacias_comuna.append(farmacia)

cantidad = len(farmacias_comuna)

print(f'Se encontraron {cantidad} farmacias de turno en {comuna_destino}.')