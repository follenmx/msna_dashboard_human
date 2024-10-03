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

st.header("Future Plans and Needs")
# Level of Interaction
interaction_pie_chart = create_sex_distribution_pie_chart(
    df,
    "How would you describe the level of interaction between Ukrainian refugees and the local Moldovan community?",
    "Level of Interaction with Local Community",
)
st.plotly_chart(interaction_pie_chart)

# Future Concerns
future_concern_options = [
    "Uncertainty about the future / lack of long-term stability",
    "Financial insecurity / difficulty making ends meet",
    "Limited employment opportunities",
    "Inadequate or temporary housing conditions",
    "Separation from family members",
    "Difficulties with language and communication",
    "Concerns about legal status or documentation",
    "Lack of social integration / feeling isolated",
    "Prefer not to say",
    "Other (please specify)",
]
future_concern_bar_chart = create_mbar_chart(
    df,
    "What are your biggest concerns about your future in Moldova?",
    future_concern_options,
    "Future Concerns",
)
st.plotly_chart(future_concern_bar_chart)
# Urgent Needs
urgent_need_options = [
    "Affordable and stable housing",
    "Access to healthcare services",
    "Employment opportunities",
    "Legal assistance and documentation support",
    "Education for children and youth",
    "Mental health and psychosocial support",
    "Financial assistance",
    "Integration support and community connections",
    "Prefer not to say",
    "Other (please specify)",
]
urgent_need_bar_chart = create_mbar_chart(
    df,
    "In your opinion, what is the most urgent need for refugees in Moldova right now?",
    urgent_need_options,
    "Urgent Needs",
)
st.plotly_chart(urgent_need_bar_chart)
# Future Plans
plans_options = [
    "Return to Ukraine as soon as possible",
    "Stay in Moldova until it's safe to return to Ukraine",
    "Relocate to another country to join family/contacts",
    "Stay in Moldova long-term, regardless of the war",
    "Undecided / Don't know yet",
    "Prefer not to say",
    "Other (please specify)",
]
plans_bar_chart = create_mbar_chart(
    df,
    "What are your future plans regarding the war?",
    plans_options,
    "Future Plans Regarding the War",
)
st.plotly_chart(plans_bar_chart)
