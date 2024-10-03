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

st.header("MHPSS Information")

# Accessed MHPSS Services
mhpss_used_options = [
    "No",
    "Individual counseling sessions",
    "Group therapy or support groups",
    "Stress reduction and relaxation techniques",
    "Cultural adaptation and integration support",
    "Community-building activities and social events",
    "Educational workshops on mental health and well-being",
    "Crisis hotline or emergency mental health services",
    "Family counseling",
    "I don't know/Not sure",
    "Prefer not to say",
    "Other (please specify)",
]
mhpss_used_bar_chart = create_mbar_chart(
    df,
    "Have you or members of your household, accessed any mental health or psychosocial support services in Moldova?",
    mhpss_used_options,
    "Accessed MHPSS Services",
)
st.plotly_chart(mhpss_used_bar_chart)
# MHPSS Providers
mhpss_provider_options = [
    "Government health services",
    "International NGO",
    "Local NGO",
    "Private practitioner",
    "Remote services from Ukraine",
    "Religious organization",
    "Prefer not to say",
    "Other (please specify)",
]
mhpss_provider_bar_chart = create_mbar_chart(
    df,
    "From which source did you or your family members receive mental health and psychosocial support services?",
    mhpss_provider_options,
    "MHPSS Providers",
)
st.plotly_chart(mhpss_provider_bar_chart)
# Satisfaction with MHPSS Services
mhpss_quality_pie_chart = create_sex_distribution_pie_chart(
    df,
    "Are you satisfied with the quality of services received?",
    "Satisfaction with MHPSS Services",
)
st.plotly_chart(mhpss_quality_pie_chart)
# Helpful MHPSS Services
mhpss_helpful_options = [
    "Individual counseling sessions",
    "Group therapy or support groups",
    "Stress reduction and relaxation techniques",
    "Cultural adaptation and integration support",
    "Community-building activities and social events",
    "Educational workshops on mental health and well-being",
    "Crisis hotline or emergency mental health services",
    "Family counseling",
    "Prefer not to say",
    "Other",
]
mhpss_helpful_bar_chart = create_mbar_chart(
    df,
    "What type of psychosocial support do you think might be most helpful for the refugee community?",
    mhpss_helpful_options,
    "Most Helpful type of MHPSS Services",
)
st.plotly_chart(mhpss_helpful_bar_chart)
