import streamlit as st
import pandas as pd
import datetime

# Streamlit UI
st.set_page_config(
    page_title="Prototype-Insighthub",
    page_icon="👋",
)
st.divider()
st.markdown(
        "<h3 style='text-align: center; color: white;'>InsightHub: Empowering Investment Decisions in India's Entrepreneurial Landscape </h1>",
        unsafe_allow_html=True)
st.markdown('')
st.markdown('**Overview**')
df = pd.DataFrame({
    'first column': ['', 'Start-up Founder', 'Venture Capitalist'],
    })

option = st.selectbox(
    'You are:',
     df['first column'])

'You selected: ', option
    
