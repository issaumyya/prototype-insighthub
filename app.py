import streamlit as st
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.header('I N S I G H T  H U B', divider='blue')
st.subheader('_Empowering_ enterpreneur landscape of :blue[India] :sunglasses:')
col1, col2, col3 = st.column((3))
with col1:
    if st.button("Fellow Investor?"):
        st.switch_page("pages/2_InvestorZone.py")
with col2:
    if st.button("Fellow Founder?"):
        st.switch_page("pages/3_FoundersZone.py")
with col3:
    if st.button("Talk to Us!"):
        st.switch_page("pages/1_TalkToUs.py")

tab1, tab2, tab3 = st.tabs(["India", "Global", "About Us"])
    with tab1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
    with tab2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
    with tab3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
