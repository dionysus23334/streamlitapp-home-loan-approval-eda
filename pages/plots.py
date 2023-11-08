import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd




#Author:Yuxi Guo
def main():
    #This section is to implement the control flow of our app, where the pages designing are implemented.
    session_state=st.session_state
    if 'page' not in session_state:
        session_state['page']='Home'
    page=st.sidebar.radio('Navigate',['Home','Plot_bar','Plot_box','Plot_pie','Plot_heatmap','LiuYanLin_pie','LiuTianqi','HuXintong'])
    #to implement multi-pages
    if page=='Home':
        page_home()
    elif page=='Plot_bar':
        page_plot_bar()
    elif page=='Plot_box':
        page_plot_box()
    elif page=='Plot_pie':
        page_plot_pie()
    elif page=='Plot_heatmap':
        page_plot_heatmap()
    elif page=='LiuYanLin_pie':
        plot_pie_chart()   
    elif page=='LiuTianqi':
        page_question2()
    elif page=='HuXintong':
        Page_selected()
main()


