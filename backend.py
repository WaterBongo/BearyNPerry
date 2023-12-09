import flask


app = flask.Flask("berrynperry")

@app.route("/")
def main():
    return "lol"


app.run('0.0.0.0',port=8080)