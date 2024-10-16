import requests

import sys


url = "http://localhost:8080/AltoroJ/api/login"

# Uploads del login

params = {"username": "' OR 1=1--", "password": "hola"}

# Realizar la solicitud POST

try:
    response = requests.post(url, json=params)
    # Si la respuesta es exitosa (código 200)

    if response.status_code == 200:
        response_json = response.json()
        print("Login válido:", response_json["success"])
        sys.exit(1)  # Login válido, retornar exit code 1

    # Si la respuesta es un error 400 (credenciales inválidas)

    elif response.status_code == 400:
        response_json = response.json()
        print("Login inválido:", response_json["error"])
        sys.exit(0)  # Login inválido, retornar exit code 0


except requests.exceptions.RequestException as e:

    print(f"Error al conectar con la API: {e}")
    sys.exit(0)