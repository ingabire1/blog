import unittest
from app.models import  BlogPost
from app import db


class CommentTest(unittest.TestCase):

    def setUp(self):
        self.new_blog =  BlogPost(title='New Blog',blogpost='This is the content')

    def tearDown(self):
        db.session.delete(self.new_blog)
        db.session.commit()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog, BlogPost))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.title,'New Blog')
        self.assertEquals(self.new_blog.blog_content,'This is the content')
        


    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Blog.query.all())>0)
if __name__ ==  '__main__':
    unittest.main()