from flask import Flask, render_template, url_for
app = Flask(__name__)

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
    return render_template("home.html", posts=posts, title="About")

@app.route("/about")
def about():
    return render_template("about.html")

app.run(
    host="0.0.0.0",
    port=80,
    debug=True)