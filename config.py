import pymongo
import certifi


cont_str = "mongodb+srv://FSDI:1234@cluster0.rwtcumn.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(cont_str, tlsCAFile=certifi.where())
db = client.get_database("camexpert")