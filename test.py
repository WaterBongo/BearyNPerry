import requests

user_db = {
    "Summer": {
        "name":"Summer",
        "subject":"CS",
        "Bio":"I am beary",
        "link":"zoom-link",
        "contact":{
            "number":"4084084081",
            "discord":"ihatekiwis",
            "email":"pooh@gmail.com"
        }
    }
}
subject='CS'
users = []
def search():
    for i in user_db.values():
        if i["subject"] == subject:
            users.append(i)
    return users
print(search())
# import requests


ip = "127.0.0.1:8080/"

r = requests.post(ip,json={"subject":"cs"})
print(r.text)