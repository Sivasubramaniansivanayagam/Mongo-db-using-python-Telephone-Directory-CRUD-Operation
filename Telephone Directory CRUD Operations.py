#   Import necessary modules.

import pymongo as pm

# Create a database using attribute style on a MongoClient instance. Declare a variable db
# and assign the new database as an attribute of the client.

client = pm.MongoClient(
    "mongodb+srv://user1:Mongodb123@cluster0.cxmnv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client.Telephone_directory11

mydb = db.Tamilnadu_tele_dir13

# For CRUD operation, create a directory which has fields like Name, Phone number, Place etc.,

details = [{"_id": 1, "Name": "Rajesh", "phone number": 272123, "Address": {"Place": "Adambakkam", "pincode": 600025}},
           {"_id": 2, "Name": "Suresh", "phone number": 272124, "Address": {"Place": "Velachery", "pincode": 600063}},
           {"_id": 3, "Name": "Rocky", "phone number": 272125, "Address": {"Place": "Guindy", "pincode": 600045}},
           {"_id": 4, "Name": "Ravi", "phone number": 272126, "Address": {"Place": "Ashok Nagar", "pincode": 600078}},
           {"_id": 5, "Name": "Harish", "phone number": 272127,
            "Address": {"Place": "Virugambakkam", "pincode": 600089}},
           {"_id": 6, "Name": "Remo", "phone number": 272128, "Address": {"Place": "Adayar", "pincode": 600093}},
           {"_id": 7, "Name": "John", "phone number": 272129, "Address": {"Place": "Annanagar", "pincode": 600092}},
           {"_id": 8, "Name": "Sofi", "phone number": 272130, "Address": {"Place": "T-nagar", "pincode": 600096}},
           {"_id": 9, "Name": "Priya", "phone number": 272131, "Address": {"Place": "Numgambakkam", "pincode": 600095}},
           {"_id": 10, "Name": "Sony", "phone number": 272132, "Address": {"Place": "Tenampet", "pincode": 600097}}]

# Insert the record into the collection

in_data = mydb.insert_many(details)
print(in_data.inserted_ids)

# Make a query to find records you just created.

for i in mydb.find({"_id": 5}):
    print(i)

and_query = mydb.find({"$and": [{"_id": 8}, {"Name": "Sofi"}]})
for i in and_query:
    print(i)

for i in mydb.find({"$or": [{"_id": 3}, {"Name": "Sony"}]}):
    print(i)

# Modify the records, use the update_one() method. The update_one() method requires two arguments, query and update.

r = mydb.update_one({"Name": "Remo"}, {"$set": {"Name": "Tharani"}})
print(r.matched_count)
print(r.modified_count)

for i in mydb.find({"Name": "Tharani"}):
    print(i)
# successfully updated

# Delete the record, use delete_one() method. delete_one() requires a query parameter
# which specifies the document to delete.

a = mydb.delete_one({"Name": "Harish"})
print(a.deleted_count)
