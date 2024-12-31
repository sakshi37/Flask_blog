from flask_blog import db, login_manager, app
from itsdangerous import URLSafeSerializer
from itsdangerous import URLSafeTimedSerializer

from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)  # Corrected typo from 'usernam' to 'username'
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(120), nullable=True, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)  # Changed 'post' to 'posts' for consistency

    def get_reset_token(self, expires_sec=1800):
        try:
            s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
            print(f"Serializer created successfully with secret key: {app.config['SECRET_KEY']}")
            token = s.dumps({'user_id': self.id})
            print(f"Generated token: {token}")
            return token
        except Exception as e:
            print(f"Error while generating token: {e}")
            raise e

    @staticmethod
    def verify_reset_token(token):
        s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None 
        return User.query.get(user_id)


    def __repr__(self):
        return f"user({self.username}, {self.email}, {self.image_file})"  # Fixed typo in __repr__

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)  # Increased length of title for flexibility
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)  # Adjusted 'nullable' as needed

    def __repr__(self):
        return f"Post({self.title}, {self.date_posted})"


