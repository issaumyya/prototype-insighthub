import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("StartupIndiaStats.csv")

# Create initial columns with desired ratio (3:1:1)
col1, col2, col3 = st.columns([2, 1, 1])
st.title("Indian Startups at a Glance")
# Create a container within the first column
with col1: 
  def create_state_distribution(data, filter_by, top_value):
    filtered_data = data.nlargest(top_value, filter_by)  # Filter top states
    fig = px.bar(filtered_data, x="State", y=filter_by, title=f"Top {top_value} States by {filter_by.capitalize()}")
    #fig.update_traces(marker_color='gray')  # Set initial color
    max_value = filtered_data[filter_by].max()
    #fig.update_traces(marker=dict(color=st.colors.green), selector=max(fig.data, key='y'))  # Highlight max
    fig.update_yaxes(range=[0, max_value * 1.2])
    return fig
    
  top_states_slider = st.sidebar.slider("Number of Top States", min_value=1, max_value=10, value=5)
  filter_by_select = st.sidebar.selectbox("Filter By", ["Startups", "Accelerators", "Incubators"])
  selected_filter = filter_by_select
  if selected_filter == "Startups":
    startup_graph = create_state_distribution(data.copy(), "Startups", top_states_slider)
    st.header("Distribution of Startups Across States")
    st.plotly_chart(startup_graph)
  elif selected_filter == "Accelerators":
    accelerator_graph = create_state_distribution(data.copy(), "Accelerators", top_states_slider)
    st.header("Distribution of Accelerators Across States")
    st.plotly_chart(accelerator_graph)
  elif selected_filter == "Incubators":
    incubator_graph = create_state_distribution(data.copy(), "Incubators", top_states_slider)
    st.header("Distribution of Incubators Across States")
    st.plotly_chart(incubator_graph)
  else:
    st.write("Please select a filter from the sidebar.")

# Add content to columns and nested columns
with col2:
  st.write("Content in Column 2")

with col3:
  st.write("Content in Column 3")
