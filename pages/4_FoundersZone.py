import streamlit as st

# Create columns
col1, col2, col3 = st.columns([1, 3, 2])

# Add content to each column
with col1:
    st.subheader("#1  16.")
    st.write("19")

with col2:
    st.subheader("#2 - Some metrics insights")
    st.subheader("based on clusters")
    st.write("#3- Filters on the")
    st.write("basis of region")
    st.write("#4-Felter on the basis")
    st.write("of sector")
    st.write("#5-")
    st.write("geospatial distru-")
    st.write("bution with hover")
    st.write("on some nalues.")
    st.write("#6 same as #2")

with col3:
    st.subheader("#7 - Based on any")
    st.write("growith trend.")
    st.write("amalgamation")
    st.write("(Rev.")
    st.write("groveta")
    st.write("th")  
    st.subheader("#8& #9-risk estimation/factor importance")
    st.write("#10")
    st.write("some motivational quote.")
