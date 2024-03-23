import streamlit as st
import pandas as pd
from plotly.express import px
import plotly.graph_objects as go

data = pd.read_csv("StartupIndiaStats.csv")

# Create initial columns with desired ratio (3:1:1)
col1, col2, col3 = st.columns([3, 1, 1])

# Create a container within the first column
with col1:
  st.title("Indian Startups at a Glance")
  fig_state_distribution = px.bar(
    data, x="State", y="Startups", title="Distribution of Startups Across States")
    st.plotly_chart(fig_state_distribution)

# Add content to columns and nested columns
with col2:
  st.write("Content in Column 2")

with col3:
  st.write("Content in Column 3")
