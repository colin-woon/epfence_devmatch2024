import requests
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

API_URL = os.getenv("MASCHAIN_API_URL")
CLIENT_ID = os.getenv("CLIENT_KEY")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# Wallets
EMPLOYER_WALLET = os.getenv("EMPLOYER_WALLET")
EMPLOYEE_WALLET = os.getenv("EMPLOYEE_WALLET")
EPFENSE_ADMIN_WALLET = os.getenv("EPFENSE_ADMIN_WALLET")

# Token Smart Contracts
REPORT_SC_ADDRESS = os.getenv("REPORT_SC_ADDRESS")
PENALTY_SC_ADDRESS = os.getenv("PENALTY_SC_ADDRESS")

headers = {
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "content-type": "application/json",
}


def provide_report_token():
    data = {
        "wallet_address": EPFENSE_ADMIN_WALLET,
        "to": EMPLOYEE_WALLET,
        "amount": "1",
        "contract_address": REPORT_SC_ADDRESS,
        "callback_url": "http://localhost:8501",
    }

    response = requests.post(f"{API_URL}/api/token/mint", headers=headers, json=data)
    return response.json()


def provide_penalty_token():
    data = {
        "wallet_address": EPFENSE_ADMIN_WALLET,
        "to": EMPLOYER_WALLET,
        "amount": "1",
        "contract_address": PENALTY_SC_ADDRESS,
        "callback_url": "http://localhost:8501",
    }

    response = requests.post(f"{API_URL}/api/token/mint", headers=headers, json=data)
    return response.json()


# @st.cache_data
def get_report_token_balance():
    data = {
        "wallet_address": EMPLOYEE_WALLET,
        "contract_address": REPORT_SC_ADDRESS,
    }

    response = requests.post(f"{API_URL}/api/token/balance", headers=headers, json=data)
    return response.json()


def get_penalty_token_balance():
    data = {
        "wallet_address": EMPLOYER_WALLET,
        "contract_address": PENALTY_SC_ADDRESS,
    }

    response = requests.post(f"{API_URL}/api/token/balance", headers=headers, json=data)
    return response.json()


def report_to_kwsp():
    data = {
        "wallet_address": EMPLOYEE_WALLET,
        "to": EPFENSE_ADMIN_WALLET,
        "amount": "1",
        "contract_address": REPORT_SC_ADDRESS,
        "callback_url": "http://localhost:8501",
    }

    response = requests.post(
        f"{API_URL}/api/token/token-transfer", headers=headers, json=data
    )
    return response.json()


def pay_fine_to_kwsp():
    data = {
        "wallet_address": EPFENSE_ADMIN_WALLET,
        "to": EMPLOYER_WALLET,
        "amount": "1",
        "contract_address": PENALTY_SC_ADDRESS,
        "callback_url": "http://localhost:8501",
    }

    response = requests.post(
        f"{API_URL}/api/token/token-transfer", headers=headers, json=data
    )
    return response.json()


def get_report_token_transaction():
    data = {
        "wallet_address": EPFENSE_ADMIN_WALLET,
        "contract_address": REPORT_SC_ADDRESS,
        "filter": "to|from",
        "status": "success",
    }

    response = requests.get(
        f"{API_URL}/api/token/get-token-transaction", headers=headers, json=data
    )
    return response.json()


def get_penalty_token_transaction():
    data = {
        "wallet_address": EPFENSE_ADMIN_WALLET,
        "contract_address": PENALTY_SC_ADDRESS,
        "filter": "to|from",
        "status": "success",
    }

    response = requests.get(
        f"{API_URL}/api/token/get-token-transaction", headers=headers, json=data
    )
    return response.json()


def check_wallet_owner(wallet_address):
    response = requests.get(
        f"{API_URL}/api/wallet/wallet/{wallet_address}", headers=headers
    )
    response = response.json()

    return response["result"]["name"]
