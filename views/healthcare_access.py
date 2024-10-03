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
# Sidebar changes
with st.sidebar:
    st.header("Filters")

    gender_filter = st.multiselect(
        "Please select Sex",
        options=df["What is your sex?"].unique(),
        default=df["What is your sex?"].unique(),
    )

    age_filter = st.multiselect(
        "Please select Age Group",
        options=df["Age_grp"].unique(),
        default=df["Age_grp"].unique(),
    )

    nationality_filter = st.multiselect(
        "Please select Nationality",
        options=df["What is your citizenship?"].unique(),
        default=df["What is your citizenship?"].unique(),
    )

    legal_filter = st.multiselect(
        "Please select Legal Status",
        options=df[
            "What is your current status (e.g., refugee, asylum seeker, etc.)?"
        ].unique(),
        default=df[
            "What is your current status (e.g., refugee, asylum seeker, etc.)?"
        ].unique(),
    )

    ethnic_filter = st.multiselect(
        "Please select Ethnicity",
        options=df["Please specify what ethnic minority group"].unique(),
        default=df["Please specify what ethnic minority group"].unique(),
    )

    accomodation_filter = st.multiselect(
        "Please select Accommodation",
        options=df["Do you currently live in a city or a village?"].unique(),
        default=df["Do you currently live in a city or a village?"].unique(),
    )
    duration_stay_filter = st.multiselect(
        "Please select the duration of stay in Moldova",
        options=df["How long have you been in the Republic of Moldova?"].unique(),
        default=df["How long have you been in the Republic of Moldova?"].unique(),
    )
    st.markdown("---")
    st.header("Actions")
    button_col1, button_col2 = st.columns(2)
    with button_col1:
        refresh_button = st.button("Data Refresh")
    with button_col2:
        reset_button = st.button("Reset Filters")

    if refresh_button:
        load_data.clear()
        st.rerun()

    if reset_button:
        st.rerun()
    # Display total submissions after filters
    st.markdown(f"**Total Submissions: {len(df)}**")

# Filter query
df_query = (
    "`What is your sex?`.isin(@gender_filter) & "
    "`Age_grp`.isin(@age_filter) & "
    "`What is your citizenship?`.isin(@nationality_filter) & "
    "`What is your current status (e.g., refugee, asylum seeker, etc.)?`.isin(@legal_filter) & "
    "`Please specify what ethnic minority group`.isin(@ethnic_filter) & "
    "`Do you currently live in a city or a village?`.isin(@accomodation_filter) & "
    "`How long have you been in the Republic of Moldova?`.isin(@duration_stay_filter)"
)
df = df.query(df_query)
if df.empty:
    st.warning("No data available for the selected filters.")
    st.stop()

total_submissions = len(df)
average_value = round(
    df["How many members are in your household, including you?"].mean(), 1
)
max_value = df["How many members are in your household, including you?"].max()
kid_value = round(df["Of these, how many are children under 18?"].mean(), 1)
elderly_value = round(
    df["Of these, how many are senior citizens, aged over 60?"].mean(), 1
)
age_value = round(df["What is your age?"].mean(), 1)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"**Total Submissions:** {total_submissions}")
with col2:
    st.markdown(f"**Avg household size:** {average_value}")
with col3:
    st.markdown(f"**Max household size:** {max_value}")

col4, col5, col6 = st.columns(3)
with col4:
    st.markdown(f"**Avg # of children in a household:** {kid_value}")
with col5:
    st.markdown(f"**Avg # of elderly in a household:** {elderly_value}")
with col6:
    st.markdown(f"**Avg age:** {age_value}")

st.markdown("---")
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
