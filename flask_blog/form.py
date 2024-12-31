from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField , SubmitField, BooleanField, EmailField, ValidationError, TextAreaField
from wtforms.validators import DataRequired,Length,Email, EqualTo
from flask_blog.models import User



class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    email = EmailField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm_password',
                                   validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('sign up')


    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("That usernane is taken please use another username")
    
    def validate_email(self, email):
        user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("That email is taken please use another username")

class LoginForm(FlaskForm):
    
    email = EmailField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    email = EmailField('Email',validators=[DataRequired(),Email()])
    picture = FileField('Update profile pic',validators=[FileAllowed(['jpg','png'])])
       
    submit = SubmitField('Update')


    def validate_username(self,username):
        if username.data != current_user.username:
            user=User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError("That usernane is taken please use another username")
    
    def validate_email(self, email):
        if email.data != current_user.email:
            user=User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("That email is taken please use another username")
            
class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class RequestResetForm(FlaskForm):
    email = EmailField('Email', validators=[ DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_username(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError(" That is no account with that email. You must register first ")

class RestPasswordForm(FlaskForm):
     password = PasswordField('Password',validators=[DataRequired()])
     confirm_password = PasswordField('Confirm_password',
                                   validators=[DataRequired(), EqualTo('password')])
     submit = SubmitField("Reset Password")




                        
                        
                        

