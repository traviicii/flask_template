from . import app, db

# create accessible routes for our application functionality

@app.route("/")
def homepage():
    return "Look we did it!"

@app.route("/test")
def test():
    return "THIS TEST WORKED"