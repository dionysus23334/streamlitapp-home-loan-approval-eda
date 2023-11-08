from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.commons.utils import JsCode
from streamlit_echarts import st_pyecharts
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import numpy as np
import streamlit as st
import wash_data
import get_data

#Author:Yuxi Guo
def data_selected():
    '''
    This section is to get the dataset selected and transfer the dataset to plots function that works in different pages.
    '''
    x = st.sidebar.slider('The size of data:', 0.0, 1.0, 1.0, 0.01)
    df = wash_data.wash_data()
    is_graduate = st.sidebar.selectbox('Graduate', [None, True, False])
    is_married = st.sidebar.selectbox('Married', [None, True, False])
    is_female = st.sidebar.selectbox('Female', [None, True, False])
    is_self_employed = st.sidebar.selectbox('Self_employed', [None, True, False])
    is_urban = st.sidebar.selectbox('Urban', [None, True, False])
    credit_history = st.sidebar.selectbox('Credit_History', [None, True, False])
    df_selected = get_data.select_data(x, is_graduate, is_married, is_female, is_self_employed, is_urban,
                                       credit_history)
    return df_selected

#Author:Yuxi Guo
#To implement the home page and make our dataset visible.
def page_home(): 
    df_selected = data_selected() 
    # Display the welcome message in the center, bold, and larger font 
    st.markdown("<h1 style='text-align: center; font-size: 2em; font-weight: bold;'>Welcome to our app</h1>", unsafe_allow_html=True) # Display the DataFrame below the welcome message 
    st.markdown("<h2 style='font-weight: bold;'>APP Introduction:</h2>\n" "After analyzing the customer's own information, the customer will judge the likelihood of the success of the loan based on our analysis results.", unsafe_allow_html=True) 
    st.markdown("<h2 style='font-weight: bold;'>Dataset Source:</h2>\n" "About the company Dream Housing Finance Corporation. They have a presence in all urban, semi-urban and rural areas. They would like to present the relevant charts based on the details of the customer provided when filling out the online application form. These details include the borrower's gender, marital status, educational background, employment situation, income situation, co-applicant income, loan amount required, repayment time, number of loans, place of residence, etc. Here, they provide a partial data set.", unsafe_allow_html=True) 
    st.dataframe(df_selected) # Display the introduction text 
    return None


#Author:Yuxi Guo
def main():
    st.balloons()
    #This section is to implement the control flow of our app, where the pages designing are implemented.
    session_state=st.session_state
    if 'page' not in session_state:
        session_state['page']='Home'
    page=st.sidebar.radio('Navigate',['Home'])
    #to implement multi-pages
    if page=='Home':
        page_home()
    
main()
