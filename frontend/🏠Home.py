import streamlit as st
from io import BytesIO




st.set_page_config(page_title="Aura")
SERVER_URL = "http://127.0.0.1:8080/upload_video"
# Define sidebar
#add a logo the top left
st.sidebar.image("./assets/logo.png", width=250)
#add text
st.markdown("# Beary N Perry🎈")
st.markdown("## Main Page <3")
st.text("""
Welcome to the world of better learning, where everyone has access
to quality education!

Our innovative app is designed to bridge the education gap
and offer affordable peer-to-peer tutoring for children from
less privileged backgrounds. We believe that every child
deserves the opportunity to learn, grow, and excel regardless of their circumstances.


Join us in our mission to create an inclusive environment
where every child can shine! Because at Beary n perry,
we believe in the power of education to change lives.
Together, we can make a difference, and together, we can build a brighter future.
        
                                                - Love Edward and Summer
""")
st.image("./assets/logo.png",width=250)

st.sidebar.markdown("# Main page 🎈")
st.sidebar.image("./assets/logo.png", width=250)
