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

st.header("PwD Information")

dif1_bar = create_bar_chart(
    df,
    "Do you have difficulty seeing, even when wearing glasses?",
    "Difficulty Seeing, Even When Wearing Glasses",
)
st.plotly_chart(dif1_bar)
dif2_bar = create_bar_chart(
    df,
    "Do you have difficulty hearing, even if using a hearing aid?",
    "Difficulty Hearing, Even When Using a Hearing Aid",
)
st.plotly_chart(dif2_bar)
dif3_bar = create_bar_chart(
    df,
    "Do you have difficulty walking or climbing steps?",
    "Difficulty Walking or Climbing Steps",
)
st.plotly_chart(dif3_bar)
dif4_bar = create_bar_chart(
    df,
    "Do you have difficulty remembering or concentrating?",
    "Difficulty Remembering or Concentrating",
)
st.plotly_chart(dif4_bar)

st.markdown("---")
#
pwd_hh_pie_chart_fig = create_sex_distribution_pie_chart(
    df,
    "Are there other members in the household that have a lot of difficulty or cannot do any one of these actions?",
    "Are there other members in the household that have a lot of difficulty or cannot do any one of these actions?",
)
st.plotly_chart(pwd_hh_pie_chart_fig)
# PwD Household
pwd_household_histogram_fig = create_histogram(
    df,
    "How many household members that are having significant difficulties with any of the actions above are there in general, excluding you?",
    "How many household members that are having significant difficulties with any of the actions above are there in general, excluding you?",
)
st.plotly_chart(pwd_household_histogram_fig)

pwd_household_kid_histogram_fig = create_histogram(
    df,
    "How many among them are children under 18?",
    "How many among them are children under 18?",
)
st.plotly_chart(pwd_household_kid_histogram_fig)

pwd_household_elderly_histogram_fig = create_histogram(
    df,
    "How many senior people aged over 60 are among them?",
    "How many senior people aged over 60 are among them?",
)
st.plotly_chart(pwd_household_elderly_histogram_fig)
