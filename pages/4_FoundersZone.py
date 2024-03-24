import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("StartupIndiaStats.csv")
df1 = pd.read_csv("unicorns100.csv")
# Create initial columns with desired ratio (3:1:1)
col1, col2 = st.columns((2))
# Create a container within the first column
with col1:
  top_states_slider = st.slider("Number of Top States", min_value=1, max_value=10, value=5)
with col2:
  filter_by_select = st.selectbox("Filter By", ["Startups", "Accelerators", "Incubators"])
  textbox_style = """
    <style>
        .textbox {
            background: rgba(255, 255, 255, 0.1);
            padding: 2px;
            border-radius: 15px;
            border: 1px solid rgba(255, 255, 255, 0.18);
            color: #076D90;
            text-align: center;
        }
        .textbox h3{
            font-size: 22px;
            font-weight: bold;
            margin: 0;
        }
    </style>
"""
  st.markdown(textbox_style, unsafe_allow_html=True)
  st.markdown(f"<div class='textbox'><h3>Revenue Growth is the key metric to focus for early stage startups<h3></div>", unsafe_allow_html=True)
def create_state_distribution(data, filter_by, top_value):
  filtered_data = data.nlargest(top_value, filter_by)  # Filter top states
  fig = px.bar(filtered_data, x="State", y=filter_by, title=f"Top {top_value} States by {filter_by.capitalize()}")
  #fig.update_traces(marker_color='gray')  # Set initial color
  max_value = filtered_data[filter_by].max()
  fig.update_yaxes(range=[0, max_value * 1.2])
  return fig
with col1: 
  selected_filter = filter_by_select
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

  sectors = ["Fintech", "Ecommerce", "Enterprisetech", "Media & Entertainment", "Edtech", "Traveltech", "Others"]
  soonicorns = [37, 18, 17, 7, 7, 7, 22]
  df2 = pd.DataFrame({"Sectors":sectors, "Soonicorns":soonicorns})
  pie_fig = px.pie(
    data_frame=df2,
    names='Sectors',
    values='Soonicorns',  # Use 'Soonicorns' for pie slice values
    hole=.4,  # Adjust the hole size for a donut chart (0 for regular pie)
    title='Soonicorn Distribution by Sector')

  pie_fig.update_layout(showlegend=False)
  st.plotly_chart(pie_fig)
  
st.text("Fintech is the most likely sector to generate Future Unicorns in India")
sectors = ["Upto 2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
no_of_unicorns = [4,3,3,2,1,10,7,12,45,22,2]
uni_fig = px.bar(x=sectors, y=no_of_unicorns)
st.plotly_chart(uni_fig)
st.text("Only 2 Unicorns were Minted in 2023, a decline by 91% from last year")
