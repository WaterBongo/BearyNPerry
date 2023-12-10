import streamlit as st
import webbrowser,requests,base64

st.markdown("# Find Tutors! ❄️")
st.sidebar.markdown("# Finder ❄️")
st.sidebar.image("./assets/logo.png", width=250)

tab1, tab2, tab3,tab4 = st.tabs(["English", "Math", "Computer Science","new users"])

with tab1:
   r = requests.post('http://127.0.0.1:8080/lookup',json={"subject":"English"})
   person_json = r.json()
   print(person_json)
   col1, col2 = st.columns(2)
   with col1:
    st.header("English Volunteers")
    st.image("./assets/summer.png")
    st.text(f"Phone Number : {person_json['contact']['number']}")
    st.text(f"Email : {person_json['contact']['email']}")
    bio = base64.b64decode(person_json['Bio']).decode('utf-8')
    #decode bio, its in base64
    if st.button("Book now!"):
      webbrowser.open("https://BearynPerry.as.me/")
      #redirect to https://BearynPerry.as.me/
      

   with col2:
    st.title("Summer Shen")
    st.markdown(bio)


with tab2:
    r = requests.post('http://127.0.0.1:8080/lookup',json={"subject":"Math"})
    rjson = r.json()
    print(rjson)
    col1, col2 = st.columns(2)
    with col1:
        st.header("Math Volunteers")
        st.image("./assets/edward.png")
        st.text(f"Phone Number : {rjson['contact']['number']}\nEmail : {rjson['contact']['email']}")
        if st.button("book now!"):
           webbrowser.open("https://BearynPerry.as.me/")

    with col2:
        #decode the bio
        bio = base64.b64decode(rjson['Bio']).decode('utf-8')
        st.markdown(bio)
with tab3:
   r = requests.post('http://127.0.0.1:8080/lookup',json={"subject":"CS"})
   rjson=r.json()
   print(rjson)
   col1, col2 = st.columns(2)
   with col1:
    st.header("Comp Sci Pro")
    st.image('./assets/gato.png', width=200)
    st.text("Phone Number : 408-408-4081\nEmail : gatoeatpeople@mail.ru")
    if st.button("order now!"):
      webbrowser.open("https://BearynPerry.as.me/")
    with col2:
        st.markdown("""
# Jinx
### Introduction

Greetings! I'm Jinx, your feline guide and friend in the joyful journey of learning.

Being an unique part of Berry n Perry, I help kids from less fortunate backgrounds dive into the world of learning in a fun and engaging way.

## About Me

With my feline superpowers, I navigate children through different subjects sparking curiosity and encouraging exploration. I specialize in making learning fun, by using my love for play to teach valuable lessons.

## My Ideology 

As a cat, I'm naturally curious and that's what I seek to inspire in my students - a desire to explore and learn. I believe every child has potential, and it's our job to guide them to discover that, with a pawful of fun!
""")