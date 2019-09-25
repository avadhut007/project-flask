from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

#secrets.token_hex(16)
app.config['SECRET_KEY']='89411675b09c95600928be84bf9cc0ec'

posts = [

    {
        'author':'Tony Stark',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'September 20, 2019'
    },

    {
        'author':'Steve Rogers',
        'title':'Blog Post 2',
        'content':'Second post content',
        'date_posted':'September 21, 2019'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)
    


if __name__ == "__main__":
    app.run(debug=True)    