import streamlit as st
import pandas as pd
import numpy as np
import get_data
import wash_data


def page_question2():
    st.title('question2')
    info=[0,1]
    select_loan=st.selectbox('Please enter whether the applicant has successfully borrowed (0 represents unsuccessful, 1 represents successful) ',info.columns.tolist())
    df_selected_new=get_data.select_Loan_Status(select_loan)
    info2=['ApplicantIncome','CoapplicantIncome','LoanAmount']
    select_line=st.selectbox('Please enter the data you want to view',info2.columns.tolist())
    mean=df_select_new[select_line].mean()
    min=df_select_new[select_line].min()
    max=df_select_new[select_line].min()
    data = {'mean': [mean],
        'min': [min],
        'max': [max]}
    df = pd.DataFrame(data)
    st.write(df)







