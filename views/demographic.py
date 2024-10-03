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

st.header("Demographic Information")
# Age and Sex Distribution
age_histogram_fig = create_histogram(df, "What is your age?", "Age Distribution")
st.plotly_chart(age_histogram_fig)

age_pie_chart_fig = create_sex_distribution_pie_chart(df, "Age_grp", "Age Distribution")
st.plotly_chart(age_pie_chart_fig)

sex_pie_chart_fig = create_sex_distribution_pie_chart(
    df, "What is your sex?", "Sex Distribution"
)
st.plotly_chart(sex_pie_chart_fig)

# Nationality Distribution (Select Multiple)
nationality_options = ["Ukraine", "Moldova", "Romania", "Prefer not to say", "Other"]
nationality_bar_chart = create_mbar_chart(
    df, "What is your citizenship?", nationality_options, "Citizenship Distribution"
)
st.plotly_chart(nationality_bar_chart)

# Ethnicity Distribution
ethnicity_pie_chart_fig = create_sex_distribution_pie_chart(
    df,
    "Please specify what ethnic minority group",
    "Ethnicity Distribution",
)
st.plotly_chart(ethnicity_pie_chart_fig)

# Legal Status

legalstatus_pie_chart_fig = create_sex_distribution_pie_chart(
    df,
    "What is your current status (e.g., refugee, asylum seeker, etc.)?",
    "Legal Status (Self Assessed)",
)
st.plotly_chart(legalstatus_pie_chart_fig)

# Obstacles from TP

obstaclestp_options = options = [
    "Long waiting times or bureaucratic delays",
    "Lack of information about the process",
    "Uncertainty about length of stay in Moldova",
    "Fear of impact on future return to Ukraine",
    "Difficulty gathering required documents",
    "Language barriers in completing the application",
    "Prefer not to say",
    "Other",
]
obstaclestp_bar_chart = create_mbar_chart(
    df,
    "What obstacles are preventing you from pursuing temporary protection status?",
    obstaclestp_options,
    "What obstacles are preventing you from pursuing temporary protection status?",
)
st.plotly_chart(obstaclestp_bar_chart)
