import streamlit as st
import requests
import pandas as pd
from streamlit_option_menu import option_menu
from utils import (
    check_contribution,
    highlight_rows_report,
    highlight_rows_penalty,
    exceed_report_token_threshold,
    pay_fine_dialog,
)
from maschain_api import (
    provide_penalty_token,
    provide_report_token,
    get_report_token_balance,
    report_to_kwsp,
    get_penalty_token_balance,
    pay_fine_to_kwsp,
    get_report_token_transaction,
    get_penalty_token_transaction,
    check_wallet_owner,
    burn_for_penalty,
)


# State Varibables
# Dictionary of default values
default_values = {
    "report_token_amount": 0,
    "penalty_token_amount": 0,
    "wallet_owner": "0",
}

# Initialize session state variables if they don't already exist
for key, value in default_values.items():
    if key not in st.session_state:
        st.session_state[key] = value

st.set_page_config(
    page_title="EPFense",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Options Menu
with st.sidebar:
    st.image("img/EPFense_logo.jpg", use_column_width=True)
    sidebar_choice = option_menu(
        "EPFense",
        [
            "Simulate Contribution",
            "Employee Dashboard",
            "Employer Dashboard",
            "EPF Admin Dashboard",
        ],
        icons=["people-fill", "house-fill", "building-fill", "person-fill-lock"],
        menu_icon="shield-shaded",
        default_index=0,
    )


if sidebar_choice == "Simulate Contribution":
    # Header
    st.title("Simulation")
    st.subheader("Employer Contribution and Employee Salary Deduction")

    employer_cont = st.selectbox("Employer Contribution", ["Yes", "No"])
    employee_cont = st.selectbox("Employee Salary Deduction", ["Yes"])
    if st.button("Simulate", type="primary"):
        if check_contribution(employer_cont, employee_cont):
            st.success("Contributions are made!", icon="✅")
        else:
            response = provide_report_token()
            # st.write(response)
            if response["status"] == 200:
                response = get_report_token_balance()
                st.session_state.report_token_amount = response["result"]
                st.error(
                    "Report token credited to employee wallet! Please make report to KWSP!",
                    icon="❗",
                )
            else:
                st.error(response)

if sidebar_choice == "Employee Dashboard":
    # st.write(response)

    menu_option = option_menu(
        None,
        ["Home", "Wallet", "Settings"],
        icons=["house", "wallet-fill", "gear"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
    )
    report_token_threshold = 3
    if menu_option == "Home":
        response = get_report_token_balance()
        st.session_state.report_token_amount = response["result"]
        # st.write(st.session_state.report_token_amount)
        if st.session_state.report_token_amount != "0":
            if exceed_report_token_threshold(
                float(st.session_state.report_token_amount), report_token_threshold
            ):
                st.warning(
                    "You have exceeded the report token threshold, the system will burn your tokens and send a penalty to the employee",
                    icon="⚠️",
                )
                response = burn_for_penalty(report_token_threshold)
                st.write(response)
                if response["status"] == 200:
                    new_response = provide_penalty_token()
                    st.write(new_response)
                    if new_response["status"] == 200:
                        st.info(
                            "KWSP will take legal action on your behalf. Please refresh the page.",
                            icon="ℹ️",
                        )
            else:
                st.error(
                    "You have LAP tokens! Please submit a token in 'Wallet' menu to make a report to KWSP!",
                    icon="❗",
                )
        else:
            st.success("Good Afternoon!", icon="👋")

    if menu_option == "Wallet":
        response = get_report_token_balance()
        st.session_state.report_token_amount = response["result"]
        st.header("")
        left_co, cent_co, last_co = st.columns(3, vertical_alignment="center")

        with cent_co:
            st.header("Employee Wallet", anchor=False)
            st.image("img/laporan_token_full.jpg", width=50, use_column_width=True)
            st.info(f"Balance: LAP   {st.session_state.report_token_amount}", icon="🪙")
            if st.button("Make Report", type="primary"):
                response = report_to_kwsp()
                # st.write(response)
                if response["status"] == 200:
                    response = get_report_token_balance()
                    st.session_state.report_token_amount = response["result"]
                    st.success(
                        "Report has been sent to EPF. Please refresh the page to update wallet balance.",
                        icon="✅",
                    )

if sidebar_choice == "Employer Dashboard":
    response = get_penalty_token_balance()
    st.session_state.penalty_token_amount = response["result"]
    # st.write(response)

    menu_option = option_menu(
        None,
        ["Home", "Penalty", "Settings"],
        icons=["house", "exclamation-octagon-fill", "gear"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
    )

    if menu_option == "Home":
        # st.write(st.session_state.penalty_token_amount)
        if st.session_state.penalty_token_amount != "0":
            st.error(
                "You have DEN tokens! KWSP is taking legal action! Please reimburse the proper amount to EPF and pay the fine at 'Penalty' menu!",
                icon="❗",
            )
        else:
            st.success("Good Afternoon!", icon="👋")

    if menu_option == "Penalty":
        st.header("")
        left_co, cent_co, last_co = st.columns(3, vertical_alignment="center")

        with cent_co:
            st.header("Penalty Tokens", anchor=False)
            st.image("img/denda_token_full.jpg", width=50, use_column_width=True)
            st.info(
                f"Balance: DEN   {st.session_state.penalty_token_amount}", icon="🛑"
            )
            if st.button("Pay Fine", type="primary"):
                response = pay_fine_to_kwsp()
                pay_fine_dialog()
                # st.write(response)
                if response["status"] == 200:
                    response = get_penalty_token_balance()
                    st.session_state.penalty_token_amount = response["result"]

if sidebar_choice == "EPF Admin Dashboard":
    response = get_penalty_token_balance()
    st.session_state.penalty_token_amount = response["result"]
    # st.write(response)

    menu_option = option_menu(
        None,
        ["Report Dashboard", "Penalty Dashboard", "Settings"],
        icons=["flag-fill", "hammer", "gear"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
    )

    if menu_option == "Report Dashboard":
        response = get_report_token_transaction()
        df = pd.DataFrame(
            [
                {
                    "Type": "Report" if item["method"] == "transfer" else "Credit",
                    "Timestamp": item["timestamp"],
                    "Report From": item["from"],
                    "Token To": item["to"],
                }
                for item in response["result"]
            ]
        )
        styled_df = df.style.apply(highlight_rows_report, axis=1)
        st.dataframe(styled_df, use_container_width=True, hide_index=True)
        left_co, cent_co, last_co = st.columns(3, vertical_alignment="center")
        with left_co:
            wallet_address = st.text_input("Wallet Address")
        if st.button("Check"):
            st.session_state.wallet_owner = check_wallet_owner(wallet_address)
            st.info(st.session_state.wallet_owner, icon="ℹ️")
        if st.button("Penalize", type="primary"):
            response = provide_penalty_token()
            if response["status"] == 200:
                st.error(f"Penalty given to {st.session_state.wallet_owner}", icon="🚨")

    if menu_option == "Penalty Dashboard":
        response = get_penalty_token_transaction()
        df = pd.DataFrame(
            [
                {
                    "Type": "Penalty" if item["method"] == "mint" else "Payment",
                    "Timestamp": item["timestamp"],
                    "Payment From": item["from"],
                    "Penalty To": item["to"],
                }
                for item in response["result"]
            ]
        )
        styled_df = df.style.apply(highlight_rows_penalty, axis=1)
        st.dataframe(styled_df, use_container_width=True, hide_index=True)
        left_co, cent_co, last_co = st.columns(3, vertical_alignment="center")
        with left_co:
            wallet_address = st.text_input("Wallet Address")
        # with cent_co:
        if st.button("Check"):
            wallet_owner = check_wallet_owner(wallet_address)
            st.info(wallet_owner, icon="ℹ️")
