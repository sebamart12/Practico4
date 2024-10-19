import requests

import sys

# URL del login

url = "http://localhost:8080/AltoroJ/doLogin"


paramsattack = {

    "uid": "' OR 1=1--", 

    "passw": "hola", 

    "btnSubmit": "Login"
}

def Login(params):
    try:
        response = requests.post(url, data=params, allow_redirects=False)  
        if response.status_code == 302:
            location = response.headers.get('Location')
            if location == "/AltoroJ/bank/main.jsp":
                sys.exit(1)
            else:
                sys.exit(0)
    except requests.exceptions.RequestException as e:
        print(f"Error en la conexión: {e}")
Login(paramsattack)

