import pymongo
dbobj = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
# Create database
dbase = dbobj['Book']
print('Book Database Created')
# Add data and check
data = dbase['mybooks']
# List all dbs in mongodb
print('All Databases:'+str(dbobj.list_database_names()))
# Check if database already exists
dblist = dbobj.list_database_names()
if 'Book' in dblist:
    print('Book Database exists')
else:
    print('Book Database Not exist')


# Insert 1 record
dict1 = {'isbn_no': '12345', 'title': '12 Pivet Drive',
         'author': 'ABC', 'No_of_pages': '250', 'price': '500'}
ins1 = data.insert_one(dict1)
print('\nInserted Record: '+str(ins1.inserted_id))

l1 = [{'isbn_no': '20145', 'title': '12 Drive', 'author': 'PQR', 'No_of_pages': '350', 'price': '600'},
      {'isbn_no': '02458', 'title': 'Drive', 'author': 'XYZ',
          'No_of_pages': '200', 'price': '450'},
      {'isbn_no': '89632', 'title': 'Blockchain',
       'author': 'MNO', 'No_of_pages': '300', 'price': '400'},
      {'isbn_no': '98620', 'title': 'Big Data', 'author': 'PQR', 'No_of_pages': '350', 'price': '500'}]

c = data.insert_many(l1)
print('Records inserted: '+str(c.inserted_ids))
# Print all docs in collection using find method
print('Records:\n\n')
for data1 in data.find():
    print(data1)
# Find document with address
myq = {'author': 'XYZ'}
mydoc1 = data.find(myq)
print('\n\nRecord with Matched Address: ')
for i in mydoc1:
    print(i)
# Delete one
del1 = {'author': 'PQR'}
d1 = data.delete_one(del1)

var = data.find()
print('\n\nRecords after Deletion: ')
for i in var:
    print(i)

print('Records deleted: '+str(d1.deleted_count))

# Delete many
del1 = {'No_of_pages': '350'}
d1 = data.delete_many(del1)

var = data.find()
print('\n\nRecords after Deletion: ')
for i in var:
    print(i)
7
# Update one record
up1 = {'isbn_no': '12345'}
set1 = {'$set': {'price': '600'}}
u1 = data.update_one(up1, set1)
var = data.find()
for i in var:
    print(i)
print('\n\nUpdated record count: '+str(u1.modified_count))

# Update many
up2 = {'isbn_no': '12345'}
set2 = {'$set': {'price': '550'}}
u2 = data.update_many(up2, set2)
var = data.find()
for i in var:
    print(i)
print('\n\nUpdated record count: '+str(u2.modified_count))

# limit
var = data.find().limit(3)
print('\n\nLimited Records: ')
for i in var:
    print(i)
