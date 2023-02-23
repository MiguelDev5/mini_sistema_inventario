import json

# SETTERS: Actualiza el archivo json con el nuevo objeto json
# GETTERS: Retorna el objeto json alojado en el archivo json

def setProducts(products_json): 
    with open("./data/products.json", "w") as write_file:
        json.dump(products_json, write_file)

def getProducts(): 
    with open("./data/products.json", "r") as read_file:
        products_json = json.load(read_file)
        return products_json

def setPrices(products_json):
    with open("./data/prices.json", "w") as write_file:
        json.dump(products_json, write_file)

def getPrices():
    with open("./data/prices.json", "r") as read_file:
        prices_json = json.load(read_file)
        return prices_json

def setStock(products_json):
    with open("./data/stock.json", "w") as write_file:
        json.dump(products_json, write_file)

def getStock():
    with open("./data/stock.json", "r") as read_file:
        stock_json = json.load(read_file)
        return stock_json