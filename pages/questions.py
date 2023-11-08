import streamlit as st
import pandas as pd
import numpy as np
import get_data
import wash_data
import matplotlib.pyplot as plt

#Author:Yuxi Guo
#This section is to wash the data, making it more convenient for EDA. And I use some build-in functions to pad the nan value of data we chose.
def is_graduate(x):
    if x=='Graduate':
        return 1
    else:
        return 0
def is_female(x):
    if x=='Female':
        return 1
    else:
        return 0
def is_married(x):
    if x=='Yes':
        return 1
    else:
        return 0
def is_urban(x):
    if x=='Urban':
        return 1
    else:
        return 0
def is_self_employed(x):
    if x=='Yes':
        return 1
    else:
        return 0    
def Loan_Status_(x):
    if x=='Y':
        return 1
    else:
        return 0
    
def wash_data():
    HomeLoansApproval=pd.read_csv('loan_sanction_train.csv')
    #drop the data that has same ID
    HomeLoansApproval=HomeLoansApproval.drop_duplicates(subset=['Loan_ID'])
    #use subset to point out the columns whose nan values are deleted 
    HomeLoansApproval.dropna(axis=0,how='any',subset=['Gender','Married','Dependents','Self_Employed','Credit_History'],inplace=True)
    HomeLoansApproval_mean=HomeLoansApproval['LoanAmount'].fillna(value=HomeLoansApproval['LoanAmount'].mean(),inplace=False)
    #median replacing
    HomeLoansApproval_median=HomeLoansApproval['Loan_Amount_Term'].fillna(HomeLoansApproval['Loan_Amount_Term'].median(),inplace=False)
    #replace the old series object with new series.
    HomeLoansApproval=HomeLoansApproval.drop(labels=['LoanAmount','Loan_Amount_Term'],axis=1)
    HomeLoansApproval['LoanAmount']=HomeLoansApproval_mean
    HomeLoansApproval['Loan_Amount_Term']=HomeLoansApproval_median
    HomeLoansApproval['Is_graduate']=HomeLoansApproval['Education'].apply(lambda x:is_graduate(x))
    HomeLoansApproval['Is_Female']=HomeLoansApproval['Gender'].apply(lambda x:is_female(x))
    HomeLoansApproval['Is_married']=HomeLoansApproval['Married'].apply(lambda x:is_married(x))
    HomeLoansApproval['Is_urban']=HomeLoansApproval['Property_Area'].apply(lambda x:is_urban(x))
    HomeLoansApproval['Is_self_employed']=HomeLoansApproval['Self_Employed'].apply(lambda x:is_self_employed(x))
    HomeLoansApproval['Loan_Status_']=HomeLoansApproval['Loan_Status'].apply(lambda x:Loan_Status_(x))
    Loan_Status=HomeLoansApproval['Loan_Status_']
    HomeLoansApproval=HomeLoansApproval.drop(['Education','Gender','Married','Property_Area','Self_Employed','Loan_Status','Loan_Status_'],axis=1)
    HomeLoansApproval['Loan_Status']=Loan_Status
    HomeLoansApproval['Dependents']=HomeLoansApproval['Dependents'].apply(lambda x:( (0 if x=='0' else 1) if x!='2' else 2 )if x!='3+' else 3)
    return HomeLoansApproval
    
#Author:Yuxi Guo
#This section is to make a function that can connect the parameters of widgets of app to our dataset and get the selected data. 
def get_all_data():
    return wash_data()

#Author:Yuxi Guo
def select_data(size=1,is_graduate=None,is_married=None,is_female=None,is_self_employed=None,is_urban=None,credit_history=None):
    df=get_all_data()
    df=df.head(int(len(df)*size))
    df=df[df.columns if is_graduate==None else df['Is_graduate']==is_graduate]
    df=df[df.columns if is_female==None else df['Is_Female']==is_female]
    df=df[df.columns if is_self_employed==None else df['Is_self_employed']==is_self_employed]
    df=df[df.columns if is_married==None else df['Is_married']==is_married]
    df=df[df.columns if is_urban==None else df['Is_urban']==is_urban]
    df=df[df.columns if credit_history==None else df['Credit_History']==credit_history]
    return df

#Author:Tianqi Liu
def select_Loan_Status(x=None):
    df=get_all_data()
    df=df[df.columns if x==None else df['Loan_Status']==x]
    return df

#Author:Tianqi Liu
def select_Loan_Status(x=None):
    df=get_all_data()
    df=df[df.columns if x==None else df['Loan_Status']==x]
    return df

