from flask import render_template,request,redirect,url_for, abort
from . import main

from .forms import UpdateProfile,CommentForm,AddPitchForm
from .. import db,photos
from ..models import Comment,Pitch,User
from flask_login import login_required, current_user
# import markdown2 
from flask_fontawesome import FontAwesome

@main.route('/')
def index():
  title="Home| Blog"
  all_blog = blog.get_blogs()
  
  return render_template('index.html',title=title, blog = all_blogs)

@main.route('/blog/new', methods = ['GET', 'POST'])
@login_required
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
    

    

