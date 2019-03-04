# from app.models import quotes,User
# from app import db
# import unittest


# class PitchModelTest(unittest.TestCase):
#    def setUp(self):
#         self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com', bio='herooo',profile_pic_path='https://sss.com')
#         self.new_quote = Quote(id=1234,content='quote for movies',category="hhh",user = self.user_James )

#    def tearDown(self):
#         User.query.delete()
#         Quote.query.delete()


#    def test_check_instance_variables(self):
#         self.assertEquals(self.new_quote.id,1234)
#         self.assertEquals(self.new_quote.content,'quote for movies')
#         self.assertEquals(self.new_quote.category,"hhh")
#      #    self.assertEquals(self.new_pitch.upvotes,12)
#      #    self.assertEquals(self.new_pitch.downvotes,34)
#         self.assertEquals(self.new_quote.user,self.user_James)

#    def test_save_quote(self):
#         self.new_pitch.save_quote()
#         self.assertTrue(len(quote.query.all())>0)  

#    def test_get_quote_by_id(self):

#         self.new_quote.save_quote()
#         got_quote = qoute.get_quote(1234)
#         self.assertTrue(len(got_quotes) == 1)      
