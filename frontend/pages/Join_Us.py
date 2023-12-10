import streamlit as st
import requests
st.sidebar.image("./assets/logo.png", width=250)
def main():
    st.title("Join Us")
    st.write("Please provide your information to join us.")
    name = st.text_input("Name")
    subject = st.text_input("Subject")

    phone_number = st.text_input("Phone Number")
    email = st.text_input("Email")
    markdown = st.text_area("Introduction (Markdown)")

    if st.button("Submit"):
        # Save the user's information
        save_user_info(subject,name,phone_number, email, markdown)
        st.success("Thank you for joining us!")

def save_user_info(subject,name,phone_number, email, markdown):
    thin = {
        'Bio': markdown, 'contact': {'discord': 'test', 'email': email, 'number': phone_number}, 'name': name, 'subject': subject}

    # Save the user's information to a database or file
    # You can customize this function based on your needs
    # For example, you can use a database library like SQLAlchemy or write to a file
    # Your code here
    ip = "http://127.0.0.1:8080/addpeople"
    r = requests.post(ip,json=thin)
    print(r.text)


if __name__ == "__main__":
    main()
