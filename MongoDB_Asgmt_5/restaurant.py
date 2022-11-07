# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 10:20:24 2022

@author: ustpython03
"""

from pymongo import MongoClient
import json

#Q1 Create database – restaurant, create collection – rescollection. 
#   Insert the documents into collections.
if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017")
    print(client)
    #first create a database
    db = client['restaurant']
    #collection
    collection = db['rescollection']
    #loading or opening json file
    with open ('E:/PyMongo_Dataset/restaurants-dataset.json', "r", encoding="utf-8") as file:
        record = file.read()
        record = record.replace('\n', '')
        record = record.replace('}{', '},{')
        record = "[" + record + "]"
        file_data = json.loads(record)
        
    if isinstance(file_data, list):
        collection.insert_many(file_data)
    else:
        collection.insert_one(file_data)
        
    
    
    
    #Q2) Display all the documents in the collection restaurants.
    
    #MongoDB Query
    db.rescollection.find().pretty()
    
    #PyMongoCode
    alldocs2 = collection.find({})
    for i in alldocs2:
        print(i)
    
    
    
    #Q3) Display the fields restaurant_id, name, borough, and zip code,
    #    but exclude the field _id for all the documents in the collection restaurant.
    
    #MongoDB Query
    db.rescollection.find({},{restaurant_id : 1,name : 1, borough : 1, 'address.zipcode' : 1,_id : 0})
    
    #PyMongo Code
    alldocs3 = collection.find({},{'restaurant_id' : 1,'name' : 1, 'borough' : 1, 'address.zipcode' : 1,'_id' : 0})
    
    for i in alldocs3:
        print(i)
    
    
    
    #Q4) Find the restaurants who achieved a score more than 90.
    
    #MongoDB Query
    db.rescollection.find({'grades.score' : {$gt : 90}},{name : 1})
    
    #PyMongo Code
    alldocs4 = collection.find({"grades.score":{'$gt':90}},{'_id':0,'name':1,'restaurant_id':1,'borough':1,'cuisine':1,'grades.score':1})
    
    for i in alldocs4:
        print(i)
    
    
    
    
    #Q5) Show the restaurants that achieved a score, more than 80 but less than 100.
    
    #MongoDB Query
    db.rescollection.find({'grades.score' : {$gt : 80,$lt : 100}},{name : 1})
    
    #PyMongo Code
    alldocs5 = collection.find({'$and':[{"grades.score":{'$gt':80}},{"grades.score":{'$lt':100}}]},
                              {'_id':0,'name':1,'restaurant_id':1,'borough':1,'cuisine':1,'grades.score':1})
    
    for i in alldocs5:
        print(i)
    
    
    
    
    #Q6) Write Query to show the restaurants that do not prepare any cuisine of american & their grade score > 70.
    
    #MongoDB Query
    db.rescollection.find({$and:[{"cuisine" : {$ne :"American "}},{"grades.score" : {$gt : 70}}]})
    
    #PyMongo Code
    alldocs6 = collection.find({'$and':[{"grades.score":{'$gt':70}},{"cuisine":{'$ne':'American '}}]},
                                  {'_id':0,'name':1,'restaurant_id':1,'borough':1,'cuisine':1,'grades.score':1})
   
    for i in alldocs6:
        print(i)
    
    
    
    
    
    #Q7) Write a MongoDB query to arrange the name of the cuisine in an ascending order 
    #    and for that same borough arranged in descending order.
    
    
    #MongoDB Query
    db.rescollection.find().sort({cuisine:1,borough:-1})
    
    #PyMongo Code
    alldocs7 = collection.find({},{'_id':0,'name':1,'restaurant_id':1,'borough':1,'cuisine':1}).sort([('cuisine',1),('borough',-1)])
    
    for i in alldocs7:
        print(i)
    
    
    
    
    #Q8) Write a MongoDB query to arrange the name of the cuisine in descending order.
    
    #MongoDB Query
    db.rescollection.find().sort({cuisine:-1})
    
    #PyMongo Code
    alldocs8 = collection.find({},{'_id':0,'name':1,'restaurant_id':1,'cuisine':1}).sort('cuisine',-1)
    
    for i in alldocs8:
        print(i)
    
    
    
    
    #Q9) Show the restaurant Id, name, borough and cuisines for those restaurants
    #    which prepared dish except 'American' and 'Chinese' or restaurant's name begins with letter 'Bil'.
    
    #MongoDB Query
    db.rescollection.find({$or:[{name: /^Bil/},{"$and": [{"cuisine" : {$ne :"American "}}, 
        {"cuisine" : {$ne :"Chinese"}}]}]},{"restaurant_id" : 1,"name":1,"borough":1,"cuisine" :1})
    
    #PyMongo Code
    alldocs9 = collection.find({'$or':[{"cuisine":{'$nin':['American ','Chinese']}},{"name":{'$regex':'^Bil'}}]},
                                  {'_id':0,'name':1,'restaurant_id':1,'borough':1,'cuisine':1}).sort('name',1)   
                                                                                                                                   
    for i in alldocs9:
        print(i)
    
    
    
    #Q10) Show the restaurant Id, name, borough and cuisines and score for restaurant's name begins with letter 'Bil'.
    
    #MongoDB Query
    db.rescollection.find({"name" : { $regex : /^Bil.*/}}, {restaurant_id : 1, name : 1,borough: 1,'grades.score' :1, cuisine : 1})
    
    #PyMongo Code
    alldocs10 = collection.find({"name":{'$regex':'^Bil'}},{'_id':0,'name':1,'restaurant_id':1,'borough':1,'cuisine':1,'grades.score':1})
                                        
    for i in alldocs10:
        print(i)
    
    
    
    #Q11) Show the restaurant Id, name, borough and cuisines and score for restaurant serving “Indian” as cuisines. 
    
    #MongoDB Query
    db.rescollection.find({cuisine:'Indian'},{restaurant_id:1,name:1,borough:1,cuisine:1,_id:0,'grades.score':1})
    
    #PyMongo Code
    alldocs11 = collection.find({"cuisine":'Indian'},
                                  {'_id':0,'name':1,'restaurant_id':1,'borough':1,'cuisine':1,'grades.score':1})                                                                                                                                     
    for i in alldocs11:
        print(i)
    
    
    
    
    #Q12) Write a MongoDB query to find the restaurant Id, name, borough, cuisines, and score 
    #     for those restaurants which contain 'bi' as last three letters for its name.
    
    #MongoDB Query
    db.rescollection.find({"name" : { $regex : /.*bi$/}}, {restaurant_id : 1, name : 1,borough: 1,'grades.score' :1, cuisine : 1})
    
    #PyMongo Code
    alldocs12 = collection.find({"name":{'$regex':'bi$'}},
                                  {'_id':0,'name':1,'restaurant_id':1,'borough':1,'cuisine':1,'grades.score':1})
    for i in alldocs12:
        print(i)
    
    
    
    #Q13) Write a MongoDB query to find the restaurant Id, name, borough, cuisines, and score 
    #     for those restaurants which contain 'il' as last three letters for its name.
    
    #MongoDB Query
    db.rescollection.find({"name" : { $regex : /.*il$/}}, {restaurant_id : 1, name : 1,borough: 1,'grades.score' :1, cuisine : 1})
    
    #PyMongo Code
    alldocs13 = collection.find({"name":{'$regex':'il$'}},
                                  {'_id':0,'name':1,'restaurant_id':1,'borough':1,'cuisine':1,'grades.score':1})
    for i in alldocs13:
        print(i)
    
    
    
    #Q14 Write a query to show all the restaurant Id, name, borough, cuisines, and score for those restaurants which contain 'il' anywhere in its name.
    
    #MongoDB Query
    db.rescollection.find({"name":{'$regex':'.*il.*'}},{'_id':0,'name':1,'restaurant_id':1,'borough':1,'cuisine':1,'grades.score':1})
    
    #PyMongo Code
    alldocs14 = collection.find({"name":{'$regex':'.*il.*'}},
                                  {'_id':0,'name':1,'restaurant_id':1,'borough':1,'cuisine':1,'grades.score':1})
    for i in alldocs14:
        print(i)
    
    
    
    #Q15) Write a MongoDB query which will select the restaurant Id, name and grades 
    #     for those restaurants which returns 0 as a remainder after dividing the score by 7.
    
    #MongoDB
    db.rescollection.find({"grades.score":{$mod : [7,0]}},{"restaurant_id" : 1,"name":1,"grades":1})
    
    #PyMongo
    alldocs15 = collection.find({"grades.score" :{'$mod' : [7,0]}},{"_id":0,"restaurant_id" : 1,"name":1,"grades":1})
                                                                                                                              
    for i in alldocs15:
        print(i)
        
        
    
    #Q16) Show document/record counts that has street and not street in addresses.
    
    #MongoDB Query
    db.rescollection.find({"address.street":{ $exists : true }})
    
    #PyMongo Code
    is_street_present = collection.count_documents({'address.street' :{'$exists' : 1}})
    print("Records that contain street in address:",is_street_present)
    is_street_not_present=collection.count_documents({'address.street' :{'$exists' : 0}})
    print("Records that dont contain street in address:",is_street_not_present)
    
    
    
    #Q17) Write a MongoDB query to find the restaurants which do not prepare any cuisine of 'American' 
    #     and achieved a score more than 70 and located in the longitude less than -65.754168 
    
    #MongoDB Query
    db.rescollection.find({'$and':[{"cuisine":{'$ne':'American '}},{"grades.score":{'$gt':70}},{"address.coord" : {'$lt' : -65.754168}}]},
                                  {'_id':0,'name':1,'restaurant_id':1,'borough':1,'cuisine':1,'grades.score':1})
    
    #PyMongo Code
    alldocs17 = collection.find({'$and':[{"cuisine":{'$ne':'American '}},{"grades.score":{'$gt':70}},{"address.coord" : {'$lt' : -65.754168}}]},
                                  {'_id':0,'name':1,'restaurant_id':1,'borough':1,'cuisine':1,'grades.score':1})
    for i in alldocs17:
        print(i)
       

    
    
    
    
