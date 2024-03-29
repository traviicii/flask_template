from . import app, db

@app.route("/")
def homepage():
    return "Look we did it!"

@app.route("/test")
def test():
    return "THIS TEST WORKED"