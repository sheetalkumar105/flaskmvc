#!/usr/bin/python
# -*- coding: utf-8 -*-

from ..app import mongo
from flask import request,json
import hashlib
import pprint
from flask_pymongo import ObjectId
from datetime import datetime
from app.helpers.Utility import toDictionaryArray

class AuthModel():
    def __init__(self):
        pass

    def getUser(_id):
        users = mongo.db.users.find({'_id': _id})
        x = []
        for user in users:
            x.append(user)
        return user

    def getAllUser(_id):
        users = mongo.db.users.find()
        return toDictionaryArray(users)

    def registerUser(self,_first_name, _last_name, _email, _password):
        d = datetime.now()
        h = hashlib.md5(_password)
        insertdata = {'first_name': _first_name, 'last_name': _last_name, 'email': _email, 'password': h.hexdigest(), 'status': "0", 'created_at': d, 'updated_at': d}
        u = mongo.db.users.insert(insertdata)
        return {'status':'1','message':'Registration Successfull','_id': str(ObjectId(u))}


authmodel=AuthModel()
