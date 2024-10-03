import pandas as pd
import streamlit as st
from templates.chart_templates import *

sheet_id = st.secrets["data_link"]
csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"


@st.cache_data
def load_data():
    df = pd.read_csv(csv_url)
    return df


df = load_data()

st.header("Overall Assessment and Feedback")

# Biggest Gaps in Healthcare Services
healthcare_gaps_options = [
    "Administrative barriers and bureaucracy",
    "Lack of family doctors in the area",
    "Lack of specialized doctors in the area",
    "Lack of laboratories or diagnostic imaging services",
    "No preventive care being offered",
    "Prefer not to say",
    "Other (please specify)",
]
healthcare_gaps_bar_chart = create_mbar_chart(
    df,
    "In your opinion, what are the biggest gaps in the provision of healthcare services in Moldova?",
    healthcare_gaps_options,
    "Biggest Gaps in Healthcare Services",
)
st.plotly_chart(healthcare_gaps_bar_chart)

# Satisfaction with Medical System
grade_social_healthcare_pie_chart = create_sex_distribution_pie_chart(
    df,
    "How satisfied are you in general with the medical system in Moldova?",
    "Satisfaction with Medical System",
)
st.plotly_chart(grade_social_healthcare_pie_chart)
