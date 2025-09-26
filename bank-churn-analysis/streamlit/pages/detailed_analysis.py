import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data
@st.cache_data
def load_analysis_objects():
    
    path = r'bank-churn-analysis/notebooks/analysis_objects.pkl'

    with open(path, 'rb') as f:
        return pickle.load(f)

def make_title(selected):
    # Build human readable title: base "Customer Churn Overview" then append selected dims
    base = "Customer Churn analysis"
    if not selected:
        return base
    # Keep "Overview" as primary if present
    parts = []
    if "Overview" in selected:
        parts.append("Overview")
    others = [s for s in selected if s != "Overview"]
    if others:
        # convert "Churn by Age" -> "by Age" etc -> produce list like "by Age", "by Gender"
        suffixes = []
        for o in others:
            # drop common prefix if present
            if o.lower().startswith("churn by "):
                suffixes.append(o[9:].strip())
            else:
                suffixes.append(o)
        # format suffixes with commas and 'and'
        if len(suffixes) == 1:
            parts.append(f"by {suffixes[0]}")
        else:
            parts.append("by " + ", ".join(suffixes[:-1]) + ", and " + suffixes[-1])
    return ", ".join([p for p in parts if p]) if parts else base

def render_overview(df, churned_df, analysis_objects):
    st.header("Overview")
    st.subheader("Sample of data")
    st.dataframe(df.sample(5).reset_index(drop=True))
    total = len(df)
    total_churn = len(churned_df)
    churn_rate = total_churn / total * 100 if total else 0.0
    cols = st.columns(3)
    cols[0].metric("Total customers", f"{total:,}")
    cols[1].metric("Total churners", f"{total_churn:,}")
    cols[2].metric("Overall churn rate", f"{churn_rate:.2f}%")
    # show overall churn chart if present in pickle
    try:
        "churn rate figure" in analysis_objects:
        st.subheader("Overall churn distribution")
        st.pyplot(analysis_objects["churn rate figure"].get_figure())
    except:
        st.info("Overall churn chart not available in saved analysis. Showing key metrics above.")
    st.markdown("#### High-level drivers (from analysis)")
    st.markdown(
        "- Top categorical signals: gender, income category, education level.\n"
        "- Top numerical signals: Total_Trans_Ct, Total_Ct_Chng_Q4_Q1, Total_Revolving_Bal.\n"
        "- Early priorities: low‑income (\"Less than $40K\") and low‑activity (Total_Trans_Ct ≤ 9) segments."
    )

def render_churn_by_age(obj):
    st.header("Churn by Age")
    st.plotly_chart(obj, use_container_width=True)
    st.markdown("Most churn occurs in the 36–55 age bands.")
    st.markdown("Recommendations:\n- Target retention offers to the 36–55 cohort; pilot segmented messaging to measure lift.")

def render_churn_by_card(obj, pivot_card=None):
    st.header("Churn by Credit Card Category")
    st.plotly_chart(obj, use_container_width=True)
    if pivot_card is not None:
        st.subheader("Churn by Card — table")
        st.dataframe(pivot_card.reset_index())
    st.markdown(
        "Findings: Blue card holds the majority of churners. Platinum churns are rare but may be high value."
    )
    st.markdown("Recommendations:\n- Run scale retention for Blue card holders; prioritize personalized retention for Platinum customers.")

def render_churn_by_transactions(num_figures, scatter_list=None):
    st.header("Churn by Transactions")
    # num_figures expected to be a list of stored figures (histograms)
    for i, fig in enumerate(num_figures):
        st.plotly_chart(fig, use_container_width=True)
        # avoid repeating similar captions
        if i == 0:
            st.markdown("Low transaction volume (Total_Trans_Ct ≤ 9) is a clear high‑risk signal.")
    if scatter_list:
        st.subheader("1D scatter views")
        for f in scatter_list:
            st.plotly_chart(f, use_container_width=True)
    st.markdown("Recommendations:\n- Re‑engagement offers for low‑activity customers; test incentives to increase transactions.")

def render_churn_by_education(obj, pivot_edu=None):
    st.header("Churn by Education Level")
    st.plotly_chart(obj, use_container_width=True)
    if pivot_edu is not None:
        st.subheader("Education — table")
        st.dataframe(pivot_edu.reset_index())
    st.markdown("Majority of churners are graduates; doctorate holders show high churn rate but small sample size.")
    st.markdown("Recommendations:\n- Investigate small‑N groups (doctorate) before scaling; target Graduate segment for retention.")

