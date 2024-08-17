import streamlit as st
from streamlit_option_menu import option_menu
from utils import check_contribution

st.set_page_config(
    # page_icon="img/kwsp_logo.png",
    page_title="EPFense",
    layout="wide",
    initial_sidebar_state="expanded")

#Options Menu
with st.sidebar:
    st.image('img/kwsp_logo.jpg', use_column_width=True)
    option_selected = option_menu('EPFense', ["Simulate Contribution", 'Employee Dashboard','Employer Dashboard', 'EPF Admin Dashboard'], 
        icons=['people-fill','house-fill','building-fill', 'person-fill-lock'],menu_icon='shield-shaded', default_index=0)


if option_selected=="Simulate Contribution":
    #Header
    st.title('Simulation')
    st.subheader('Employer Contribution and Employee Salary Deduction')

    employer_cont = st.selectbox("Employer Contribution",
                            ['Yes', 'No'])
    employee_cont = st.selectbox("Employee Contribution",
                            ['Yes', 'No'])
    if st.button('Simulate', type="primary"):
        if check_contribution(employer_cont, employee_cont):
            st.success('Contributions are made!',  icon="✅")
        else:
            st.error('Report token credited to employee wallet! Please make report to KWSP!', icon="❗")

# if option_selected=="Employee Dashboard":
    # st.image('img/laporan_token_full.jpg')
            


