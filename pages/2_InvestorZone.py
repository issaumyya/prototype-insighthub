import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

years = ["Q1-2020", "Q2-2020", "Q3-2020", "Q4-2020", "Q1-2021", "Q2-2021", "Q3-2021", "Q4-2021", "Q1-2022",
        "Q2-2022", "Q3-2022", "Q4-2022","Q1-2023", "Q2-2023", "Q3-2023", "Q4-2023 (Till Nov.)"]
funding_amount_raised = [4, 1, 3, 4, 4, 6, 17, 15, 12, 7, 3, 3, 2.9, 2.5, 1.7, 1.6]
no_of_deals = [212, 179, 278, 284, 308, 313, 465, 498, 506, 394, 334, 283, 229, 241, 221, 138]

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
    title="Double Axis Graph (Bar & Line)",
    xaxis_title="Timeline",
    yaxis_title="Funding Amount ($ Bn)",
    yaxis2_title="Deal Count",
    xaxis_showgrid=False,  # Remove x-axis grid lines
    yaxis_showgrid=False,  # Remove y-axis grid lines
    xaxis_zeroline=False,  # Remove zero line for x-axis
    yaxis_zeroline=False
)

fig.update_layout(xaxis=dict(tickmode="linear"), bargap=0.1)
st.plotly_chart(fig)
