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

st.header("Education")

# Children Attending School
attend_school_pie_chart = create_sex_distribution_pie_chart(
    df, "Are your children currently attending school?", "Children Attending School"
)
st.plotly_chart(attend_school_pie_chart)

# Educational Support Needed
ed_support_options = [
    "Language classes",
    "Tutoring",
    "Psychological support",
    "Extracurricular activities",
    "None",
    "Prefer not to say",
    "Other",
]
ed_support_bar_chart = create_mbar_chart(
    df,
    "What additional support do you think children from the refugee community might need to succeed in school?",
    ed_support_options,
    "Educational Support Needed",
)
st.plotly_chart(ed_support_bar_chart)

# Impact of Online Schooling
ed_online_pie_chart = create_sex_distribution_pie_chart(
    df,
    "What are your thoughts on the impacts of online schooling on children?",
    "Impact of Online Schooling on Children",
)
st.plotly_chart(ed_online_pie_chart)
