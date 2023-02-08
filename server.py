from flask import Flask
from data import me

import json

app = Flask(__name__) #similar to new Task in JS


@app.get("/")
def home():
    return "Hello World!"

@app.get("/about")
def about():
    return "Brayan Ornelas"

@app.get("/contact/me")
def contact_me():
    return "ornelas.brayan@uabc.edu.mx"



#################################################################
######################## API -> JSON ############################
#################################################################


@app.get("/api/developer")
def developer():
    return json.dumps(me)

@app.get("/api/developer/adress")
def dev_adress():
    address = me["address"]
    # return address["street"] + " #" + str(address["number"]) + ", " + address["city"] + ", " + address["zipcode"]
    # f string
    return f'{address["street"]} #{address["number"]}, {address["city"]}, {address["zipcode"]}'




app.run(debug=True)

