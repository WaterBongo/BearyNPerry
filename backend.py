import flask,base64
from flask import request
ip = "127.0.0.1:8080/"


app = flask.Flask("berrynperry")

user_db = {
    "Summer Shen": {
        "name" : "Summer Shen",
        "subject":"English",
        "Bio":"SGVsbG8sIEknbSBTdW1tZXIgU2hlbiEKCkkgYW0gYSBkZWRpY2F0ZWQgbWVudG9yIG9uIEJlcnJ5IG4gcGVycnksIGZvY3VzZWQgb24gZW1wb3dlcmluZyBzdHVkZW50cywgcGFydGljdWxhcmx5IHRob3NlIHdobyBtaWdodCBub3QgaGF2ZSBlYXN5IGFjY2VzcyB0byB0aGUgcmVzb3VyY2VzIHRoZXkgbmVlZCB0byBleGNlbCBhY2FkaWNhbGx5LgoKIyMgQWJvdXQgTWUKCkkgZ3JhZHVhdGVkIHdpdGggYSBCYWNoZWxvcnMgaW4gQ2hpbGRyZW4gRWR1Y2F0aW9uIGZyb20gVW5pdmVyc2l0eSBvZiBDYWxpZm9ybmlhLCBCZXJrZWxleS4gSSBoYXZlIGJlZW4gdGVhY2hpbmcgZm9yIG92ZXIgZWlnaHQgeWVhcnMgbm93LCBmb2N1c2luZyBwYXJ0aWN1bGFybHkgb24gTWF0aGVtYXRpY3MgYW5kIEVuZ2xpc2ggTGl0ZXJhdHVyZSBmb3IgY2hpbGRyZW4gYWdlZCAxMC0xNS4KCiMjIE15IFZhbHVlcyAKCkkgZmlybWx5IGJlbGlldmUgdGhhdCBldmVyeSBjaGlsZCBoYXMgdGhlIHBvdGVudGlhbCB0byBleGNlbCwgYW5kIGl0J3Mgb3VyIGR1dHkgdG8gaGVscCB0aGVtIGRpc2NvdmVyIGFuZCBudXJ0dXJlIHRoZWlyIGNhcGFiaWxpdGllcy4gSSBzdHJpdmUgdG8gaW5zdGlsbCBhIHBhc3Npb24gZm9yIGxlYXJuaW5nIGFuZCBjdXJpb3NpdHkgaW4gZWFjaCBvZiBteSBzdHVkZW50cywgd2hpY2ggSSBiZWxpZXZlIGFyZSB0aGUgZm91bmRhdGlvbnMgZm9yIGxpZmVsb25nIGxlYXJuaW5nLgogICAgICAgIA==",
        "contact":{
            "number":"4084084081",
            "discord":"ihatekiwis",
            "email":"pooh@gmail.com"
        }
    },
    "Edward He" : {
        "name" : "Edward He",
        "subject":"Math",
        "Bio":"SW50cm9kdWN0aW9uCgpIZWxsbyB0aGVyZSEgTXkgbmFtZSdzIEVkd2FyZCBIZS4KCkkgYW0gdGhyaWxsZWQgdG8gYmUgYSBwYXJ0IG9mIHRoZSBCZXJyeSBuIFBlcnJ5IHRlYW0sIHByb3ZpZGluZyBhY2Nlc3NpYmxlIGFuZCBwZXJzb25hbGlzZWQgZWR1Y2F0aW9uYWwgc3VwcG9ydCBmb3IgY2hpbGRyZW4gd2hvIG1heSBiZSBsZXNzIHByaXZpbGVnZWQuCgpBYm91dCBNZQoKSSBhbSBhIGdyYWR1YXRlIGluIFNjaWVuY2UgRWR1Y2F0aW9uIGZyb20gdGhlIFVuaXZlcnNpdHkgb2YgUGVubnN5bHZhbmlhIHdpdGggYSBzcGVjaWFsaXphdGlvbiBpbiBQaHlzaWNzIGFuZCBDaGVtaXN0cnkgZm9yIGtpZHMgYWdlZCAxMCB0byAxNSB5ZWFycyBvbGQuIE92ZXIgdGhlIGNvdXJzZSBvZiB0ZW4geWVhcnMgaW4gdGhlIGVkdWNhdGlvbiBzZWN0b3IsIEkgaGF2ZSBkZXZlbG9wZWQgYSBwYXNzaW9uIGZvciBtYWtpbmcgY29tcGxleCBjb25jZXB0cyB1bmRlcnN0YW5kYWJsZSBhbmQgZW5qb3lhYmxlIGZvciB0aGUgeW91bmcgbWluZHMuCgpNeSBJZGVvbG9neSAKCkkgYmVsaWV2ZSBzdHJvbmdseSBpbiB0aGUgaGlkZGVuIHRhbGVudHMgZXZlcnkgY2hpbGQgcG9zc2Vzc2VzLiBJdCBpcyBteSBtaXNzaW9uLCBhcyBhIHR1dG9yLCB0byBndWlkZSB0aGVtLCBoZWxwIHRoZW0gdW5kZXJzdGFuZCB0aGVpciBwb3RlbnRpYWwsIGFuZCBpbnN0aWxsIGEgbG92ZSBmb3IgbGVhcm5pbmcgdGhhdCBpcyBib3VuZCB0byBsYXN0IGEgbGlmZXRpbWUuClJlbWVtYmVyLCBlZHVjYXRpb24gY2FuIGNoYW5nZSBsaXZlcywgYW5kIHRvZ2V0aGVyIHdlIGNhbiBtYWtlIGEgZGlmZmVyZW5jZSE===",
        "contact":{
            "number":"408-408-4081",
            "discord":"ihatekiwis",
            "email":"icrashcars@gmail.com"
        }
    },
    "Jinx" : {
        "name" : "Jinx",
        "subject":"CS",
        "Bio":"SW50cm9kdWN0aW9uCgpHcmVldGluZ3MhIEknbSBKaW54LCB5b3VyIGZlbGluZSBndWlkZSBhbmQgZnJpZW5kIGluIHRoZSBqb3lmdWwgam91cm5leSBvZiBsZWFybmluZy4KCkJlaW5nIGFuIHVuaXF1ZSBwYXJ0IG9mIEJlcnJ5IG4gUGVycnksIEkgaGVscCBraWRzIGZyb20gbGVzcyBmb3J0dW5hdGUgYmFja2dyb3VuZHMgZGl2ZSBpbnRvIHRoZSB3b3JsZCBvZiBsZWFybmluZyBpbiBhIGZ1biBhbmQgZW5nYWdpbmcgd2F5LgoKQWJvdXQgTWUKCldpdGggbXkgZmVsaW5lIHN1cGVycG93ZXJzLCBJIG5hdmlnYXRlIGNoaWxkcmVuIHRocm91Z2ggZGlmZmVyZW50IHN1YmplY3RzIHNwYXJraW5nIGN1cmlvc2l0eSBhbmQgZW5jb3VyYWdpbmcgZXhwbG9yYXRpb24uIEkgc3BlY2lhbGl6ZSBpbiBtYWtpbmcgbGVhcm5pbmcgZnVuLCBieSB1c2luZyBteSBsb3ZlIGZvciBwbGF5IHRvIHRlYWNoIHZhbHVhYmxlIGxlc3NvbnMuCgpNeSBJZGVvbG9neSAKCkFzIGEgY2F0LCBJJ20gbmF0dXJhbGx5IGN1cmlvdXMgYW5kIHRoYXQncyB3aGF0IEkgc2VlayB0byBpbnNwaXJlIGluIG15IHN0dWRlbnRzIC0gYSBkZXNpcmUgdG8gZXhwbG9yZSBhbmQgbGVhcm4uIEkgYmVsaWV2ZSBldmVyeSBjaGlsZCBoYXMgcG90ZW50aWFsLCBhbmQgaXQncyBvdXIgam9iIHRvIGd1aWRlIHRoZW0gdG8gZGlzY292ZXIgdGhhdCwgd2l0aCBhIHBhd2Z1bCBvZiBmdW4h===",
        "contact":{
            "number":"408-408-4081",
            "discord":"ihatekiwis",
            "email":"gatoeatpeople@mail.ru"
        }
    }
}

@app.route("/")
def main():
    return "lol"

@app.route("/lookup",methods=["POST"])
def lookup():
    data = request.json
    subject_to_search = data['subject']
    teacher = search(subject_to_search)
    return teacher
    #{"subject":"cs"}

def search(subject):
    for i in user_db.values():
        if i["subject"] == subject:
            return i


@app.route("/addpeople",methods=["POST"])
def add_teacher():
    req_json = request.json
    #convert json to dict
    name = req_json['name']
    #offuscate the bio with b64
    bio = req_json['Bio']
    byte_data = bio.encode('utf-8')
    encoded_data = base64.b64encode(byte_data)
    req_json['Bio'] = encoded_data
    user_db[name]=req_json
    print(user_db)
    return "hehe"

app.run('0.0.0.0',port=8080)