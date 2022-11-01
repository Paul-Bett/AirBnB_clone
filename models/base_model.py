#!/usr/bin/env python3
import uuid
from datetime import datetime
import models


'''
Module: base_model
'''


class BaseModel():
    '''
    Base Model Class
    '''

    def __init__(self, *args, **kwargs):
        ''' Initialization of BaseModel
        public instance attributes:
        id(str): uniqued identifier
        created_at(DT): instance creation date time
        updated_at(DT): instance change date time
        '''
        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    self.__dict__[key] = datetime.isoformat(datetime.today())
                elif key == 'id':
                    self.id = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.isoformat(datetime.today())
            self.updated_at = datetime.isoformat(datetime.today())
            models.storage.new(self)

    def __str__(self):
        ''' Print informal representation of an instance
        Print:
            [<class_name>], (self.id), <self.i__dict__>
        '''

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        ''' update attribute updated at with current DT
        '''
        self.updated_at = datetime.isoformat(datetime.today())
        # save storage
        models.storage.save()

    def to_dict(self):
        """A dictionary containing all keys/values of __dict__
        of the instance
        Return:
            dictionary (dict): Dictionary object that contains __dict__
        """
        the_dict = self.__dict__.copy()
        the_dict["created_at"] = self.created_at
        the_dict["updated_at"] = self.updated_at
        the_dict["__class__"] = self.__class__.__name__
        return the_dict


if __name__ == '__main__':
    new = BaseModel()
    print(new.to_dict())
