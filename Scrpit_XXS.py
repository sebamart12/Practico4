import requests

import urllib.parse

import sys

# URL de la página vulnerable

url = 'http://localhost:8080/AltoroJ/search.jsp'

# Payload con el XSS que envías en la query

payload = "<script>alert('Hola, soy un script');</script>"


encoded_payload = urllib.parse.quote(payload)

full_url = f"{url}?query={encoded_payload}"

response = requests.get(full_url)

if response.status_code == 200:
    html_content = response.text
    if payload in html_content:
        sys.exit(1)
    else:
         sys.exit(0)

else:
    print(f"Error en la petición: Código {response.status_code}")