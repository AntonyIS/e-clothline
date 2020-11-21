from app import app



# signup route
# http://127.0.0.1:5000/signup


# login route
# http://127.0.0.1:5000/login


# product route
# http://127.0.0.1:5000/
@app.route('/')
def index():
    return "Helo world"


# page not found route
# http://127.0.0.1:5000/


# internal server route
# http://127.0.0.1:5000/
