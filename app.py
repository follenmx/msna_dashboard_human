import pandas as pd
import streamlit as st
from templates.chart_templates import *

st.set_page_config(
    page_title="MSNA:Dashboard",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("📊MSNA Survey: Data Analysis")
st.markdown("---")
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
    "`Do you currently live in a city or a village?`.isin(@accomodation_filter)"
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

# PAGE_SETUP

demographic_page = st.Page(
    page="views/demographic.py", title="Demographic Information", icon="🚻"
)
accommodation_page = st.Page(
    page="views/accommodation.py", title="Accommodation Information", icon="🏠"
)
household_page = st.Page(
    page="views/household.py", title="Household Information", icon="👨‍👩‍👧"
)
pwd_page = st.Page(page="views/pwd.py", title="PwD Information", icon="👩🏻‍🦯")

healthcare_access = st.Page(
    page="views/healthcare_access.py", title="Healthcare Access", icon="🏥"
)
health_insurance = st.Page(
    page="views/health_insurance.py",
    title="Health Insurance and Informations",
    icon="📝",
)

feedback_assessment = st.Page(
    page="views/feedback_assessment.py",
    title="Overall Assessment and Feedback",
    icon="💬",
)


safety_protection = st.Page(
    page="views/safety_protection.py", title="Safety and Protection", icon="🛡️"
)
mhpss_protection = st.Page(page="views/mhpss.py", title="MHPSS", icon="💆")
education_protection = st.Page(page="views/education.py", title="Education", icon="📚")
employment = st.Page(page="views/employment.py", title="Employment", icon="💼")
integration_and_involvement = st.Page(
    page="views/integration_and_involvement.py",
    title="Future Plans and Needs",
    icon="➡️",
)


pg = st.navigation(
    {
        "Demographic Information": [
            demographic_page,
            accommodation_page,
            household_page,
            pwd_page,
        ],
        "Health": [healthcare_access, health_insurance, feedback_assessment],
        "Protecion": [
            safety_protection,
            mhpss_protection,
            education_protection,
            employment,
            integration_and_involvement,
        ],
    }
)

pg.run()
