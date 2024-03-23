import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("StartupIndiaStats.csv")

# Create initial columns with desired ratio (3:1:1)
col1, col2, col3 = st.columns([3, 1, 1])

# Create a container within the first column
with col1: 
  st.title("Indian Startups at a Glance")
  st.sidebar.header("Filter Options")
  top_states_slider = st.slider("Number of Top States", min_value=1, max_value=10, value=5)
  filter_by_select = st.selectbox(
      "Filter By", ["Startups", "Accelerators", "Incubators"])
  # Define a function to create the graph with filtering options
  def create_state_distribution(data, filter_by, top_value):
    filtered_data = data.nlargest(top_value, filter_by)  # Filter top states
    fig = px.bar(filtered_data, x="State", y=filter_by, title=f"Top {top_value} States by {filter_by.capitalize()}")
    return fig
  startup_graph = create_state_distribution(data.copy(), "Startups", top_states_slider)
  accelerator_graph = create_state_distribution(data.copy(), "Accelerators", top_states_slider)
  incubator_graph = create_state_distribution(data.copy(), "Incubators", top_states_slider)
    
  st.header("Distribution of Startups Across States")
  st.subheader("Startups")
  st.plotly_chart(startup_graph)
  st.subheader("Accelerators")
  st.plotly_chart(accelerator_graph)
  st.subheader("Incubators")
  st.plotly_chart(incubator_graph)

# Add content to columns and nested columns
with col2:
  st.write("Content in Column 2")

with col3:
  st.write("Content in Column 3")
