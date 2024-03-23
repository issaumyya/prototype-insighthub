import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("StartupIndiaStats.csv")
df1 = pd.read_csv("unicorns100.csv")
# Create initial columns with desired ratio (3:1:1)
col1, col2 = st.columns([1,1])
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
with col1:
  if selected_filter == "Startups":
    startup_graph = create_state_distribution(data.copy(), "Startups", top_states_slider)
    st.plotly_chart(startup_graph)
  elif selected_filter == "Accelerators":
    accelerator_graph = create_state_distribution(data.copy(), "Accelerators", top_states_slider)
    st.plotly_chart(accelerator_graph)
  elif selected_filter == "Incubators":
    incubator_graph = create_state_distribution(data.copy(), "Incubators", top_states_slider)
    st.plotly_chart(incubator_graph)
  else:
    st.write("Please select a filter from the sidebar.")

with col2:
  startup_counts = df1['Founded In'].value_counts().reset_index()
  startup_counts.columns = ['Founded In', 'Number of Startups']
  fig = px.line(startup_counts, x='Founded In', y='Number of Startups',
             labels={'Founded In': 'Year Founded', 'Number of Startups': 'Number of Startups'},
             title='Number of Unicorns Founded Each Year')
