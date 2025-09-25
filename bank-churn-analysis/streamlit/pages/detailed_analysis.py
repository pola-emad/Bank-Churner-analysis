import streamlit as st
import pandas as pd
import plotly.express as px

# Load the cleaned data

def load_data():
    churned_data = pd.read_csv('../../data/processed/bank_churners_complete.csv')
    return churned_data
#complete_data = pd.read_csv('bank-churn-analysis/data/processed/bank_churners_complete.csv')

# Main function for detailed analysis page
def main():
    st.title("Detailed Customer Churn Analysis")
    
    # Load data
    df = load_data()
    
    # Display data overview
    st.subheader("Data Overview")
    st.write(df.head())
    
    # Churn distribution
    st.subheader("Churn Distribution")
    churn_counts = df['Attrition_Flag'].value_counts()
    fig = px.pie(churn_counts, names=churn_counts.index, values=churn_counts.values, title='Churn Distribution')
    st.plotly_chart(fig)
    
    # Age distribution
    st.subheader("Customer Age Distribution")
    fig_age = px.histogram(df, x='Customer_Age', nbins=30, title='Customer Age Distribution')
    st.plotly_chart(fig_age)
    
    # Income category analysis
    st.subheader("Income Category Analysis")
    income_counts = df['Income_Category'].value_counts()
    fig_income = px.bar(income_counts, x=income_counts.index, y=income_counts.values, title='Income Category Counts')
    st.plotly_chart(fig_income)

    # Additional analyses can be added here

if __name__ == "__main__":
    main()