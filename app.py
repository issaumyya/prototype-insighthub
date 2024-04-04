import streamlit as st
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.header('I N S I G H T  H U B', divider='blue')
st.subheader('_Empowering_ Entrepreneurial Landscape of :blue[India]')
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
business_emoji = "💸"
government_emoji = "️🚨"
startup_emoji = "📊"
investment_emoji = "💰"
technology_emoji = "🖥"

tab1, tab2, tab3 = st.tabs(["India                 ", "Global                 ", "About Us                 "])
with tab1:
    st.subheader("Latest News")

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
        f'<div style="padding: 10px; border-radius: 5px; margin-bottom: 10px; border: 1px solid #ddd; transition: box-shadow 0.3s; cursor: pointer;" onmouseover="this.style.boxShadow=\'0px 4px 8px rgba(0, 0, 0, 0.2)\'" onmouseout="this.style.boxShadow=\'none\'">'
        f'<span style="font-size: 20px; margin-right: 10px;">{emoji}</span>'
        f'<span style="font-size: 16px;">{title}</span>'
        '</div>'
        for emoji, title in news
    ]
    news_html = "".join(news_html)
    st.markdown(news_html, unsafe_allow_html=True)
with tab2:
    st.subheader("Latest News")
    global_news = [
        (technology_emoji, "Databricks’ GPT rival and who’s investing in “underdog” founders"),
        (startup_emoji, "The final countdown: Early Stage 2024 ticket savings end tonight"),
        (business_emoji, "Byju’s founder floats share offer to make peace with estranged investors"),
        (investment_emoji, "Buy now, pay later on a Porsche? Zaver now has $30M to make it a reality"),
        (technology_emoji, "New AI-powered health tech startup revolutionizes patient care"),
        (business_emoji, "Electric vehicle startup announces plans for global expansion"),
        (government_emoji, "Food delivery startup partners with leading restaurants for innovative services"),
        (business_emoji, "Healthcare startup introduces groundbreaking medical device for early disease detection"),
        (investment_emoji, "Blockchain startup secures $50 million in Series A funding round"),
    ]

    news_html1 = [
        f'<div style="padding: 10px; border-radius: 5px; margin-bottom: 10px; border: 1px solid #ddd; transition: box-shadow 0.3s; cursor: pointer;" onmouseover="this.style.boxShadow=\'0px 4px 8px rgba(0, 0, 0, 0.2)\'" onmouseout="this.style.boxShadow=\'none\'">'
        f'<span style="font-size: 20px; margin-right: 10px;">{emoji}</span>'
        f'<span style="font-size: 16px;">{title}</span>'
        '</div>'
        for emoji, title in global_news
    ]
    news_html1 = "".join(news_html1)
    st.markdown(news_html1, unsafe_allow_html=True)

with tab3:
    st.header("About InsightHub")
    st.image('Copy Of DTI Final Presentation.png')

