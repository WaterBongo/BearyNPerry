import requests

# user_db = {
#     "Summer": {
#         "name":"Summer",
#         "subject":"CS",
#         "Bio":"I am beary",
#         "link":"zoom-link",
#         "contact":{
#             "number":"4084084081",
#             "discord":"ihatekiwis",
#             "email":"pooh@gmail.com"
#         }
#     }
# }
# subject='CS'
# users = []
# def search():
#     for i in user_db.values():
#         if i["subject"] == subject:
#             users.append(i)
#     return users
# print(search())
# # import requests


ip = "http://127.0.0.1:8080/addpeople"
thin = {'Bio': 'SW50cm9kdWN0aW9uCgpHcmVldGluZ3MhIEknbSBKaW54LCB5b3VyIGZlbGluZSBndWlkZSBhbmQgZnJpZW5kIGluIHRoZSBqb3lmdWwgam91cm5leSBvZiBsZWFybmluZy4KCkJlaW5nIGFuIHVuaXF1ZSBwYXJ0IG9mIEJlcnJ5IG4gUGVycnksIEkgaGVscCBraWRzIGZyb20gbGVzcyBmb3J0dW5hdGUgYmFja2dyb3VuZHMgZGl2ZSBpbnRvIHRoZSB3b3JsZCBvZiBsZWFybmluZyBpbiBhIGZ1biBhbmQgZW5nYWdpbmcgd2F5LgoKQWJvdXQgTWUKCldpdGggbXkgZmVsaW5lIHN1cGVycG93ZXJzLCBJIG5hdmlnYXRlIGNoaWxkcmVuIHRocm91Z2ggZGlmZmVyZW50IHN1YmplY3RzIHNwYXJraW5nIGN1cmlvc2l0eSBhbmQgZW5jb3VyYWdpbmcgZXhwbG9yYXRpb24uIEkgc3BlY2lhbGl6ZSBpbiBtYWtpbmcgbGVhcm5pbmcgZnVuLCBieSB1c2luZyBteSBsb3ZlIGZvciBwbGF5IHRvIHRlYWNoIHZhbHVhYmxlIGxlc3NvbnMuCgpNeSBJZGVvbG9neSAKCkFzIGEgY2F0LCBJJ20gbmF0dXJhbGx5IGN1cmlvdXMgYW5kIHRoYXQncyB3aGF0IEkgc2VlayB0byBpbnNwaXJlIGluIG15IHN0dWRlbnRzIC0gYSBkZXNpcmUgdG8gZXhwbG9yZSBhbmQgbGVhcm4uIEkgYmVsaWV2ZSBldmVyeSBjaGlsZCBoYXMgcG90ZW50aWFsLCBhbmQgaXQncyBvdXIgam9iIHRvIGd1aWRlIHRoZW0gdG8gZGlzY292ZXIgdGhhdCwgd2l0aCBhIHBhd2Z1bCBvZiBmdW4h===', 'contact': {'discord': 'ihatekiwis', 'email': 'gatoeatpeople@mail.ru', 'number': '408-408-4081'}, 'name': 'Jinx', 'subject': 'CS'}
r = requests.post(ip,json=thin)
print(r.text)