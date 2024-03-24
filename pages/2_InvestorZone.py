import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

years = ["2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]
funding_amount_raised = [5.4, 9.3, 5.6, 13, 11.9, 12, 12, 42, 25]
no_of_deals = [378, 985, 1049, 999, 833, 810, 953, 1584, 1519]

# Create a figure with two y-axes
fig = go.FigureWidget(make_subplots(specs=[[{"secondary_y": True}]]))

# Defining the two y-axes
fig.add_trace(go.Bar(
    x=years,
    y=funding_amount_raised,
    name="Funding Amount ($ Bn)",
))

fig.add_trace(go.Scatter(
    x=years,
    y=no_of_deals,
    name="Deal Count",
    mode="lines",
    yaxis="y2"
))

fig.update_layout(
    title="Double Axis Graph (Bar & Line)",
    xaxis_title="Years",
    yaxis_title="Funding Amount ($ Bn)",
    yaxis2_title="Deal Count",
)

fig.update_layout(xaxis=dict(tickmode="linear"), bargap=0.1)

fig.show()
