import streamlit as st
import webbrowser,requests

st.markdown("# Find Tutors! ❄️")
st.sidebar.markdown("# Finder ❄️")
st.sidebar.image("./assets/logo.png", width=250)

tab1, tab2, tab3 = st.tabs(["English", "Math", "Computer Science"])

with tab1:
   r = requests.post('http://127.0.0.1:8080/lookup',json={"subject":"English"})
   person_json = r.json()
   col1, col2 = st.columns(2)
   with col1:
    st.header("English Volunteers")
    st.image("./assets/summer.png")
    st.text("Phone Number : 408-408-4081")
    st.text("Email : summertimes@gmail.com")
    if st.button("Book now!"):
      webbrowser.open("https://BearynPerry.as.me/")
      #redirect to https://BearynPerry.as.me/
      

   with col2:
    st.title("Summer Shen")
    st.markdown("""
### Introduction!
Hello, I'm Summer Shen!

I am a dedicated mentor on Berry n perry, focused on empowering students, particularly those who might not have easy access to the resources they need to excel acadically.

## About Me

I graduated with a Bachelors in Children Education from University of California, Berkeley. I have been teaching for over eight years now, focusing particularly on Mathematics and English Literature for children aged 10-15.

## My Values 

I firmly believe that every child has the potential to excel, and it's our duty to help them discover and nurture their capabilities. I strive to instill a passion for learning and curiosity in each of my students, which I believe are the foundations for lifelong learning.
                
""")


with tab2:
    r = requests.post('http://127.0.0.1:8080/lookup',json={"subject":"Math"})
    rjson = r.json()
    col1, col2 = st.columns(2)
    with col1:
        st.header("Math Volunteers")
        st.image("./assets/edward.png")
        st.text("Phone Number : 408-408-4081\nEmail : icrashcars@gmail.com")
        if st.button("book now!"):
           webbrowser.open("https://BearynPerry.as.me/")

    with col2:
        st.markdown("""
### Introduction

Hello there! My name's Edward He.

I am thrilled to be a part of the Berry n Perry team, providing accessible and personalised educational support for children who may be less privileged.

## About Me

I am a graduate in Science Education from the University of Pennsylvania with a specialization in Physics and Chemistry for kids aged 10 to 15 years old. Over the course of ten years in the education sector, I have developed a passion for making complex concepts understandable and enjoyable for the young minds.

## My Ideology 

I believe strongly in the hidden talents every child possesses. It is my mission, as a tutor, to guide them, help them understand their potential, and instill a love for learning that is bound to last a lifetime.
Remember, education can change lives, and together we can make a difference!
""")
with tab3:
   r = requests.post('http://127.0.0.1:8080/lookup',json={"subject":"CS"})
   rjson=r.json()
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