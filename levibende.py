
import MongodbDAO

# informatie tonen over wat data
db = MongodbDAO.getMongoDB()

collectionsNames = db.list_collection_names()
for collectionName in collectionsNames:
    collection = db.get_collection(collectionName)
    print(f'Collection {collectionName} contains {collection.estimated_document_count()} documents')


# zoeken
products = MongodbDAO.getDocuments("products")
# products is een Cursor
print(f'First document in products = {products.next()}')
eerste_product = products.next()
print(f"De naam van het eerste product is: {eerste_product['name']}, de prijs van het eerste product is: {eerste_product['price']['selling_price']}")

#2a vraag 1
print(f"Het eerste product is {eerste_product['name']} en kost: €{eerste_product['price']['selling_price']/100}")

#2a vraag 2
for product in products:
    if product['name'][0] == 'R':
        print(f"Het eerste product met de R is {product['name']}")
        break
#2a vraag 3
totaleprijs = 0
productcount = 0
for product in products:
    try:
        if product['price']['selling_price'] > 0:
            totaleprijs += product['price']['selling_price']
            productcount += 1
    except KeyError:
        print(f"Price niet aanwezig bij productid:{product['_id']}")
print(f"De gemiddelde prijs van de producten is: €{round((totaleprijs/productcount))/100}. Er staan {productcount} producten met prijs in de database.")

# zoeken met filter
# products = mongodbDAO.getDocuments("products",{'category': 'Wonen & vrije tijd'})
