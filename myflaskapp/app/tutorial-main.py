# from flask import Flask, render_template, request
# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, BooleanField, SubmitField
# from wtforms.validators import DataRequired, Length
# from flask_sqlalchemy import SQLAlchemy
# import os


# # create new flask application instance from Flask class
# # __name__ > name of app - helps to locate resources like template / static files
# app = Flask(__name__)

# # define routes to views to handle all incoming requests

# @app.route('/')
# def index():
#     return 'Hello, World' 


# # dynamic route
# @app.route('/user/<username>')
# def profile(username):
#     return render_template('test_user.html', first_name=username)

# # use template
# @app.route('/user/<first_name>/<last_name>')
# def names(first_name, last_name):
#     return render_template('test_user.html', first_name=first_name, last_name=last_name)

# # easy form intro

# # check for method from request object that has all request data in it
# # @app.route('/login', methods=['GET', 'POST'])
# # def login():
# #     if request.method == 'POST':
# #         username = request.form['username']
# #         password = request.form['password']
# #         # handle user input, e.g. validate pw and save user in DB
# #         print(username, password)
# #         return render_template('login.html')        
# #     else:
# #         return render_template('login.html')

# class LoginForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
#     password = PasswordField('Password', validators=[DataRequired()])
#     remember_me = BooleanField(' Remember Me')
#     submit = SubmitField('Log In')

# # we also have access to the config values of our app
# app.config['SECRET_KEY'] = 'secret_key' # better to generate this somehow

# # from intro with library

# # @app.route('/login', methods=['GET', 'POST'])
# # def login():
# #     form = LoginForm()
# #     if form.validate_on_submit():
# #         # handle user input here, e.g. db storage
# #         print(form)
# #         print(form.username)
# #         pass
# #     return render_template('new_login.html', form=form)

# # for practice, we keep the config here, but better in seprarate file

# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'test.db')}"


# # db = SQLAlchemy(app) # to the constructor we pass the instance of our app

# # # 1. Create Models
# # class User(db.Model):
# #     id = db.Column(db.Integer, primary_key = True)
# #     username = db.Column(db.String, unique = True, nullable = False)
# #     email = db.Column(db.String(120), unique=True, nullable=True)

# #     def __repr__(self):
# #         return f"<User '{self.username}'>"

# # # 2. Migrate Models to DB > will create data in SQlite DB

# # with app.app_context(): # this line is required to make DB work with app
# #     db.create_all() # adds models to db

# #     # 3. Add Data
# #     user1 = User(username='testuser3', email='testuser3@test.com')
# #     user2 = User(username='testuser2')
# #     db.session.add(user1)
# #     # db.session.add(user2)
# #     db.session.commit()

# # # 4. Query Data
# #     users = User.query.all()
# #     testuser = User.query.filter_by(username='testuser3').first()
# #     print(users)
# #     print(testuser)
# #     print(testuser.email)

# # like we did @app.route to handle our own routes
# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('404.html'), 404

# # Static Files
# # 1. Set up static directory
# # 2. url_for() - get the path for a static file