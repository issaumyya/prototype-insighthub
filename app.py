import streamlit as st
st.title("Welcome to InsightHub!")
sectors = ["Upto 2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
no_of_unicorns = [4,3,3,2,1,10,7,12,45,22,2]
uni_fig = px.bar(x=sectors, y=no_of_unicorns)
st.plotly_chart(uni_fig,use_container_width=True, height = 150)
st.markdown(textbox_style, unsafe_allow_html=True)
st.markdown(f"<div class='textbox'><h3>✅ Only 2 Unicorns were Minted in 2023, a decline by 91% from last year<h3></div>", unsafe_allow_html=True)
