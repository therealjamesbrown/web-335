#============================================
# Title:  Exercise 9.2
# Author: Professor Krasso
# Modified by: James Brown
# Date:   6/26/2020
# Description: coding per requirements of exercise 9.2
#===========================================

#import statements
from pymongo import MongoClient
import pprint
import datetime

#connection to local db
client = MongoClient('localhost', 27017)

#specifying the collection
db = client.web335

#create the user
user = {
  "first_name": "Tyler",
  "last_name": "Graham",
  "email": "ty@gmail.com",
  "employee_id":"1234567890",
  "date_created": datetime.datetime.utcnow()
}

#insert user
user_id = db.users.insert_one(user).insterted_id

#print user id
print(user_id)

#find the user and print
pprint.pprint(db.users.find_one({"employee_id": "1234567890"}))

