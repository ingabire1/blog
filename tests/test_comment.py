from app.models import Pitch,User,Comment
from app import db
import unittest


class CommentModelTest(unittest.TestCase):
   def setUp(self):
        self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com', bio='pooo',profile_pic_path='https://sss.com')
        self.new_blog = Blog(id=4433,content='Blog for movies',category="weeee",user = self.user_James )
        self.new_comment=Comment(id=3344,content="weeee",user=self.user_James,quote=self.new_quote)
   def tearDown(self):
        blog.query.delete()
        User.query.delete()
        Comment.query.delete()

   def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.id,3344)
        self.assertEquals(self.new_comment.content,'weeee')
        
        self.assertEquals(self.new_comment.pitch,self.new_blog)
        
        self.assertEquals(self.new_blog.user,self.user_James)

   def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)  

   def test_get_pitch_by_id(self):

        self.new_comment.save_pitch()
        got_comments = Comment.get_comments(3344)
        self.assertTrue(len(got_comments) == 1)      