from flask import Flask, abort
from data import me, mock_catalog


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



################################################################
######################## API -> JSON ###########################
################################################################


@app.get("/api/developer")
def developer():
    return json.dumps(me)

@app.get("/api/developer/adress")
def dev_adress():
    address = me["address"]
    # return address["street"] + " #" + str(address["number"]) + ", " + address["city"] + ", " + address["zipcode"]
    # f string
    return f'{address["street"]} #{address["number"]}, {address["city"]}, {address["zipcode"]}'


@app.get("/api/catalog")
def get_catalog():
    return json.dumps(mock_catalog)

@app.get("/api/catalog/count")
def count_products():
    return json.dumps(len(mock_catalog))

@app.get("/api/category/<cat>")
def prods_by_category(cat):
    results = []
    for prod in mock_catalog:
        if prod["category"] == cat:
            results.append(prod)

    return json.dumps(results)

@app.get("/api/product/<id>")
def prod_by_id(id):
    for prod in mock_catalog:
        if prod["_id"] == id:
            return json.dumps(prod)
    
    return abort(404, "Invalid id")

@app.get("/api/product/search/<title>")
def search_product(title):
    results = []
    for prod in mock_catalog:
        if title.lower() in prod["title"].lower():
            results.append(prod)
    
    return json.dumps(results)

@app.get("/api/categories")
def get_categories():
    results = []
    for prod in mock_catalog:
        cat = prod["category"]
        

    return category
            



    



app.run(debug=True)



