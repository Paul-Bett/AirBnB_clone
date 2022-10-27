import unittest
from base_model import BaseModel
import sys

''' base_model module test cases
'''
    

class base_module_TestCase(unittest.TestCase):
    def setUp(self):
        ''' Initialize testing framework 
            This will automatically call for all test we run
        '''
        self.my_model = BaseModel()

    def tearDown(self):
        ''' Tidies up agter the test method has been run
            Will run wether test method succeeds or not
        '''
        del self.my_model 

    def test_id_set(self):
        ''' Test if auto-generation of ID is successful
        '''
        self.assertTrue(self.my_model.id,"ID not generated")

    def test_create_time(self):
        ''' Test if create_time was generated
        '''
        self.assertTrue(self.my_model.id, "Create_Time not generated")

