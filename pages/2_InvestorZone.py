import pandas as pd
import streamlit as st
from plotly.express import px

# Load data
df1 = pd.read_csv("unicorns100.csv")

data["Funding Stage"] = pd.cut(data["Total Funding"], bins=[0, 10, 50, 100, float("inf")], labels=["Seed", "Series A", "Series B+", "Late Stage"])

# Sidebar filters
sector_filter = st.sidebar.selectbox("Filter by Sector", data["Sector"].unique())
funding_range = st.sidebar.slider(
    "Total Funding Range (USD Billion)", min_value=0, max_value=data["Total Funding"].max()
)
min_years_unicorn = st.sidebar.slider("Minimum Years to Unicorn", min_value=0, max_value=data.get("Years to Unicorn", 0).max())
min_valuation = st.sidebar.slider("Minimum Valuation (USD Billion)", min_value=0, max_value=data["Valuation"].max())
stage_filter = st.sidebar.selectbox("Funding Stage", data["Funding Stage"].unique())

filtered_data = data[
    (data["Sector"] == sector_filter) &
    (data["Total Funding"] <= funding_range[1]) &
    (data["Total Funding"] >= funding_range[0]) &
    (data.get("Years to Unicorn", data["Years to Unicorn"].max()) <= min_years_unicorn) &
    (data["Valuation"] >= min_valuation) &
    (data["Funding Stage"] == stage_filter)
]

st.title("Identifying Promising Startups")
st.write(f"Total Companies Found: {len(filtered_data)}")


if "Growth Rate" in data.columns:
    st.subheader("High Growth Potential")
    high_growth = filtered_data[filtered_data["Growth Rate"] > 0.5]  # Example threshold
    fig = px.bar(high_growth, x="Sector", y="Growth Rate", title="High Growth Startups by Sector")
    st.plotly_chart(fig)


