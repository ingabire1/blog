from app.models import Pitch,User,Comment
from app import db
import unittest


class CommentModelTest(unittest.TestCase):
   def setUp(self):
        self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com', bio='herooo',profile_pic_path='https://sss.com')
        self.new_pitch = Pitch(id=1234,content='Pitch for movies',category="hhh",upvotes=12,downvotes=34,user = self.user_James )
        self.new_comment=Comment(id=1233,content="hhhh",user=self.user_James,pitch=self.new_pitch)
   def tearDown(self):
        Pitch.query.delete()
        User.query.delete()
        Comment.query.delete()

   def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.id,1233)
        self.assertEquals(self.new_comment.content,'hhhh')
        
        self.assertEquals(self.new_comment.pitch,self.new_pitch)
        
        self.assertEquals(self.new_pitch.user,self.user_James)

   def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)  

   def test_get_pitch_by_id(self):

        self.new_comment.save_pitch()
        got_comments = Comment.get_comments(1234)
        self.assertTrue(len(got_comments) == 1)      