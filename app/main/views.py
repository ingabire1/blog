from flask import render_template,request,redirect,url_for,abort, flash
from . import main
from .forms import ReviewForm,UpdateProfile,BlogForm,CommentForm,SubscriptionForm,UpdatePostForm
from ..models import User,BlogPost,Comment,Subscription
from flask_login import login_required,current_user
from .. import db
from ..request import get_quote
from ..email import mail_message


@main.route('/')
def index():
    
    '''
    View root page function that returns the index page and its data
    '''
    quote = get_quote()
    blog=BlogPost.query.all()
    
    title = 'Home'
    return render_template('index.html', title = title,blog=blog,quote=quote)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)
@main.route('/blog/new', methods=['GET','POST'])
@login_required
def create_blogs():
    form = BlogForm()
    subscriptions=Subscription.query.all()
    if form.validate_on_submit():
        title=form.title.data
        blog_post=form.blog_post.data
        new_blog = BlogPost(title=title,blog_post=blog_post, user=current_user)
        db.session.add(new_blog)
        db.session.commit()
        for subscription in subscriptions:
            mail_message("hey!!there is new post","email/notification",subscription.subscription_data)

        return redirect(url_for('main.index'))

    return render_template('blog.html',form = form)   

@main.route('/edit/blog/<int:id>',methods= ['GET','POST'])
@login_required
def update_post(id):
   blog=BlogPost.query.filter_by(id=id).first()
   if blog is None:
        abort(404)

   form=UpdatePostForm()
   if form.validate_on_submit():
        #  post.title=form.title.data
        #  blog.title=form.title.data
         blog.blog_post=form.blog_post.data

         db.session.add(blog)
         db.session.commit()

         return redirect(url_for('main.index'))
   return render_template('update_post.html',form=form)

@main.route('/comment/new/<int:id>', methods=['GET','POST'])
@login_required
def add_comments(id):
    form = CommentForm()
    if form.validate_on_submit():
        name=form.name.data
        comment=form.comment.data
        new_comment = Comment(comment=comment,name=name,blogposts_id=id, user=current_user)
        
        db.session.add(new_comment)
        db.session.commit()

        return redirect(url_for('main.index'))
    comment=Comment.query.filter_by(blogposts_id=id).all()


    return render_template('comment.html',comment=comment,form =form)   
@main.route('/sub/new/', methods = ['GET','POST'])
def Subscription_view():
    form = SubscriptionForm()
    # print(form.name.data)
    if form.validate_on_submit():
        name = form.name.data
        subscription_data = form.subscription_data.data
        

        new_subscription = Subscription(name=name,subscription_data=subscription_data)
        db.session.add(new_subscription)
        db.session.commit()
        mail_message("Thank you for subscribing","email/subscrib",new_subscription.subscription_data)

        flash('subscription complete now we will receive an email of update')
        return redirect(url_for('main.index'))

    return render_template('subscription.html',user = current_user, form = form)
@main.route('/blog/<int:id>/<int:id_comment>/delete_comment')
@login_required
def delete_comment(id,id_comment):
    comment = Comment.get_single_comment(id,id_comment)

    db.session.delete(comment)
    db.session.commit()

    flash('Comment has been deleted')

    return redirect(url_for('main.add_comments',id=id))


@main.route('/index/<int:id>/delete_blog')
@login_required
def delete_blog(id):
    blog = BlogPost.get_single_blog(id)

    db.session.delete(blog)
    db.session.commit()

    flash('Blog has been deleted') 

    return redirect(url_for('main.index'))