import flask
import sqlite3

conn = sqlite3.connect('tutoring.db')
cursor = conn.cursor()

app = flask.Flask("berrynperry")

user_db = {
    "Summer": {
        "subject":"CS",
        "Bio":"I am beary",
        "contact":{
            "number":"4084084081",
            "discord":"ihatekiwis",
            "email":"pooh@gmail.com"
        }
    }
}

@app.route("/")
def main():
    return "lol"

@app.route("/lookup",methods=["POST"])

def lookup(subject):
    cursor.execute('SELECT * FROM users WHERE bio LIKE ?', ('%' + subject + '%',))
    results = cursor.fetchall()
    return results

app.run('0.0.0.0',port=8080)