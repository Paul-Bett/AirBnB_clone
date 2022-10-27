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
    