#Author:Xintong Hu
def page_question1():
    st.title("Question 1")
    st.header("Please choose your situation")
    df=wash_data()
    choice_App=st.selectbox('Applicant Income',["<5000","<10000","<15000","<=20000",">20000"])
    choice_App=(choice_App.replace('<',''))
    choice_App=(choice_App.replace('=',''))
    choice_App=float(choice_App.replace('>',''))
    if choice_App==5000:
        df=df[df['ApplicantIncome']<=5000]
    elif choice_App==10000:
        df=df[5000<df['ApplicantIncome']]
        df=df[df['ApplicantIncome']<=10000]
    elif choice_App==15000:
        df=df[10000<df['ApplicantIncome']]
        df=df[df['ApplicantIncome']<=15000]
    elif choice_App==20000:
        df=df[15000<df['ApplicantIncome']]
        df=df[df['ApplicantIncome']<=20000]
    else:
        df=df[df['ApplicantIncome']>20000]
    choice_Coapp=st.selectbox('CoApplicant Income',["0","<3000","<6000","<=10000",">10000"])
    choice_Coapp=(choice_Coapp.replace('<',''))
    choice_Coapp=(choice_Coapp.replace('=',''))
    choice_Coapp=float(choice_Coapp.replace('>',''))
    if choice_Coapp==0:
        df=df[df['CoapplicantIncome']==0]
    elif choice_Coapp==3000:
        df=df[0<df['CoapplicantIncome']]
        df=df[df['CoapplicantIncome']<=3000]
    elif choice_Coapp==6000:
        df=df[3000<df['CoapplicantIncome']]
        df=df[df['CoapplicantIncome']<=6000]
    elif choice_Coapp==10000:
        df=df[6000<df['CoapplicantIncome']]
        df=df[df['CoapplicantIncome']<=10000]
    else:
        df=df[df['CoapplicantIncome']>10000]
    df_success=df[df['Loan_Status']==1].shape[0]
    df_all=df.shape[0]
    if df_all==0:
        st.text("empty dataset")
        return None
    df_how=df_success*100/df_all
    if float(df_how)>60:
        st.balloons()
    df_how2=format(df_how,'.2f')   
    st.header("The probability of your loan success is:"+str(df_how2)+"%")
    st.text("Here are samples of this situation from existing data")
    st.dataframe(df)
    st.markdown("""The probability algorithm is based on the proportion of the successful number of databases to all eligible quantities. Therefore, due to the limitations of database data and the limited amount of data, the calculated results have limitations. This is only a reference for whether the applicant can successfully apply. The probability of reality varies greatly, please consider more based on individual circumstances.""")
    return None

#Author:Tianqi Liu
#To show the mean/max/min value of ApplicantIncome/CoapplicantIncome/LoanAmount under the selection of whether it is succesfully loaned.
def page_question2():
    st.title('Question 2')
    st.markdown("This section displays the distribution of three types of data: applicant income, coapplicant income, and applicant loan amount in the case of successful or unsuccessful borrowing. Quickly filter the conditions and click the button below!")
    st.write(':sparkles:'+':sparkles:'+':sparkles:'+':sparkles:'+':sparkles:'+':sparkles:'+':sparkles:')
    info=[0,1]
    select_loan=st.selectbox('Please enter whether the applicant has successfully borrowed (0 represents unsuccessful, 1 represents successful) ',info)
    df_select_new=select_Loan_Status(select_loan)
    info2=['ApplicantIncome','CoapplicantIncome','LoanAmount']
    select_line=st.selectbox('Please enter the data you want to view',info2)
    if st.button("generate"):
        mean=df_select_new[select_line].mean()
        mean=round(mean,2)
        min=df_select_new[select_line].min()
        max=df_select_new[select_line].max()
        st.write("The mean value of "+select_line+" is:")
        st.header(str(mean))
        st.write("The minimum value of "+select_line+" is:")
        st.header(str(min))
        st.write("The maximum value of "+select_line+" is:")
        st.header(str(max))
        data = {'mean': [mean], 'min': [min], 'max': [max]}
        x = ['mean', 'min', 'max']
        y = [data['mean'][0], data['min'][0], data['max'][0]]
        fig,ax=plt.subplots()
        ax.bar(x, y)
        plt.xlabel('Value')
        plt.ylabel('Data')
        plt.title('Data Distribution')
        st.pyplot(fig)
    if st.button('Information'):
        st.markdown('''
        This code defines a page named_ The function of question2() creates a page in the Streamlit application. This page displays the distribution of three data types (applicant income, co applicant income, and loan amount applied for) in the case of successful or failed loans. Users can quickly filter the conditions and click the button to view the distribution of different data types.
The specific application process is as follows:\ 
Display a title and a text explanation on the page.\ 
Create a select_ Loan selection box allows users to select whether the application was successful (0 represents unsuccessful, 1 represents successful).\ 
Based on the successful application selected by the user, filter out the corresponding records from the data to obtain a new data box df_ Select_ New.\ 
Create a select_ The line selection box allows users to select the type of data they want to view (applicant income, co applicant income, or loan amount applied for).\ 
If the user clicks on the 'generate' button:\ 
Calculate the average, minimum, and maximum values for the selected data type.\ 
Display the calculation results on the page.\ 
Create a bar chart with the average, minimum, and maximum values as the data for the bar chart, and draw the chart on the page.\ 
Through this method, users can understand the distribution of corresponding data by selecting different successful loan situations and data types, and visually display the average, minimum, and maximum values of the data through bar charts. This is very useful for analyzing the relationship between the applicant's income, loan amount, and the success or failure of the loan.\ ''')

    

def main():
    st.balloons()
    #This section is to implement the control flow of our app, where the pages designing are implemented.
    session_state=st.session_state
    if 'page' not in session_state:
        session_state['page']='Question1'
    page=st.sidebar.radio('Navigate',['Question1','Question2'])
    #to implement multi-pages
    if page=='Question1':
        page_question1()
    elif page=='Question2':
        page_question2()
   
main()





