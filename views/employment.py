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

st.header("Employment")

# Attempted to Find Employment
seek_employment_pie_chart = create_sex_distribution_pie_chart(
    df,
    "Have you attempted to find employment in Moldova?",
    "Have you attempted to find employment in Moldova?",
)
st.plotly_chart(seek_employment_pie_chart)

# Secured Employment
secure_employment_pie_chart = create_sex_distribution_pie_chart(
    df,
    "Were you able to secure employment?",
    "Were you able to secure employment?",
)
st.plotly_chart(secure_employment_pie_chart)

# Job Challenges Faced
job_challenge_options = [
    "No difficulties",
    "Language barriers",
    "Lack of recognition of qualifications or work experience",
    "Discrimination or prejudice from employers",
    "Lack of professional networks or connections",
    "Difficulty obtaining necessary work permits or documentation",
    "Cultural differences in workplace norms and expectations",
    "Prefer not to say",
    "Other (please specify)",
]
job_challenge_bar_chart = create_mbar_chart(
    df,
    "What challenges have you faced / are you facing in accessing the job market?",
    job_challenge_options,
    "Job Challenges Faced",
)
st.plotly_chart(job_challenge_bar_chart)
# Planning to Seek Employment
seek_employment_future_pie_chart = create_sex_distribution_pie_chart(
    df,
    "Are you planning to look for job in the coming months?",
    "Are you planning to look for job in the coming months?",
)
st.plotly_chart(seek_employment_future_pie_chart)

# Support Needed for Employment
job_support_options = [
    "Language training specific to job-related terminology",
    "Vocational training or skill development programs",
    "Job search workshops (resume writing, interview skills)",
    "Job placement services or employment agencies",
    "Assistance with credential recognition and skill certification",
    "Entrepreneurship support and small business development programs",
    "Prefer not to say",
    "Other (please specify)",
]
job_support_bar_chart = create_mbar_chart(
    df,
    "What type of support do you think would be helpful for refugees in securing employment?",
    job_support_options,
    "Support Needed for Employment",
)
st.plotly_chart(job_support_bar_chart)
