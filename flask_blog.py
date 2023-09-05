from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fa4b9769bf92b5de1b3dd7f000be7bb2'

posts = [
    {
        'author': 'Nikki Vaughan',
        'title': 'Blog Post 1',
        'content': 'First blog post',
        'date_posted': 'Aug 19, 2023'
    },
    {
        'author': 'Nikki Vaughan',
        'title': 'Blog Post 2',
        'content': 'Second blog post',
        'date_posted': 'Aug 20, 2023'
    }
]
    
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts, title="Home")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash("Account created for {}!".format(form.username.data), 'success')
        return redirect(url_for('home'))
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash("You have been logged in!", 'success')
            redirect(url_for('home'))
        else:
            flash("Login unsuccessful. Please check username and password", 'danger')
    return render_template('login.html', title='Login', form=form)

app.run(
    host="0.0.0.0",
    port=80,
    debug=True)