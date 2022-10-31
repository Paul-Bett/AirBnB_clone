import unittest
from base_model import BaseModel
import sys

''' base_model module test cases
'''
    

class base_model_TestCase(unittest.TestCase):
    ''' Test for base model class
    '''
    def setUp(self):
        ''' Initialize testing framework 
            This will automatically call for all test we run
        '''
        self.my_instance = BaseModel()

    def tearDown(self):
        ''' Tidies up agter the test method has been run
            Will run wether test method succeeds or not
        '''
        del self.my_instance 

    def test_id_set(self):
        ''' Test if auto-generation of ID is successful
        '''
        self.assertTrue(self.my_instance.id,"ID not generated")

    def test_create_time_set(self):
        ''' Test if create_time was generated
        '''
        self.assertTrue(self.my_instance.id, "Create_Time not generated")

    def test_id_type(self):
        '''
            Checks that the type of the id is string.
        '''
        self.assertEqual("<class 'str'>", str(type(self.my_instance.id)))
   
    def test_save(self):
        '''
            Checks that after updating the instance; the dates differ in the
            updated_at attribute.
        '''
        old_update = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(self.my_model.updated_at, old_update)

    def test_type_created_at(self):
        '''
            Test that the new_model's updated_at
            data type is datetime.
        '''
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(my_model_dict)
        self.assertTrue(isinstance(new_model.created_at, datetime.datetime))
 
    def test_type_updated_at(self):
        '''
            Test that the new_model's created_at
            data type is datetime.
        '''
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(my_model_dict)
        self.assertTrue(isinstance(new_model.updated_at, datetime.datetime))

