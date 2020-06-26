#============================================
# Title:  Exercise 9.3
# Author: Professor Krasso
# Modified by: James Brown
# Date:   6/26/2020
# Description: coding per requirements of exercise 9.3
#===========================================

#import statements
from pymongo import MongoClient
import pprint
import datetime

#connection to local db
client = MongoClient('localhost', 27017)

#specifying the collection
db = client.web335

#update the user email address from assignment 9.2
db.users.update_one(
    {"employee_id": "1234567890"},
    {
        "$set": {
            "email": "jamesbrown2@my365.bellevue.edu"
        }
    }
)

#output the change with find_one
pprint.pprint(db.users.find_one({"employee_id": "1234567890"}))