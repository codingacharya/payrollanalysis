import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit app title
st.title("HR & Payroll Data Analysis")

# Upload CSV File
uploaded_file = st.file_uploader("Upload Payroll Data (CSV)", type=["csv"])

if uploaded_file:
    # Load data
    df = pd.read_csv(uploaded_file)
    
    # Show dataset preview
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # Calculate payroll statistics
    total_payroll = df["Total_Pay"].sum()
    total_overtime_expense = (df["Overtime_Hours"] * df["Overtime_Rate"]).sum()

    st.subheader("Payroll Overview")
    st.write(f"**Total Payroll Expenses:** ${total_payroll:,.2f}")
    st.write(f"**Total Overtime Expense:** ${total_overtime_expense:,.2f}")

    # Highest Paid Employees
    top_paid = df.nlargest(5, "Total_Pay")[["Name", "Department", "Total_Pay"]]
    st.subheader("Top 5 Highest Paid Employees")
    st.dataframe(top_paid)

    # Payroll by Department
    dept_payroll = df.groupby("Department")["Total_Pay"].sum().sort_values(ascending=False)

    # Visualization - Salary Distribution
    st.subheader("Salary Distribution")
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(df["Total_Pay"], bins=10, color="blue", alpha=0.7, edgecolor="black")
    ax.set_xlabel("Salary Range ($)")
    ax.set_ylabel("Number of Employees")
    ax.set_title("Salary Distribution")
    ax.grid(True)
    st.pyplot(fig)

    # Visualization - Payroll Cost by Department
    st.subheader("Payroll Cost by Department")
    fig, ax = plt.subplots(figsize=(8, 5))
    dept_payroll.plot(kind="bar", color="green", ax=ax)
    ax.set_xlabel("Department")
    ax.set_ylabel("Total Payroll Expense ($)")
    ax.set_title("Payroll Cost by Department")
    ax.grid(axis="y", linestyle="--", alpha=0.7)
    st.pyplot(fig)

else:
    st.info("Please upload a CSV file to analyze payroll data.")
