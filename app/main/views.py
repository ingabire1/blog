from flask import render_template,request,redirect,url_for, abort
from . import main

from .forms import UpdateProfile,CommentForm,AddPitchForm
from .. import db,photos
from ..models import Comment,Pitch,User
from flask_login import login_required, current_user



@main.route('/')
def index():
  title="Home| Blog"
  all_blog = blog.get_blogs()
  
  return render_template('index.html',title=title, blog = all_blogs)

@main.route('/blog/new', methods = ['GET', 'POST'])
@login_requiredfrom . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

class User(UserMixin,db.Model):
    __tablename__='users'

    id = db.Column(db.Integer,primary_key=True)
    username= db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True , index=True)
    bio= db.Column(db.String(255))
    profile_pic_path = db.Column(db.String(255))
    pass_secure=db.Column(db.String(255))
    pitches= db.relationship('Pitch',backref='user', lazy='dynamic')
    comments = db.relationship('Comment',backref='user' ,lazy='dynamic')

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

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class quote(db.Model):
   __tablename__ = 'quotes'

   id = db.Column(db.Integer,primary_key = True)
   user_id= db.Column(db.Integer,db.ForeignKey('users.id'))
   content = db.Column(db.String(255))
   comments = db.relationship('Comment',backref='pitch' ,lazy='dynamic')
   category = db.Column(db.String(255))
#    upvotes = db.Column(db.Integer)
#    downvotes = db.Column(db.Integer)


   def save_quote(self):
        db.session.add(self)
        db.session.commit()

   @classmethod
   def clear_quote(cls):
        quote.all_quotes.clear()

   @classmethod
   def get_quote(cls,id):
        quote = quote.query.filter_by(id=id).all()
        return quote
    
   @classmethod
   def get_quotes(cls):
       quotes = quote.query.filter_by().all()
       return quotes

#    @classmethod
#    def upvotess(cls,id):
#        pitch=Pitch.query.filter_by(id=id).first()
#        pitch.upvotes=0
#        upvotes=pitch.upvotes+1
#        return upvotes

#    @classmethod
#    def downvotess(cls,id):
#        pitch=Pitch.query.filter_by(id=id).first()
#        pitch.downvotes=0
#        downvotes=pitch.downvotes-1
#        return downvotes




class Comment(db.Model):
    __tablename__= 'comments'
    
    id= db.Column(db.Integer,primary_key= True)
    content = db.Column(db.String(255))
    user_id= db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))


    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_comments(cls):
        Comment.all_comments.clear()

    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(pitch_id=id).all()
        return comments

    @classmethod
    def get_commentss(cls,id):
        comments = Comment.query.filter_by(user_id=id).all()
        return comments

def add_pitch():
    form = Add blogForm()
    
    if form.validate_on_submit():
        category = form.category.data

        pitch = form.content.data

        new_blog = blog(content=blog,user=current_user)
        new_blog.save_blog()

        return redirect(url_for('main.index'))



    title = 'Add Blog| one new blog'    
    return render_template('pitches.html', title = title, pitch_form = form,user=current_user)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

# @main.route('/user/<uname>/update',methods = ['GET','POST'])
# @login_required
# def update_profile(uname):
#     user = User.query.filter_by(username = uname).first()
#     if user is None:
#         abort(404)

#     form = UpdateProfile()

#     if form.validate_on_submit():
#         user.bio = form.bio.data

#         db.session.add(user)
#         db.session.commit()

#         return redirect(url_for('.profile',uname=user.username))

#     return render_template('profile/update.html',form =form)

# @main.route('/user/<uname>/update/pic',methods= ['POST'])
# @login_required
# def update_pic(uname):
#     user = User.query.filter_by(username = uname).first()
#     if 'photo' in request.files:
#         filename = photos.save(request.files['photo'])
#         path = f'photos/{filename}'
#         user.profile_pic_path = path
#         db.session.commit()
#     return redirect(url_for('main.profile',uname=uname))

@main.route('/new/comment/<int:id>', methods = ['GET','POST'])
@login_required
def add_comment(id):
  pitch=Pitch.query.filter_by(id=id).first()
  if pitch is None:
    abort(404)

  form=CommentForm()
  if form.validate_on_submit():
     comment=form.comment.data
     new_comment=Comment(content=comment ,blog=blog ,user=current_user)
     db.session.add(new_comment)  
     db.session.commit() 

     return redirect(url_for('main.index'))
  return render_template('comment.html', comment_form=form)

# @main.route('/pitch/<int:id>')
# def single_pitch(id):
#     pitch=Pitch.query.filter_by(id=id).first()
#     comments=Comment.get_comments(id=id)
#     return render_template('pitch.html',pitch=pitch,comments=comments)

# @main.route('/upvotes/<int:id>')
# def upvoting(id):
#     pitch1=Pitch.query.filter_by(id=id).first()
#     pitch1.upvotes=Pitch.upvote(pitch1.id)
#     return redirect(url_for('main.single_pitch',id=pitch1.id))

@main.route('/categories')
def categories():
    title="Categories"

    return render_template('categories.html')

@main.route('/category/quotes')
def recent-post():
    title="|quotes"
    blogs=blog.query.filter_by(category='quotes').all()
    return render_template('quotes.html',blog=blog)

@main.route('/category/update')
def update():
    title="blog|update"
    blogs=blogs.query.filter_by(category='update-blogs').all()
    return render_template('update.html',blog=blog)
        
@main.route('/category/delete')
def delete():
    title="Blog|delete"
    blogs=blog.query.filter_by(category='delete-blogs').all()
    return render_template('delete.html',blog=blog)
    

    

