#!/usr/bin/env python3
import uuid
from datetime import datetime 
'''
BaseModel Module for all common attributes
'''


class BaseModel():
    '''
    Base Model Class
    '''

    def __init__(self):
	''' Initialization of BaseModel
	    public instance attributes: 
		id(str): uniqued identifier
		created_at(DT): instance creation date time
		updated_at(DT): instance change date time
	'''
        id = str(uuid.uuid4())
        created_at = datetime.isoformat(datetime.today())
	updated_at = datetime.isoformat(datetime.today())

    def __str__(self):
 	''' Print informal representation of an instance
	'''
	
	

    def save(self):
	''' update attribute updated at with current DT
	'''
	self.updated_at = datetime.isoformat(datetime.today())


