import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
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

years = ["Q1-2020", "Q2-2020", "Q3-2020", "Q4-2020", "Q1-2021", "Q2-2021", "Q3-2021", "Q4-2021", "Q1-2022",
        "Q2-2022", "Q3-2022", "Q4-2022","Q1-2023", "Q2-2023", "Q3-2023", "Q4-2023 (Till Nov.)"]
funding_amount_raised = [4, 1, 3, 4, 4, 6, 17, 15, 12, 7, 3, 3, 2.9, 2.5, 1.7, 1.6]
no_of_deals = [212, 179, 278, 284, 308, 313, 465, 498, 506, 394, 334, 283, 229, 241, 221, 138]
col1, col2 = st.columns((2))
data = pd.DataFrame({"Timeline": years, "Funding Amount": funding_amount_raised, "Deal Count": no_of_deals})

# Create a figure with two y-axes
fig = go.Figure(make_subplots(specs=[[{"secondary_y": True}]]))

# Defining the two y-axes
fig.add_trace(go.Bar(
    x=data["Timeline"],
    y=data["Funding Amount"],
    name="Funding Amount ($ Bn)",
))

fig.add_trace(go.Scatter(
    x=data["Timeline"],
    y=data["Deal Count"],
    name="Deal Count",
    mode="lines",
    yaxis="y2"
))

fig.update_layout(
    title="Funding Trends in India (Quarterly)",
    xaxis_showgrid=False,  # Remove x-axis grid lines
    yaxis_showgrid=False,  # Remove y-axis grid lines
    xaxis_zeroline=False,  # Remove zero line for x-axis
    yaxis_zeroline=False
)

fig.update_layout(xaxis=dict(tickmode="linear"), bargap=0.1)
fig.update_layout(legend=dict(orientation="h", x=0, y=1.5))
with col1:
        st.plotly_chart(fig,use_container_width=True, height = 170)
        col11, col12 = st.columns((2))
        col11.metric("YoY Median Ticket Size of Funding", "Q4 2023","-35%")
        col12.metric("Total Funding in 2023", "$9 Bn")    

sector_name = ["Ecommerce", "Enterprisetech", "Fintech", "Deeptech", "Healthtech", "Cleantech", "Edtech", "Media & Entertainment", "Consumer Services", "Logistics"]
funding_amount_raised = [3.02, 2.6, 1.3, 0.86, 0.50, 0.39, 0.37, 0.28, 0.28, 0.23]
no_of_deals = [192, 157, 129, 61, 57, 57, 47, 44, 39, 32]
# Create a DataFrame from lists
data1 = pd.DataFrame({
    "Sector Name": sector_name,
    "Funding Amount ($ Bn)": funding_amount_raised,
    "Number of Deals": no_of_deals
})

# Filter selection for x-axis
x_axis_options = {"Funding Amount ($ Bn)": "Funding Amount ($ Bn)", "Number of Deals": "Number of Deals"}
with col1:
    selected_x_axis = st.selectbox("", options=list(x_axis_options.keys()), index=0)
selected_x_axis_value = x_axis_options[selected_x_axis]

# Create the bar graph
fig = px.bar(data1, y="Sector Name", x=selected_x_axis_value, title="Investment by Sector", color="Sector Name", barmode="group")

# Update layout for better readability (optional)
fig.update_traces(textposition="outside")  # Display data point values outside bars
fig.update_layout(showlegend=False)
fig.update_layout(
    title="",
    xaxis_showgrid=False,  # Remove x-axis grid lines
    yaxis_showgrid=False,  # Remove y-axis grid lines
    xaxis_zeroline=False,  # Remove zero line for x-axis
    yaxis_zeroline=False
)
with col1:
    st.plotly_chart(fig,use_container_width=True, height = 170)
yoy = ["2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
beng = [2.7, 3.4, 1.4, 7.2, 5.3, 5.7, 5.6, 22, 11, 4.2]
delhi = [1.6, 3.7, 2, 4, 4.5, 4.7, 3.7, 10, 5.5, 2.7]
mum = [0, 1.1, 1, 1, 1.1, 1.1, 1.2, 6.7, 3.9, 1.5]

# Create a DataFrame from the data
df3 = pd.DataFrame({
  "Year": yoy,
  "Bengaluru": beng,
  "Delhi": delhi,
  "Mumbai": mum
})

# Area chart with Plotly Express
fig1 = px.area(
  df3,
  x="Year",
  y=["Mumbai", "Delhi", "Bengaluru"],  # List of columns for area lines
  title="YoY Funding Trends",
  labels={"Year": "Year", "y": "Funding Amount"},  # Customize axis labels
)

# Display the chart (optional, for standalone usage)
with col2:
        st.plotly_chart(fig1,use_container_width=True, height = 170)
late_stage_data = pd.DataFrame({
  "sectors": ["Fintech", "Ecommerce", "Enterprisetech", "Cleantech", "Consumer Services", "Deeptech", "Others"],
  "funding_amount": [2.1, 1.3, 0.6, 0.6, 0.3, 0.1, 0.6]
})

growth_stage_data = pd.DataFrame({
  "sectors": ["Fintech", "Ecommerce", "Enterprisetech", "Deeptech", "Logistics", "Cleantech", "Others"],
  "funding_amount": [0.721, 0.543, 0.489, 0.209, 0.200, 0.190, 0.587]
})

seed_stage_data = pd.DataFrame({
  "sectors": ["Enterprisetech", "Fintech", "Ecommerce", "Cleantech", "Deeptech", "Media & Entertainment", "Others"],
  "funding_amount": [0.143, 0.139, 0.089, 0.057, 0.051, 0.046, 0.155]
})

selected_stage = None
with col2:
        selected_stage = st.radio("Select Funding Stage:", ["Late Stage", "Growth Stage", "Seed Stage"])

def get_top_sector(data):
  top_sector = data["sectors"].iloc[data["funding_amount"].idxmax()]
  return top_sector

# Display based on selected stage
if selected_stage is not None:
  # Select the appropriate data based on the chosen stage
  if selected_stage == "Late Stage":
    data = late_stage_data.copy()  # Avoid modifying original DataFrame
  elif selected_stage == "Growth Stage":
    data = growth_stage_data.copy()
  else:
    data = seed_stage_data.copy()

  # Pie chart
  fig = px.pie(data, values="funding_amount", names="sectors", title=f"{selected_stage} Investment Distribution")
  with col2:
          st.plotly_chart(fig)

  # Top sector text
  top_sector = get_top_sector(data.copy())
col2.metric("Top Sector in", selected_stage, top_sector)


