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
#To plot the mean value of the variables and make it visible in a bar plot.
def page_plot_bar():
    plt.style.use("ggplot")
    df_selected=data_selected()

    st.markdown('# **Average value matters while making your own decision** ')
    st.markdown('''
    ### 🔔 Use `multi-select` to change the category
    ''', unsafe_allow_html=True)
    
    df_x=df_selected[['Is_Female','Is_graduate','Is_married','Is_urban','Is_self_employed','Loan_Status','Credit_History','Dependents']]
    df_y=df_selected.drop(['Is_Female','Is_graduate','Is_married','Is_urban','Is_self_employed','Loan_Status','Credit_History','Dependents','Loan_ID'],axis=1)
    choice_x=st.selectbox('x variable',df_x.columns.tolist())
    choice_y=st.selectbox('y variable',df_y.columns.tolist())
    df_selected_g=df_selected.groupby(choice_x)
    df=df_selected_g[[choice_y]].mean()
    st.text("Average Values of y variables")
    st.bar_chart(df)
    return None

#Author:Yuxi Guo
#This function is to implement the box plot in our app.
def page_plot_box():
    plt.style.use("ggplot")
    st.title('Boxplot')
    
    st.markdown('# **This page will tell you about the discreteness of the data** ')
    st.markdown('# ***SEE WHERE U R AT 👀***')

    df_selected = data_selected().drop('Loan_ID',axis=1)
    df_x=df_selected[['Is_Female','Is_graduate','Is_married','Is_urban','Is_self_employed','Loan_Status','Credit_History','Dependents']]
    df_y=df_selected.drop(['Is_Female','Is_graduate','Is_married','Is_urban','Is_self_employed','Loan_Status','Credit_History','Dependents'],axis=1)
    choice_x=st.selectbox('x variable',df_x.columns.tolist())
    choice_y=st.selectbox('y variable',df_y.columns.tolist())
    s=sns.catplot(x=choice_x,y=choice_y,kind='box',data=df_selected)
    st.pyplot(s)
    return None

#Author:Yuxi Guo
#This section is to design pie chart of our dataset.
def page_plot_pie():
    plt.style.use("ggplot")

    st.markdown('# **On this page, you can clearly understand the proportion of data in different categories** :thinking_face:')
    st.markdown('''
    ### 🔔 Use `multi-select` to change the category
    ''', unsafe_allow_html=True)
    
    df_selected = data_selected()
    df_x=df_selected[['Is_Female','Is_graduate','Is_married','Is_urban','Is_self_employed','Loan_Status','Credit_History','Dependents']]
    choice_x=st.selectbox('Ways to classify',df_x.columns.tolist())
    df_selected_g=df_selected.groupby(choice_x)
    df=df_selected_g.count()
    fig,ax=plt.subplots()
    labels=[]
    #to implement the labels' length is the same to the number of rows
    if df.shape[0]==0:
        st.text('The dataset that you selected is empty, please give up some selectors.')
        return None
    else:
        for i in range(0,df.shape[0]):
            labels.append(f'{choice_x}:{df.index.tolist()[i]}')
    ax.pie(df['Loan_ID'],labels=labels,autopct="%1.1f%%")
    st.pyplot(fig)
    return None

