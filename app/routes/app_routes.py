from app import app
from app.forms import SignupForm, LoginForm
from app import db
from flask_login import current_user, login_user
from app.models import User

# signup route
# http://127.0.0.1:5000/signup
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SignupForm()
    if form.validate_on_submit():
        user = User(
            firstname=form.firstname.data, 
            middlename=form.middlename.data, 
            lastname=form.lastname.data, 
            phone=form.phone.data, 
            email=form.email.data
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('signup.html', title='Register', form=form)

# login route
# http://127.0.0.1:5000/login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


# product route
# http://127.0.0.1:5000/
@app.route('/')
def index():
    return "Helo world"


# page not found route
# http://127.0.0.1:5000/


# internal server route
# http://127.0.0.1:5000/
