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



#2a Q1
products.rewind() # Cursor terug naar oorspronkelijke plaats
print( f" Naam 1st prod {first_product['name']} , 1st prod prijs:  {first_product['price']['selling_price']}")

#2a Q2\
products.rewind() # Cursor terug naar oorspronkelijke plaats
for product in products:
    try:
        if product['name'][0] =='r':
            print(f" naam 1st prod dat begint met r :  {product['name']} ")
            break
    except:
        continue

#2a Q2
products.rewind() # Cursor terug naar oorspronkelijke plaats
totprice= 0
count =0
for product in products:
    try:
        if product['price']['selling_price']>0 and product['price']['selling_price'] == int:
            totprice += product['price']['selling_price']
            count +=1
    except KeyError:
        print('Er ')

print(f'De AVG price is {totprice / count} euro cent, en er zijn  {count} producten ')

# zoeken met filter
products = MongodbDAO.getDocuments("products",{'category': 'Wonen & vrije tijd'})