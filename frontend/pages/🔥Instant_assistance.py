import streamlit as st
import openai,json


with open('./assets/config.json','r') as f:
    data = f.read()
    config = json.loads(data)
    openai.api_key = config['openai_key']
if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
        st.session_state.messages = [
        {"role": "assistant", "content": "Hello there! I'm your friendly Berry AI. I'm here to guide you through our tutoring services and help you find the perfect fit for your learning needs. Let's embark on this exciting journey to knowledge together!"}  # add this line    
        ]


# Create a DataFrame from the data
# Display the chart
for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            for response in openai.ChatCompletion.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            ):
                full_response += response.choices[0].delta.get("content", "")
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})