def render_churn_by_income(obj, pivot_income=None):
    st.header("Churn by Income Category")
    st.plotly_chart(obj, use_container_width=True)
    if pivot_income is not None:
        st.subheader("Income — table")
        st.dataframe(pivot_income.reset_index())
    st.markdown("Findings: 'Less than $40K' contributes the largest share (~37% of churners) and shows elevated within‑group churn (~17%).")
    st.markdown("Recommendations:\n- Prioritize a targeted retention pilot for the 'Less than $40K' segment (A/B test).")

def render_churn_by_gender(obj=None, pivot_gender=None):
    st.header("Churn by Gender")
    if obj:
        st.plotly_chart(obj, use_container_width=True)
    if pivot_gender is not None:
        st.subheader("Gender — table")
        st.dataframe(pivot_gender.reset_index())
    st.markdown("Females appear slightly more likely to churn than males (small effect).")
    st.markdown("Recommendation:\n- Test tailored messaging by gender; evaluate uplift before wide rollout.")

# Main function for detailed analysis page
def main():
    st.set_page_config(layout="wide", page_title="Churn — Detailed Analysis")
    analysis_objects = load_analysis_objects()

    # Access objects from pickle (keys expected from notebook)
    df = analysis_objects.get('df')
    churned_df = analysis_objects.get('churned_df')
    pivot_edu = analysis_objects.get('pivot_edu')
    pivot_income = analysis_objects.get('pivot_income')
    # plotly figure objects (if present)
    churn_edu_level = analysis_objects.get('churn by education figure')
    churn_income_level = analysis_objects.get('churn by income figure')
    churn_credit_category = analysis_objects.get('churn by credit category figure')
    churn_age = analysis_objects.get('churn by age')
    num_figures = analysis_objects.get('churn by num featerues')  # list
    num_features_scatter = analysis_objects.get('scatter plots for num features')  # list
    pivot_card = analysis_objects.get('pivot_card')
    pivot_gender = analysis_objects.get('pivot_gender')
    churn_gender_fig = analysis_objects.get('churn by gender figure')
    overall_churn_fig = analysis_objects.get('churn rate figure')

    # Sidebar checkboxes
    st.sidebar.header("Sections")
    opts = [
        "Overview",
        "Churn by Age",
        "Churn by Credit Card Category",
        "Churn by Transactions",
        "Churn by Education Level",
        "Churn by Income Category",
        "Churn by Gender",
    ]
    selections = []
    for label in opts:
        default = True if label == "Overview" else False
        if st.sidebar.checkbox(label, value=default):
            selections.append(label)

    # Dynamic title
    page_title = make_title(selections)
    st.title(page_title)

    # Render sections in a fixed order if selected; this avoids duplication and keeps layout stable
    if "Overview" in selections:
        render_overview(df, churned_df, analysis_objects)

    if "Churn by Age" in selections:
        if churn_age is not None:
            render_churn_by_age(churn_age)
        else:
            st.warning("Churn by age figure not available in saved analysis.")

    if "Churn by Credit Card Category" in selections:
        if churn_credit_category is not None:
            render_churn_by_card(churn_credit_category, pivot_card=pivot_card)
        else:
            st.warning("Churn by credit card figure not available in saved analysis.")

    if "Churn by Transactions" in selections:
        if num_figures:
            render_churn_by_transactions(num_figures, scatter_list=num_features_scatter)
        else:
            st.warning("Transaction-level figures not available in saved analysis.")

    if "Churn by Education Level" in selections:
        if churn_edu_level is not None:
            render_churn_by_education(churn_edu_level, pivot_edu=pivot_edu)
        else:
            st.warning("Churn by education figure not available in saved analysis.")

    if "Churn by Income Category" in selections:
        if churn_income_level is not None:
            render_churn_by_income(churn_income_level, pivot_income=pivot_income)
        else:
            st.warning("Churn by income figure not available in saved analysis.")

    if "Churn by Gender" in selections:
        if churn_gender_fig is not None or pivot_gender is not None:
            render_churn_by_gender(obj=churn_gender_fig, pivot_gender=pivot_gender)
        else:
            st.warning("Churn by gender outputs not available in saved analysis.")

if __name__ == "__main__":
    main()
