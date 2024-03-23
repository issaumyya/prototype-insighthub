import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# Load data
df1 = pd.read_csv("unicorns100.csv")
df1['Years to Unicorn'] = pd.to_numeric(df1['Years to Unicorn'].str.replace('years', '').str.replace('Years', ''), errors='coerce')
df1['Valuation'] = df1['Valuation'].str.replace('$', '').str.replace('+', '').str.replace('<', '').str.replace('Less than', '')
df1['Val_num'] = df1['Valuation'].str.replace('Mn', '').str.replace('Bn', '')
df1['Val_num'] = pd.to_numeric(df1['Val_num'], errors='coerce')

df1.loc[df1['Valuation'].notnull() & df1['Valuation'].astype(str).str.endswith('Mn'), 'Val_num'] *= 1000000
df1.loc[df1['Valuation'].notnull() & df1['Valuation'].astype(str).str.endswith('Bn'), 'Val_num'] *= 100000000

df1['Total Funding'] = df1['Total Funding'].str.replace('$', '').str.replace('+', '').str.replace('<', '').str.replace('Less than', '')

df1['Funding_num'] = df1['Total Funding'].str.replace('Mn', '').str.replace('Bn', '')
df1['Funding_num'] = pd.to_numeric(df1['Funding_num'], errors='coerce')

df1.loc[df1['Total Funding'].notnull() & df1['Total Funding'].astype(str).str.endswith('Mn'), 'Funding_num'] *= 1000000
df1.loc[df1['Total Funding'].notnull() & df1['Total Funding'].astype(str).str.endswith('Bn'), 'Funding_num'] *= 100000000
if not pd.api.types.is_numeric_dtype(df1["Funding_num"]):
    df1["Funding_num"] = pd.to_numeric(df1["Funding_num"], errors='coerce') 
                                       
df1["Funding Stage"] = pd.cut(df1["Funding_num"], bins=[0, 10, 50, 100, float("inf")], labels=["Seed", "Series A", "Series B+", "Late Stage"])
sector_filter = st.sidebar.selectbox("Filter by Sector", df1["Sector"].unique())
funding_range = st.sidebar.slider("Total Funding Range", min_value=0, max_value=df1["Funding_num"].max(), value=max_value=df1["Funding_num"].median())
min_years_unicorn = st.sidebar.slider("Minimum Years to Unicorn", min_value=0, max_value=df1.get("Years to Unicorn", 0).max(), value = df1.get("Years to Unicorn", 0).median())
min_valuation = st.sidebar.slider("Minimum Valuation (USD Billion)", min_value=0, max_value=df1["Val_num"].max(), value = df1["Val_num"].median())
stage_filter = st.sidebar.selectbox("Funding Stage", df1["Funding Stage"].unique())

filtered_data = df1[
    (df1["Sector"] == sector_filter) &
    (df1["Funding_num"] <= funding_range[1]) &
    (df1["Funding_num"] >= funding_range[0]) &
    (df1.get("Years to Unicorn", data["Years to Unicorn"].max()) <= min_years_unicorn) &
    (data["Val_num"] >= min_valuation) &
    (data["Funding Stage"] == stage_filter)
]

st.title("Identifying Promising Startups")
st.write(f"Total Companies Found: {len(filtered_data)}")


if "Growth Rate" in data.columns:
    st.subheader("High Growth Potential")
    high_growth = filtered_data[filtered_data["Growth Rate"] > 0.5]  # Example threshold
    fig = px.bar(high_growth, x="Sector", y="Growth Rate", title="High Growth Startups by Sector")
    st.plotly_chart(fig)


