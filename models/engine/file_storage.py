#!/usr/bin/env python3
import json
import models

''' Class FileStorage
'''


class FileStorage():
    ''' Serialize and deserialize instance to and from JSON file
    '''

    __file_path = my_file.json
    __objects = dict()

    def all(self):
        ''' Returns the dictionary __objects
        '''
        return __objects

    def new(self,obj):
        '''  sets in __objects the obj with key <obj class name>.id
        '''
        self.__objects[(obj.__class__.__name__) + "." + (obj.id)] = obj

    def save(self):
        ''' serializes __objects to the JSON file (path: __file_path)
        '''
        with open(__file_path, mode="w", encoding="UTF8") as jsonfile:
            json.dump(__objects, jsonfile) 

    def reload(self):
        ''' Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists
            otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
        '''
        with open(__file_path, encoding-"UTF8") as jsonfile:
            self.__objects = json.load(jsonfile)

