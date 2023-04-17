from flask import Flask, jsonify
import requests
import response
app = Flask(__name__)https://github.com/finnend/requestget/blob/main/app.py

       
Nombre_1 = {

    {
        "id": 2,
        "Rut": 202824291,
        "Nombres": "Juan Antonio",
        "apellidoPaterno": "De la mancha",
        "apellidoMaterno": "Benavent",
        "fechadenacimiento": "20/01/2000",
        "Sueldo": 1000
    },

    {
        "id": 3,
        "Rut": 192824291,
        "Nombres": "Pedro",
        "apellidoPaterno": "De la mancha",
        "apellidoMaterno": "Benavent",
        "fechadenacimiento": "20/01/2000",
        "Sueldo": 1000
    },

    {
        "id": 4,
        "Rut": 202834291,
        "Nombres": "Pablo",
        "apellidoPaterno": "De la mancha",
        "apellidoMaterno": "Benavent",
        "fechadenacimiento": "20/01/2000",
        "Sueldo": 1000
    },

    {
        "id": 5,
        "Rut": 182824291,
        "Nombres": "Manuel",
        "apellidoPaterno": "De la mancha",
        "apellidoMaterno": "Benavent",
        "fechadenacimiento": "20/01/2000",
        "Sueldo": 1000
    },

    {
        "id": 6,
        "Rut": 192834291,
        "Nombres": "Cristian",
        "apellidoPaterno": "De la mancha",
        "apellidoMaterno": "Benavent",
        "fechadenacimiento": "20/01/2000",
        "Sueldo": 1000 
    },

    {
        "id": 7,
        "Rut": 172824291,
        "Nombres": "John",
        "apellidoPaterno": "De la mancha",
        "apellidoMaterno": "Benavent",
        "fechadenacimiento": "20/01/2000",
        "Sueldo": 1000 
    },
 
    {
        "id": 8,
        "Rut": 192824291,
        "Nombres": "Joaquin",
        "apellidoPaterno": "De la mancha",
        "apellidoMaterno": "Benavent",
        "fechadenacimiento": "20/01/2000",
        "Sueldo": 1000 
    },

    {
        "id": 9,
        "Rut": 192824291,
        "Nombres": "Ignacio",
        "apellidoPaterno": "De la mancha",
        "apellidoMaterno": "Benavent",
        "fechadenacimiento": "20/01/2000",
        "Sueldo": 1000 
    },

    {
        "id": 10,
        "Rut": 122824291,
        "Nombres": "Alejandro",
        "apellidoPaterno": "De la mancha",
        "apellidoMaterno": "Benavent",
        "fechadenacimiento": "20/01/2000",
        "Sueldo": 1000 
    }

]
}


@app.route('/')
def index():
    print(__name__)
    return 'Index' 

@app.route("/json")
def json():
    return jsonify({"Nombre_1": Nombre_1})


@app.route("/cristobal")
def show_nombre():
    nombre = requests.get("https://finnend.com/datos.json").json()
    c = nombre["personas"][0]
    return c
@app.route("/juan")
def show_persona():
    nombre = requests.get("https://finnend.com/datos.json").json()
    c = nombre["personas"][1]
    return c
@app.route("/pedro")
def hide_persona():
    nombre = requests.get("https://finnend.com/datos.json").json()
    c = nombre["personas"][2]
    return c
@app.route("/pablo")
def showed_person():
    nombre = requests.get("https://finnend.com/datos.json").json()
    c = nombre["personas"][3]
    return c
@app.route("/manuel")
def finding_person():
    nombre = requests.get("https://finnend.com/datos.json").json()
    c = nombre["personas"][4]
    return c
@app.route("/cristian")
def trying_person():
    nombre = requests.get("https://finnend.com/datos.json").json()
    c = nombre["personas"][5]
    return c
@app.route("/john")
def drying_person():
    nombre = requests.get("https://finnend.com/datos.json").json()
    c = nombre["personas"][6]
    return c
@app.route("/joaquin")
def oking_person():
    nombre = requests.get("https://finnend.com/datos.json").json()
    c = nombre["personas"][7]
    return c
@app.route("/ignacio")
def king_person():
    nombre = requests.get("https://finnend.com/datos.json").json()
    c = nombre["personas"][8]
    return c
@app.route("/alejandro")
def ing_person():
    nombre = requests.get("https://finnend.com/datos.json").json()
    c = nombre["personas"][9]
    return c

if __name__ == "__main__":
    app.run(debug=True)
