import openai
import streamlit as st

st.title("ChatBot")

# Connect OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Initialize messages attribute if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize OpenAI model in session state if it doesn't exist
if "openai_model" not in st.session_state:
    st.session_state.openai_model = "text-davinci-002"  # Change this to your desired model

if prompt := st.text_input("What is up?"):
    # Append user message to session state messages
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message in chat message container
    st.text(f"User: {prompt}")

    # Display assistant message in chat message container
    full_response = ""
    # Simulate stream of response with milliseconds delay
    for response in openai.ChatCompletion.create(
        model=st.session_state.openai_model,
        messages=[
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ],
        # Will provide lively writing
        stream=True,
    ):
        # Get content in response
        full_response += response.choices[0].delta.get("content", "")
        # Add a blinking cursor to simulate typing
        st.text(f"Assistant: {full_response}▌")
    st.text(f"Assistant: {full_response}")
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
