import streamlit as st


def check_contribution(employer_cont, employee_cont):
    if employee_cont == "Yes" and employer_cont == "Yes":
        return True
    return False


def highlight_rows_report(row):
    color = (
        "background-color: yellow;"
        if row["Type"] == "Report"
        else "background-color: white;"
    )
    return [color] * len(row)


def highlight_rows_penalty(row):
    color = (
        "background-color: red;"
        if row["Type"] == "Penalty"
        else "background-color: green;"
    )
    return [color] * len(row)


def exceed_report_token_threshold(report_token_balance, threshold):
    if report_token_balance >= threshold:
        return 1
    return 0


@st.dialog("Payment Gateway")
def pay_fine_dialog():
    st.text_input("Enter amount to pay (RM):")
    if st.button("Submit"):
        st.success(
            "Successfully paid penalty fine. Please refresh the page.", icon="✅"
        )
