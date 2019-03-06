from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class CommentForm(FlaskForm):
   
#    title = StringField('Comment title',validators=[Required()])
   comment = TextAreaField('posts', validators=[Required()])
   submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class AddBlogForm(FlaskForm):
    category= SelectField('Category:',choices=[('blog posts','comment blog'),('recent posts','quotes'),('update','delete blog')])
    content=TextAreaField('Blog',validators = [Required()])
    submit=SubmitField('SUBMIT')