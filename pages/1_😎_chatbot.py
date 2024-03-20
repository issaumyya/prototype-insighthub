import openai
import streamlit as st

# Set page title
st.title("ChatBot")

# Connect OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Initialize messages attribute if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize OpenAI model in session state if it doesn't exist
if "openai_model" not in st.session_state:
    st.session_state.openai_model = "text-davinci-002"  # Change this to your desired model

# Function to display chat messages
def display_chat_message(role, content):
    if role == "user":
        # Style user message
        st.write(f'<div style="background-color: #d1e8ff; padding: 10px; border-radius: 10px; text-align: right;">{content}</div>', unsafe_allow_html=True)
    elif role == "assistant":
        # Style assistant message
        st.write(f'<div style="background-color: #e2f3ff; padding: 10px; border-radius: 10px; text-align: left;">{content}</div>', unsafe_allow_html=True)

# User input prompt
prompt = st.text_input("You:", key="user_input")

# Process user input and display chat messages
if st.button("Send"):
    if prompt:
        # Append user message to session state messages
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Display user message
        display_chat_message("user", prompt)

        # Display assistant message
        full_response = ""
        for response in openai.ChatCompletion.create(
            model=st.session_state.openai_model,
            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
            stream=True,
        ):
            full_response += response.choices[0].delta.get("content", "")
            display_chat_message("assistant", full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
