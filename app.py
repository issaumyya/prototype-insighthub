import streamlit as st
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
st.page_link('streamlit_app.py', label='Home Page', icon='📈')

textbox_style = """
    <style>
        .textbox {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            border: 1px solid rgba(255, 255, 255, 0.18);
            color: #076D90;
            text-align: center;
        }
        .textbox h3{
            font-size: 18px;
            font-weight: bold;
            margin: 0;
        }
    </style>
"""
with st.sidebar:
        with st.popover("Open popover"):
                name = st.text_input("What's your name?")
st.title("Welcome to InsightHub,", name)

sectors = ["Upto 2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
no_of_unicorns = [4,3,3,2,1,10,7,12,45,22,2]
uni_fig = px.bar(x=sectors, y=no_of_unicorns)
col1, col2 = st.columns((2))
with col2:
    st.plotly_chart(uni_fig,use_container_width=True, height = 150)
    st.markdown(textbox_style, unsafe_allow_html=True)
    st.markdown(f"<div class='textbox'><h1>2</h1> <h3>Unicorns were Minted in 2023, a decline by 91% from last year<h3></div>", unsafe_allow_html=True)
