#!/usr/bin/env python3
import json
import models
import os

'''Module: file_storage
    Class: FileStorage
'''


class FileStorage():
    ''' Serialize and deserialize instance to and from JSON file
        Private Class Attributes:
            __file_path(str): path to JSON file
            __objects(dict): storage of object
        Public instance methods:
            all(self): returns __objects
            new(self, obj):
            save(self):
            reload(self):
    '''

    __file_path = "my_file.json"
    __objects = dict()

    def all(self):
        ''' Returns the dictionary __objects
        '''
        return FileStorage.__objects

    def new(self,obj):
        '''  sets in __objects the obj with key <obj class name>.id
            Args:
                obj(dict): the object
        '''
        key = (obj.__class__.__name__) + "." + (obj.id)
        FileStorage.__objects[key] = str(obj)

    def save(self):
        ''' serializes __objects to the JSON file (path: __file_path)
        '''
        with open(FileStorage.__file_path, mode="w", encoding="UTF8") as jsonfile:
            json.dump(FileStorage.__objects, jsonfile) 

    def reload(self):
        ''' Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists
            otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
        '''
        if os.path.isfile(FileStorage.__file_path) and os.access(FileStorage.__file_path, os.R_OK):
            with open(FileStorage.__file_path, encoding="UTF8") as jsonfile:
               FileStorage.__objects = json.load(jsonfile)
