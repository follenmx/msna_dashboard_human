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

st.header("Accommodation Information")

# Living Locations
living_loc_pie_fig = create_sex_distribution_pie_chart(
    df,
    "Do you currently live in a city or a village?",
    "Current Living Location: City vs. Village",
)
st.plotly_chart(living_loc_pie_fig)

# District

district_poc_bar = create_bar_chart(
    df,
    "In which district are you currently living?",
    "In which district are you currently living?",
)
st.plotly_chart(district_poc_bar)

# accommodation_type_bar

accommodation_type_bar = create_bar_chart(
    df,
    "What is your current accommodation type?",
    "Current Accommodation type",
)
st.plotly_chart(accommodation_type_bar)

# duration_of_stay

duration_of_stay = create_sex_distribution_pie_chart(
    df,
    "How long have you been in the Republic of Moldova?",
    "Duration of Stay in the Republic of Moldova",
)
st.plotly_chart(duration_of_stay)

# traveling_to_ukraine

traveling_to_ukraine = create_bar_chart(
    df,
    "(For Ukraine citizens) How often are you traveling to Ukraine?",
    "(For Ukraine citizens) How often are you traveling to Ukraine?",
)
st.plotly_chart(traveling_to_ukraine)