#Author:Yuxi Guo
#This function is to design the heatmap page and plot it with the dataset selected.
def page_plot_heatmap():
    plt.style.use("ggplot")
    fig,ax=plt.subplots()
    df_selected=data_selected()
    df=df_selected.drop(['Loan_ID'],axis=1)
    cols=df.corr().abs().nlargest(9, 'Loan_Status')['Loan_Status'].index
    cm=df_selected[cols].corr()
    variables=cols.tolist()
    for v in range(0,len(variables)):
        variables[v]=variables[v][0:3]
    labels=cols.tolist()
    cax=ax.matshow(cm,cmap='hot_r')
    fig.colorbar(cax)
    tick_spacing=1
    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    ax.set_xticklabels(['']+variables)
    ax.set_yticklabels(['']+labels)
    description=
        '''
        Heatmap：
    The heatmap specifically visualizes the correlation between various of variables in the loan approval dataset. The variables are analyzed for their correlation with the "Loan_Status" variable, which is our target variable. Overall, It allows for the interactive exploration and analysis of the loan approval dataset, enabling users to identify the variables with the strongest correlations to loan status and gain insights into the relationships between variables.
    The following step is to show the specific correlation analysis between the different variables with the LOAN STATUS.
    
    Credit History: The "Credit_History" variable is expected to have a strong positive correlation with "Loan_Status". A good credit history generally increases the chances of loan approval.
    
    Marital Status: The "Married" variable may have a moderate positive correlation with "Loan_Status". Married individuals may have more stable financial situations, which could positively impact loan approval.
    
    Education: The "Education" variable (specifically, being a graduate or not) could have a moderate positive correlation with "Loan_Status". Graduates may have better job prospects and higher incomes, increasing the likelihood of loan approval.
    
    Urban Property: The "Property_Area" variable (specifically, being in an urban area) may have a weak positive correlation with "Loan_Status". Urban areas often offer better employment opportunities, potentially influencing loan approval.
    
    Loan Amount: The "LoanAmount" variable may have a weak positive correlation with "Loan_Status". Higher loan amounts might indicate higher financial stability, which could increase the chances of loan approval.
    
    Gender: The "Gender" variable (specifically, being female) could have a weak correlation with "Loan_Status". However, further analysis is needed to determine the nature of this correlation.
    
    Applicant and Co-applicant Income: The "ApplicantIncome" and "CoapplicantIncome" variables here have a relatively weak positive correlation with "Loan_Status". Nevertheless, higher incomes might indicate better repayment capabilities, positively affecting loan approval.
    
     Let's further analyze the correlation between "Loan_Status" and other variables for some specific combinations.
    
    Male Graduates who are Married:\
    Credit History: It is expected that a good credit history will strongly positive correlate with "Loan_Status" in this group. A good credit history will likely increase the chances of loan approval.
    Urban Property: Being in an urban area have a moderate positive correlation with "Loan_Status" in this group. Urban areas often offer better job opportunities, which can positively influence loan approval.
    Loan Amount: The "LoanAmount" variable have a weak positive correlation with "Loan_Status" in this group. Higher loan amounts might indicate higher financial stability, which could increase the chances of loan approval for male graduates who are married.
    
    Female Graduates who are Unmarried:\
    Credit History: The correlation between "Credit_History" and "Loan_Status" in this group may be stronger compared to other groups. A good credit history will likely have a significant positive impact on loan approval.
    Education: Being a graduate in this group have a moderate positive correlation with "Loan_Status". Graduates often have better job prospects, increasing the likelihood of loan approval.
    Applicant and Co-applicant Income: Higher incomes of both the applicant and co-applicant may have a stronger positive correlation with "Loan_Status" in this group. Higher incomes suggest better repayment capabilities, positively affecting loan approval.
    
    Applicants with Low Loan Amounts and Good Credit History:\
    Marital Status: Being married have a weak positive correlation with "Loan_Status" in this group. Married individuals might have more stable financial situations, increasing the chances of loan approval.
    Education: The correlation between being a graduate and "Loan_Status" in this group might be weak. However, further analysis is needed to determine the exact relationship.
    Urban Property: Being in an urban area could have a weak positive correlation with "Loan_Status" in this group. Urban areas often provide better employment opportunities, potentially influencing loan approval.
        '''
    st.markdown(description)
    st.pyplot(fig)
    return None
    
#Author:Yanlin Liu
def plot_pie_chart():
    st.markdown("# **Don't know your loan success rate? 🤷‍♂️** ")
    st.markdown('''
    ### COME AND SEE !
    ''', unsafe_allow_html=True)
    df_selected = pd.read_csv('loan_sanction_train.csv')
    image_path = 'image.png'  
    st.image(image_path, caption='Caption for image', use_column_width=True)
    
    # mapping the loan status to a string label
    df_selected['Loan_Status'] = df_selected['Loan_Status'].map({'Y': 'Yes', 'N': 'No'})
    # choose property area
    area_options = ['Urban', 'Semiurban', 'Rural']
    selected_area = st.selectbox(' Choose where you live', area_options)
    # filtering dataset
    df_area_selected = df_selected[df_selected['Property_Area'] == selected_area]
    
    # calculate distribution
    loan_status_distribution = df_area_selected[['Loan_Status']].value_counts(normalize=True)
    data_pair = [list(z) for z in zip(loan_status_distribution.index.tolist(), loan_status_distribution.values.tolist())]

    
    # create pie chart
    pie_chart = (
        Pie()
        .add("", data_pair)
        .set_global_opts(title_opts=opts.TitleOpts(title=f"{selected_area} Area Loan Approval Rates"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c} ({d}%)"))
        
    )
    # rending pie chart
    st_pyecharts(pie_chart)
    # 
    return None

#Author:Yuxi Guo
def plots():
    #This section is to implement the control flow of our app, where the pages designing are implemented.
    session_state=st.session_state
    if 'page' not in session_state:
        session_state['page']='Home'
    page=st.sidebar.radio('Navigate',['Plot_bar','Plot_box','Plot_pie','Plot_heatmap','loan success rate'])
    #to implement multi-pages
    
    if page=='Plot_bar':
        page_plot_bar()
    elif page=='Plot_box':
        page_plot_box()
    elif page=='Plot_pie':
        page_plot_pie()
    elif page=='Plot_heatmap':
        page_plot_heatmap()
    elif page=='loan success rate':
        plot_pie_chart()   
  

plots()


