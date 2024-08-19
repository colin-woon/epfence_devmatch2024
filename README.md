# Devmatch2024 Hackathon Project
## Execution Steps
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```
# EPFense

**EPFense** is a Streamlit-based web application that simulates the management of employer contributions, employee deductions, and penalty enforcement for a provident fund system.

## Overview

EPFense allows users to:

- Simulate employer and employee contributions.
- Manage report and penalty tokens using a blockchain-like system.
- Access personalized dashboards for employees, employers, and administrators.

## Technologies Used

- **Streamlit**: For building the interactive web interface and dashboards.
- **Requests**: To interact with the MASCHAIN API for token operations.
- **Pandas**: For data manipulation and display in tabular form.
- **MASCHAIN API**: Handles token minting, burning, transferring, and balance checks.
- **Session State**: Manages state variables across user interactions.
- **Streamlit Option Menu**: Provides sidebar and horizontal menu navigation.
- **Environment Variables**: Securely stores API URLs, client IDs, and wallet addresses.

## Features

- **Contribution Simulation**: Simulate and validate employer and employee contributions.
- **Token Management**: Employees receive report tokens; employers receive penalty tokens based on compliance.
- **Dashboard Views**:
  - **Employee Dashboard**: Manage report tokens and submit reports.
  - **Employer Dashboard**: Monitor and pay penalties.
  - **EPF Admin Dashboard**: Oversee reports and penalties, with options to penalize employers.
- **Transaction History**: View token transactions with conditional highlights.
- **Automated Penalization**: Automatically penalizes when report token thresholds are exceeded.

# Maschain Block Explorer Link
## LAP Token  
[https://explorer-testnet.maschain.com/0xa395ba475eb9c2cd4a342565431792a7cc0f4a19dec17636cd6af387b368e3d9](https://explorer-testnet.maschain.com/0xa395ba475eb9c2cd4a342565431792a7cc0f4a19dec17636cd6af387b368e3d9)  
*First Transaction of LAP Token*
```
{
            "to": "0x3C4129Ecec857F0BB51f74182d07C25508185b13",
            "from": "0xE5aeE252eC16a7CC735A445b2761Dba479cDA3cc",
            "status": "success",
            "blockNumber": 3105156,
            "transactionHash": "0xa395ba475eb9c2cd4a342565431792a7cc0f4a19dec17636cd6af387b368e3d9",
            "method": "transfer",
            "decimal": 1,
            "amount": "10",
            "token": {
                "contract_address": "0xdaC1319E9f1DF1A2430014B145Ad28643F3ac90a",
                "name": "Token",
                "symbol": "LAP"
            },
            "timestamp": "2024-08-17T10:21:06.000000Z"
}
```

## DEN Token
[https://explorer-testnet.maschain.com/0xd1cbecb50916aa85d48a5cc13b32f34769f095028f4e496b7279183842abb122](https://explorer-testnet.maschain.com/0xd1cbecb50916aa85d48a5cc13b32f34769f095028f4e496b7279183842abb122)  
*First Transaction of DEN Token*
```
{
            "to": "0x3C4129Ecec857F0BB51f74182d07C25508185b13",
            "from": "0xD155F8B216f9De9F74bE3D9B015e0f6D649EC4c6",
            "status": "success",
            "blockNumber": 3112263,
            "transactionHash": "0xd1cbecb50916aa85d48a5cc13b32f34769f095028f4e496b7279183842abb122",
            "method": "transfer",
            "decimal": 1,
            "amount": "10",
            "token": {
                "contract_address": "0x4E5716309bE61E540F31E4EC4416E92a4602b520",
                "name": "Token",
                "symbol": "DEN"
            },
            "timestamp": "2024-08-17T22:11:48.000000Z"
}
```
