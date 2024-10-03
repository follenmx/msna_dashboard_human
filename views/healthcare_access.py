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

st.header("Healthcare Access")

# needed_to_access_healthcare
needed_to_access_healthcare = create_sex_distribution_pie_chart(
    df,
    "Since arriving in Moldova, have you or any member of your household needed to access healthcare services or medications?",
    "Since arriving in Moldova, have you or any member of your household needed to access healthcare services or medications?",
)
st.plotly_chart(needed_to_access_healthcare)

# services_needed_bar_chart
services_list1 = [
    "Pharmacy services / medication",
    "Vaccinations",
    "Specialist consultations (e.g., cardiology, neurology)",
    "Laboratory tests or diagnostic imaging (e.g., X-rays, MRI)",
    "Chronic disease management (e.g., diabetes, hypertension)",
    "Emergency care",
    "General medical check-up",
    "Pediatric care",
    "Dental care",
    "Mental health services",
    "Reproductive health services",
    "Maternity and prenatal care",
    "COVID-19 related services",
    "Physical therapy or rehabilitation",
    "Prefer not to say",
    "Other (please specify)",
]
services_needed_bar_chart = create_mbar_chart(
    df,
    "What types of medical services did you need?",
    services_list1,
    "What types of medical services did you need?",
)
st.plotly_chart(services_needed_bar_chart)

st.markdown("---")
# able_to_access_healthservice_need_pie_chart_fig

able_to_access_healthservice_need_pie_chart_fig = create_sex_distribution_pie_chart(
    df,
    "Were you able to access the healthcare service you needed?",
    "Were you able to access the healthcare service you needed?",
)
st.plotly_chart(able_to_access_healthservice_need_pie_chart_fig)
st.markdown("---")

# coverage1_bar_chart
coverage_options1 = [
    "Covered by government either through insurance or temporary protection status",
    "Partially covered, with out-of-pocket payments required",
    "Entirely covered by private healthcare / out-of-pocket payment",
    "Covered by an NGO or non-profit organization",
    "Prefer not to say",
    "Other (please specify)",
]
coverage1_bar_chart = create_mbar_chart(
    df,
    "How did you pay for the service?",
    coverage_options1,
    "How did you pay for the service?",
)
st.plotly_chart(coverage1_bar_chart)

# rate_the_quality_of_treatment

rate_the_quality_of_treatment = create_bar_chart(
    df,
    "How would you rate the quality of treatment received?",
    "How would you rate the quality of treatment received?",
)
st.plotly_chart(rate_the_quality_of_treatment)

st.markdown("---")

# service_barriers1_bar_chart

service_barriers1 = [
    "Discrimination",
    "Long waiting times",
    "Lack of information about available services",
    "Lack of necessary documentation",
    "Lack of specialized services",
    "Transportation issues",
    "Cost of services",
    "Language barriers",
    "Prefer not to say",
    "Other (please specify)",
]
service_barriers1_bar_chart = create_mbar_chart(
    df,
    "What prevented you from receiving the service?",
    service_barriers1,
    "What prevented you from receiving the service?",
)
st.plotly_chart(service_barriers1_bar_chart)

st.markdown("---")

# Access Preventive Health Services
access_preventive_options = [
    "No difficulties",
    "Limited availability",
    "Lack of information",
    "High costs",
    "Long wait times",
    "Prefer not to say",
    "Other",
]
access_preventive_bar_chart = create_mbar_chart(
    df,
    "Preventive health services (e.g., vaccinations, health screenings)?",
    access_preventive_options,
    "Difficulties in Accessing Preventive Health Services",
)
st.plotly_chart(access_preventive_bar_chart)

# Access Reproductive Health Services
access_reproductive_options = [
    "No difficulties",
    "Limited availability",
    "Lack of specialists",
    "Cultural barriers",
    "High costs",
    "Prefer not to say",
    "Other",
]
access_reproductive_bar_chart = create_mbar_chart(
    df,
    "Reproductive health services and or pre and postnatal care?",
    access_reproductive_options,
    "Difficulties in Accessing Reproductive Health Services",
)
st.plotly_chart(access_reproductive_bar_chart)

# Access Necessary Medications
access_medicine_options = [
    "No difficulties",
    "Unavailable medications",
    "High costs",
    "Prescription issues",
    "Language barriers in understanding instructions",
    "Prefer not to say",
    "Other",
]
access_medicine_bar_chart = create_mbar_chart(
    df,
    "Necessary medications?",
    access_medicine_options,
    "Difficulties in Accessing Necessary Medications",
)
st.plotly_chart(access_medicine_bar_chart)

# How Medications are Procured
procure_medicine_pie_chart = create_sex_distribution_pie_chart(
    df,
    "How do you usually obtain the medications you need in Moldova?",
    "How do you usually obtain the medications you need in Moldova?",
)
st.plotly_chart(procure_medicine_pie_chart)
