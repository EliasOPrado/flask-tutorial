#Make sure the directy/path is right
from flask import Flask, render_template, flash, redirect, url_for, session, logging
from data import Articles
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, Validators
#password incription
from passlib.hash import sha256_crypt 
#to not confund: this brings the Article function to the article() function
Articles = Articles()

app = Flask (__name__)
#to not need to re-launch the server
app.debug = True

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

#articles=articles will give the template its path and route
@app.route("/articles")
def articles():
    return render_template("articles.html", articles= Articles)


@app.route("/article/<string:id>")
def article(id):
    return render_template("article.html", id=id)

#create a class for each form with wtforms
#definig for users table
class registerForm(form):
	name = StringField('Name', [validators.kength(min=1, max=50)])
	username = StringField('Username', [validators.length(min=4, max=25)])
	email = StringField('Email', [validators.lengh(min=6, max=50)])
	password = PasswordField('Password', [
          validators.DataRequired(),
          validators.EqualTo('confirm', message='Passwords do not match')
		])
	confirm = PasswordField('Confirm Password')

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = registerForm(request.form)
	if request.method == 'POST' and form.validate():
		return render_template('register.html')		

    #return render_template('register.html', form=form)

if __name__ == "__main__":
    app.run()


