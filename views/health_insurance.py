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

st.header("Health Insurance and Informations")

# Health Insurance Coverage
have_coverage_pie_chart = create_sex_distribution_pie_chart(
    df,
    "Do you have any form of health insurance coverage in Moldova?",
    "Health Insurance Coverage",
)
st.plotly_chart(have_coverage_pie_chart)

# Impact of No Health Insurance
not_coverage_pie_chart = create_sex_distribution_pie_chart(
    df,
    "If not, has this affected your ability to access health services?",
    "If not, has this affected your ability to access health services?",
)
st.plotly_chart(not_coverage_pie_chart)

st.markdown("---")

# Sources of Health-Related Information
info_sources_options = [
    "Friends and relatives",
    "Internet/Mass Media",
    "Family doctor",
    "Prefer not to say",
    "Other (please specify)",
]
info_sources_bar_chart = create_mbar_chart(
    df,
    "Where do you typically get health-related information?",
    info_sources_options,
    "Sources of Health-Related Information",
)
st.plotly_chart(info_sources_bar_chart)

# Reliability of Health Information Sources
reliable_sources_pie_chart = create_sex_distribution_pie_chart(
    df,
    "Do you feel that you receive health information from accurate and reliable sources?",
    "Reliability of Health Information Sources",
)
st.plotly_chart(reliable_sources_pie_chart)

# Desired Health Information Topics
what_subjects_options = [
    "How to care for the health of older citizens",
    "How to care for the health of children",
    "Information on prevention and treatment of sexually transmitted diseases",
    "Information on prevention of chronic diseases",
    "Information on vaccination and access to vaccines",
    "How to care for family members with chronic diseases",
    "Myths and realities regarding health",
    "How to select adequate health sources",
    "Prefer not to say",
    "None of the above",
]
what_subjects_bar_chart = create_mbar_chart(
    df,
    "What health topics would you like to receive more information about?",
    what_subjects_options,
    "Desired Health Information Topics",
)
st.plotly_chart(what_subjects_bar_chart)
