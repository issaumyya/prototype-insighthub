import openai
import streamlit as st

# Set page title
st.title("ChatBot")

# Connect OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Initialize openai_model if not present in session state
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Initialize messages attribute if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Handle user input and display chat messages
if prompt := st.text_input("You:"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message in chat message container
    st.write("User:", prompt)

    # Display assistant message in chat message container
    full_response = ""
    for response in openai.ChatCompletion.create(
        model=st.session_state["openai_model"],
        messages=st.session_state.messages,
        # Will provide lively writing
        stream=True,
    ):
        full_response += response.choices[0].text.strip()
        # Display assistant message in chat message container
        st.write("Assistant:", full_response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
