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
first_product = products.next()
print( f" Naam 1st prod {first_product['name']} , 1st prod prijs:  {first_product['price']['selling_price']}")

product_view = products.values()
value_iterator = iter(product_view)
first_value = 



# zoeken met filter
products = MongodbDAO.getDocuments("products",{'category': 'Wonen & vrije tijd'})