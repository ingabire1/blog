
import os
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import db, login_manager

class Quote:
   '''
   Quote class to define quote objects
   '''

   def __init__(self,id,author,content):
     self.id=id
     self.author=author
     self.content=content

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    # comment_id = db.Column(db.Integer,db.ForeignKey('comments.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    blogposts = db.relationship('BlogPost',backref = 'user',lazy="dynamic")
    comments = db.relationship('Comment',backref = 'user',lazy="dynamic")
    pass_secure = db.Column(db.String(255))
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class BlogPost(db.Model):
    __tablename__= 'blogposts' 
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    blog_post = db.Column(db.String(255))
    # category = db.Column(db.String(255))
    users_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comments = db.relationship('Comment',backref = 'pitche',lazy="dynamic")
  
    def save_all_blog(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_blog(cls, id):
        blogposts = BlogPost.order_by('-id').all()
        return blogposts
    @classmethod
    def get_single_blog(cls,id):
        blog_post = BlogPost.query.filter_by(id=id).first()
        return blog_post

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    comment = db.Column(db.String(255))
    users_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    blogposts_id = db.Column(db.Integer,db.ForeignKey('blogposts.id'))
    def save_comment(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_blog_comments(cls,id):
        comments = Comment.query.filter_by(blog_id=id).order_by('-id').all()
        return comments
    
    @classmethod
    def get_single_comment(cls,id_blog,id):
        comment = Comment.query.filter_by(blogposts_id=id_blog,id=id).first()
        return comment

# @classmethod
# def get_pitches(cls):
#     pitches = Pitche.query.filter_by().all()
#     return pitches
class Subscription(db.Model):
    __tablename__='subscriptions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    subscription_data = db.Column(db.String(255))

    # def save_subscription(self):
    #     db.session.add(self)
    #     db.session.commit()
    
    @classmethod
    def send_single_subscription(cls,id):
        Subscription = Subscription.query.filter_by(id=id).first()
        return Subscription