from flask import Flask, render_template
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b7eceba8acfddfdbde122bb16f221846';

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]



@app.route("/")
@app.route("/home")
def hello():
  return render_template("home.html", posts=posts, title='Home page')


@app.route("/about")
def about():
  return render_template("about.html", title='About')

if __name__ == '__main__':
  app.run(debug=True)