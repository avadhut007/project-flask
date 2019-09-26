from flask import Flask, render_template, url_for, flash, redirect
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
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data} !', 'success')
        return redirect(url_for('home'))
        
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('Yopu have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. please check username and password', 'danger')            
    return render_template('login.html', title='Login', form=form)
    


if __name__ == "__main__":
    app.run(debug=True)    