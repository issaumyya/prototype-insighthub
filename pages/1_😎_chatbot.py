import openai
import streamlit as st

# Set page title
st.title("ChatBot")

# Connect OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"
# Initialize messages attribute if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Display assitant message in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        # Simulate stream of response with milliseconds delay
        stream = openai.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            #will provide lively writing
            stream=True,
        )
        response = st.write_stream(stream)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
