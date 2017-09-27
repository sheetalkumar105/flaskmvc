#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint,request,json
from flask_pymongo import ObjectId
from ..app import mongo
from flask import render_template

back = Blueprint("back", __name__)

@back.route('/admin/', methods=['GET'])
def index():
    user = {'nickname': 'Sheetal'}
    return render_template('admin.html',title='Login',user=user)
