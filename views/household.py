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

st.header("Household Information")

# Household
household_histogram_fig = create_histogram(
    df, "How many members are in your household, including you?", "Household Size"
)
st.plotly_chart(household_histogram_fig)

household_kid_histogram_fig = create_histogram(
    df,
    "Of these, how many are children under 18?",
    "Household Size (only children under 18)",
)
st.plotly_chart(household_kid_histogram_fig)

household_elderly_histogram_fig = create_histogram(
    df,
    "Of these, how many are senior citizens, aged over 60?",
    "Household Size (only senior citizens, aged over 60)",
)
st.plotly_chart(household_elderly_histogram_fig)

st.markdown("---")
