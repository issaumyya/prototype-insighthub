import streamlit as st
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.header('I N S I G H T  H U B', divider='blue')
st.subheader('_Empowering_ enterpreneur landscape of :blue[India] :sunglasses:')
col1, col2, col3 = st.columns((3))
with col1:
    if st.button("Fellow Investor?"):
        st.switch_page("pages/2_InvestorZone.py")
with col2:
    if st.button("Fellow Founder?"):
        st.switch_page("pages/3_FoundersZone.py")
with col3:
    if st.button("Talk to Us!"):
        st.switch_page("pages/1_TalkToUs.py")

tab1, tab2, tab3 = st.tabs(["India                 ", "Global                 ", "About Us                 "])
with tab1:
    st.subheader("Latest News")
    business_emoji = "💸"
    government_emoji = "️🚨"
    startup_emoji = "📊"
    investment_emoji = "💰"
    technology_emoji = "🖥"
    news = [
        (business_emoji, "RateGain Founder Bhanu Chopra’s Family Members Offload 3% Stake"),
        (startup_emoji, "Startup Mahakumbh: Startups Supported By MeitY Startup Hub Showcase Their Innovations"),
        (business_emoji, "BillDesk’s FY23 Profit Dips 5%, Revenue Inches Closer To INR 3,000 Cr Mark"),
        (investment_emoji, "Sustainable Packaging Startup Bambrew Bags INR 60 Cr From Blume Ventures, Others"),
        (government_emoji, "There Are Chances Of Misuse Of AI Without Proper Training: PM Narendra Modi"),
        (business_emoji, "Keep Proceeds From Rights Issues In Escrow Account, Consider Extension Of Issue: NCLT To BYJU’S"),
        (government_emoji, "Startups Under I-T Dept Scanner, Get Tax Notices Over VC Funding"),
        (business_emoji, "Swiggy’s Reported $207 Mn In Losses Between Q1 & Q3 FY24"),
        (investment_emoji, "TAC Infosec IPO Day 2: Public Issue Oversubscribed 22.8X"),
        (business_emoji, "Mamaearth Forays Into Colour Cosmetics Space With ‘Staze’"),
        (investment_emoji, "L Catterton To Launch India-Focussed Consumer Fund"),
        (business_emoji, "PhonePe Enables UPI Payments For Indians In UAE"),
    ]
    news_html = [
        f'<div style="padding: 10px; border-radius: 5px; margin-bottom: 10px; background-color: #f0f0f0; box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1); transition: box-shadow 0.3s; cursor: pointer;" onmouseover="this.style.boxShadow=\'0px 4px 8px rgba(0, 0, 0, 0.2)\'" onmouseout="this.style.boxShadow=\'0px 2px 4px rgba(0, 0, 0, 0.1)\'">'
        f'<span style="font-size: 20px; margin-right: 10px;">{emoji}</span>'
        f'<span style="font-size: 16px;">{title}</span>'
        '</div>'
        for emoji, title in news
    ]
    news_html = "".join(news_html)
    st.markdown(news_html, unsafe_allow_html=True)
    #for emoji, title in news:
        #st.write(f"{emoji} {title}\n")
with tab2:
    st.header("Latest News")

with tab3:
    st.header("About InsightHub")

