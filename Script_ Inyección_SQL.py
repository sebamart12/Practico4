"""

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


"""

"""

import requests



# URL del login

url = "http://localhost:8080/AltoroJ/doLogin"



# Datos del login en el formato adecuado

params = {
    "uid": "' OR 1=1--", 
    "passw": "hola", 
    "btnSubmit": "Login"
}



# Realizar la solicitud POST sin seguir redirecciones

try:

    response = requests.post(url, data=params, allow_redirects=False)  # Evitar redirecciones automáticas

    

    # Verificar si el código de respuesta es una redirección (3xx)

    if response.status_code in [301, 302, 303, 307, 308]:

        # Acceder a la cabecera Location

        location = response.headers.get('Location')

        if location:

            print(f"Redirigido a: {location}")

        else:

            print("No se encontró la cabecera 'Location'.")

    else:

        print(f"Respuesta recibida con código: {response.status_code}")



except requests.exceptions.RequestException as e:

    print(f"Error en la conexión: {e}")

"""


import requests

import sys

# URL del login

url = "http://localhost:8080/AltoroJ/doLogin"





# Datos del login en el formato adecuado

paramsattack = {

    "uid": "' OR 1=1--", 

    "passw": "hola", 

    "btnSubmit": "Login"

}



paramsOk= {

	"uid": "admin",

	"passw": "admin",

	"btnSubmit": "Login"

}



paramsMalo={

	"uid": "adm",

	"passw": "hola",

	"btnSubmit": "Login"

}





def Login(params):

    # Realizar la solicitud POST sin seguir redirecciones

    try:

        response = requests.post(url, data=params, allow_redirects=False)  

        

        if response.status_code == 302:

            location = response.headers.get('Location')

            if location == "/AltoroJ/bank/main.jsp":

                print(f"1, Redirigido a: {location}")

                print(sys.exit(1))

            else:

                print(f" 0, {location}")

                sys.exit(0)

        else:

            print(f"Respuesta recibida con código: {response.status_code}")



    except requests.exceptions.RequestException as e:

        print(f"Error en la conexión: {e}")



# Llamar a la función Attack con los parámetros definidos



Login(paramsMalo)

