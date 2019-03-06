import unittest
from ..models import Subscription
from app import db

class SubscriptionTest(unittest.TestCase):
    '''
    Test class to test the behavior of the Subscription class
    '''
    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_subcription = Subscription(name='John', subcription_data='abc@example.com')
    
    def tearDown(self):
        '''
        Method that will clear up after test has run
        '''
        db.session.delete(self.new_subcription)
        db.session.commit()
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_subcription,Email))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_subcription.name,'John')
        self.assertEquals(self.new_subcription.subcription_data,'abc@example.com')


    def test_save_review(self):
        self.new_subcription.save_subcription()
        self.assertTrue(len(Subscription.query.all())>0)
if __name__ ==  '__main__':
    unittest.main()
