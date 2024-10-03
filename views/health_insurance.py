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
