import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("StartupIndiaStats.csv")
df1 = pd.read_csv("unicorns100.csv")
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
# Create initial columns with desired ratio (3:1:1)
col1, col2 = st.columns((2))
# Create a container within the first column
with col2:
     col21, col22 = st.columns((2))
     with col21:
         filter_by_select = st.selectbox("Filter By", ["Startups", "Accelerators", "Incubators"])
     with col22:
         top_states_slider = st.slider("Number of Top States", min_value=1, max_value=10, value=5)
def create_state_distribution(data, filter_by, top_value):
  filtered_data = data.nlargest(top_value, filter_by)  # Filter top states
  fig = px.bar(filtered_data, x="State", y=filter_by, title=f"Top {top_value} States by {filter_by.capitalize()}")
  #fig.update_traces(marker_color='gray')  # Set initial color
  max_value = filtered_data[filter_by].max()
  fig.update_yaxes(range=[0, max_value * 1.2])
  return fig
selected_filter = filter_by_select

with col1, col2:
    if selected_filter == "Startups":
        startup_graph = create_state_distribution(data.copy(), "Startups", top_states_slider)
        st.plotly_chart(startup_graph,use_container_width=True, height = 170)
    elif selected_filter == "Accelerators":
        accelerator_graph = create_state_distribution(data.copy(), "Accelerators", top_states_slider)
        st.plotly_chart(accelerator_graph,use_container_width=True, height = 170)
    elif selected_filter == "Incubators":
        incubator_graph = create_state_distribution(data.copy(), "Incubators", top_states_slider)
        st.plotly_chart(incubator_graph,use_container_width=True, height = 170)
    else:
        st.write("Please select a filter from the sidebar.")
    col2.metric("Key Metric for Early Stage Startups is", "Revenue Growth")


with col1:
  st.markdown(textbox_style, unsafe_allow_html=True)
  st.markdown(f"<div class='textbox'><h3>India is the 3rd Largest Startup Ecosystem in the world, with 112 in the Unicorn Club!<h3></div>", unsafe_allow_html=True)
  sectors = ["Fintech", "Ecommerce", "Enterprisetech", "Media & Entertainment", "Edtech", "Traveltech", "Others"]
  soonicorns = [37, 18, 17, 7, 7, 7, 22]
  df2 = pd.DataFrame({"Sectors":sectors, "Soonicorns":soonicorns})
  pie_fig = px.pie(
    data_frame=df2,
    names='Sectors',
    values='Soonicorns',  # Use 'Soonicorns' for pie slice values
    hole=.4,  # Adjust the hole size for a donut chart (0 for regular pie)
    title='Soonicorn Distribution by Sector')

  #pie_fig.update_layout(showlegend=True)
  st.plotly_chart(pie_fig,use_container_width=True, height = 100)
  col1.metric("Most likely sector to generate future unicorns in India", "Fintech")

import plotly.graph_objects as go

fig2 = go.Figure(go.Waterfall(
    measure = ["relative", "relative", "relative", "relative", "relative", "relative","relative","relative","relative","relative"],
    x = ["2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"],
    y = [363, 649, 265, -85, -199, -101, 222, 1373, -71, -859],
    connector = {"line":{"color":"rgb(63, 63, 63)"}},
))

fig2.update_layout(
        title = "Number of Investors Backing Indian Startups",
        showlegend = False
)

data1 = {
        'Sector': [
            'Fintech', 'Fintech', 'Fintech', 'Fintech', 'Fintech', 'Fintech',
            'Ecommerce', 'Ecommerce', 'Ecommerce', 'Ecommerce',
            'Edtech', 'Edtech', 'Edtech', 'Edtech', 'Edtech', 'Edtech',
            'Deeptech', 'Deeptech', 'Deeptech', 'Deeptech', 'Deeptech'
        ],
        'Subsector': [
            'Lending Tech', 'Banking', 'Fintech SaaS', 'Insurtech', 'Investment Tech', 'Others',
            'D2C', 'B2B', 'B2C', 'Others',
            'Skill Development', 'Test Prep', 'Online Discovery', 'Online Certification', 'Edtech SaaS', 'Others',
            'RPA', 'Spacetech', 'Hardware & IoT', 'Dronetech', 'Others'
        ],
        'Value': [
            1185, 971, 348, 314, 107, 96,
            1415, 448, 682, 91,
            72, 64, 55, 45, 43, 5,
            147, 124, 123, 29, 9
        ]
    }
df4 = pd.DataFrame(data1)
fig3 = px.treemap(
    df4,
    path=[df4['Sector'], df4['Subsector']],  # Path for hierarchical levels (Sector, Subsector)
    values='Value',  
    color='Sector', 
    title='Funding Amount (in Mn) by Sector')
with col1,col2:
    st.plotly_chart(fig3, use_container_width=True, height = 350)
with col1:
    st.plotly_chart(fig2,use_container_width=True, height = 150)
