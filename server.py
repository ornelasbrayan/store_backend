from flask import Flask, abort, request
from data import me, mock_catalog
from config import db
from bson import ObjectId
from flask_cors import CORS


import json


app = Flask(__name__) #similar to new Task in JS
CORS(app) #WARNING: disable CORS policy


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

def  fix_id(obj):
    obj["_id"] = str(obj["_id"])

@app.get("/api/catalog")
def get_catalog():
    cursor = db.products.find({})
    results = []
    for prod in cursor:
        fix_id(prod)
        results.append(prod)

    return json.dumps(results)

@app.post("/api/catalog")
def save_product():
    data = request.get_json()
    db.products.insert_one(data)
    fix_id(data)
    return json.dumps(data)

@app.get("/api/catalog/count")
def count_products():
    total = db.products.count_documents({})
    return json.dumps(total)

@app.get("/api/category/<cat>")
def prods_by_category(cat):
    cursor = db.products.find({"category" : cat}) #filter on  data base
    results = []
    for prod in cursor:
        fix_id(prod)
        results.append(prod)

    return json.dumps(results)

@app.get("/api/product/<id>")
def prod_by_id(id):
    _id = ObjectId(id)
    prod = db.products.find_one({"_id" : _id})
    if prod is None:
        return abort(404, "Invalid id")

    fix_id(prod)
    return json.dumps(prod)

@app.get("/api/product/search/<title>")
def search_product(title):
    cursor = db.products.find({"title" : {"$regex": title, "$options" : "i"}})
    results = []
    for prod in cursor:
        fix_id(prod)
        results.append(prod)
        
    return json.dumps(results)

@app.get("/api/categories")
def get_categories():
    cursor = db.products.distinct("category")
    return json.dumps(list(cursor))

@app.get("/api/total")
def get_total():
    total = 0
    for prod in mock_catalog:
        total += prod["price"]
    
    return json.dumps(total)

@app.get("/api/cheaper/<price>")
def get_cheaper(price):
    result = []
    for prod in mock_catalog:
        if prod["price"] < int(price):
            result.append(prod) 
    
    return json.dumps(result)

@app.get("/api/cheapest")
def get_cheapest():
    result = mock_catalog[0]
    for prod in mock_catalog:
        if prod["price"] < result["price"]:
            result = prod
    
    return json.dumps(result)


            



    



app.run(debug=True)



