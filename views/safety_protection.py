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

st.header("Safety and Protection")

# Safety and Security Concerns
safety_concern_options = [
    "None",
    "Physical threats or violence",
    "Verbal harassment or intimidation",
    "Theft or robbery",
    "Unsafe living conditions",
    "Limited access to health services",
    "Prefer not to say",
    "Other (please specify)",
]
safety_concern_bar_chart = create_mbar_chart(
    df,
    "Have you or members of your household faced any safety and security concerns since arriving in Moldova?",
    safety_concern_options,
    "Safety and Security Concerns",
)
st.plotly_chart(safety_concern_bar_chart)

# Support Systems for Safety Concerns
safety_support_options = [
    "Police",
    "Local authorities",
    "NGOs or humanitarian organizations",
    "Community leaders",
    "Friends or family",
    "Refugee support center",
    "Prefer not to say",
    "Other (please specify)",
]
safety_support_bar_chart = create_mbar_chart(
    df,
    "Where would you go to seek support in case of safety concerns? (Select all that apply)",
    safety_support_options,
    "Support Systems for Safety Concerns",
)
st.plotly_chart(safety_support_bar_chart)

# Experience of Discrimination
discrimination_pie_chart = create_sex_distribution_pie_chart(
    df,
    "During your stay in Moldova, have you or your family members experienced any forms of discrimination?",
    "Experience of Discrimination",
)
st.plotly_chart(discrimination_pie_chart)

# Most Vulnerable Groups
most_vulnerable_options = [
    "Children (under 18)",
    "Elderly (over 60)",
    "People with disabilities",
    "Single parents/caregivers",
    "Unaccompanied minors",
    "Ethnic or religious minorities",
    "Survivors of violence or torture",
    "People with chronic illnesses (physical or mental)",
    "Women and girls",
    "Persons dealing with substance abuse",
    "LGBTQ+ individuals",
    "Prefer not to say",
    "Other (please specify)",
]
most_vulnerable_bar_chart = create_mbar_chart(
    df,
    "In your opinion, which groups among refugees are the most vulnerable?",
    most_vulnerable_options,
    "Most Vulnerable Groups",
)
st.plotly_chart(most_vulnerable_bar_chart)
# Main Protection Risks for Women
women_challenge_options = [
    "Limited access to employment opportunities",
    "Balancing childcare responsibilities with work or education",
    "Gender-based violence or harassment",
    "Limited access to healthcare, including reproductive health services",
    "Social isolation and lack of community support",
    "Difficulties in accessing education or skill development programs",
    "Prefer not to say",
    "Other (please specify)",
]
women_challenge_bar_chart = create_mbar_chart(
    df,
    "What do you think are the main protection risks that refugee women face?",
    women_challenge_options,
    "Main Protection Risks for Women",
)
st.plotly_chart(women_challenge_bar_chart)
# Main Protection Risks for Men
men_challenge_options = [
    "Finding employment opportunities",
    "Accessing healthcare services",
    "Coping with psychological stress and trauma",
    "Legal issues (documentation, residency permits, etc.)",
    "Language barriers",
    "Separation from family members",
    "Prefer not to say",
    "Other (please specify)",
]
men_challenge_bar_chart = create_mbar_chart(
    df,
    "What are the main protection risks that refugee men face?",
    men_challenge_options,
    "Main Protection Risks for Men",
)
st.plotly_chart(men_challenge_bar_chart)
# Main Challenges for Children
children_challenge_options = [
    "Disruption of education",
    "Psychological trauma and stress",
    "Difficulty integrating into a new environment",
    "Language barriers",
    "Health and nutrition issues",
    "Loss of sense of security and stability",
    "Prefer not to say",
    "Other",
]
children_challenge_bar_chart = create_mbar_chart(
    df,
    "What do you think is the main challenge that refugee children are facing?",
    children_challenge_options,
    "Main Challenges for Children",
)
st.plotly_chart(children_challenge_bar_chart)
# Usual Support System
support_system_options = [
    "Family",
    "Friends",
    "Community - online support groups",
    "Community - offline support groups",
    "Prefer not to say",
    "Other",
]
support_system_bar_chart = create_mbar_chart(
    df,
    "What is your usual suppport system, to whom do you refer when you are faced with hardships?",
    support_system_options,
    "Usual Support System",
)
st.plotly_chart(support_system_bar_chart)
# Awareness of Gender-Based Violence Cases
gbv_cases_pie_chart = create_sex_distribution_pie_chart(
    df,
    "Are you aware of any incidents of gender-based violence among refugees in your community in Moldova?",
    "Awareness of Gender-Based Violence Cases",
)
st.plotly_chart(gbv_cases_pie_chart)
# Knowledge of Support for GBV
gbv_what_do_options = [
    "Police",
    "Hotline",
    "Shelter for survivors",
    "No",
    "Prefer not to answer",
    "Other",
]
gbv_what_do_bar_chart = create_mbar_chart(
    df,
    "Do you know where could a woman or young girl go for help in case of violence?",
    gbv_what_do_options,
    "Knowledge of Support for GBV",
)
st.plotly_chart(gbv_what_do_bar_chart)
# Need More Information on GBV Services
more_info_gbv_options = [
    "Health",
    "Shelter",
    "Psychological support",
    "Legal assistance",
    "Socio-Economic reintegration",
    "No",
    "Other",
]
more_info_gbv_bar_chart = create_mbar_chart(
    df,
    "Would you need more information about existing services for women affected by Violence?",
    more_info_gbv_options,
    "Need More Information on GBV Services",
)
st.plotly_chart(more_info_gbv_bar_chart)
# Need More Information on Child Protection Services
child_info_options = ["Psychological support", "Legal assistance", "No", "Other"]
child_info_bar_chart = create_mbar_chart(
    df,
    "Would you need more information about existing child protection services?",
    child_info_options,
    "Need More Information on Child Protection Services",
)
st.plotly_chart(child_info_bar_chart)
