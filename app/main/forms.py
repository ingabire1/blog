
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class ReviewForm(FlaskForm):

    title = StringField('Review title',validators=[Required()])
    review = TextAreaField('Movie review', validators=[Required()])
    submit = SubmitField('Submit')
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
# class LoginForm(FlaskForm):
#     email = StringField('Your Email Address',validators=[Required(),Email()])
#     password = PasswordField('Password',validators =[Required()])
#     remember = BooleanField('Remember me')
#     submit = SubmitField('Sign In')
class BlogForm(FlaskForm):
    
    # my_category = StringField('Category', validators=[Required()])
    title = StringField('Title', validators=[Required()])
    blog_post = TextAreaField('Type Blog here', validators=[Required()])
    post = SubmitField('Post Blog')

class CommentForm(FlaskForm):
    name = StringField('Name',validators=[Required()])
    # email = StringField('Email', validators=[Required()],render_kw={"placeholder": "Email"})
    comment = TextAreaField('Enter Comment', validators=[Required()])
    post = SubmitField('Post Comment')
class SubscriptionForm(FlaskForm):
    name = StringField('First Name', validators=[Required()])
    subscription_data = StringField('Email', validators=[Required()])
    subscribe = SubmitField('Subscribe')
class UpdatePostForm(FlaskForm):
    # title = StringField('Title', validators=[Required()])
    blog_post = TextAreaField('Type Blog here', validators=[Required()])
    submit=SubmitField('SUBMIT')
