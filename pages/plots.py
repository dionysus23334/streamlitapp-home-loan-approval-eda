import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import wash_data
import get_data

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
    
    # 贷款状态映射到字符串标签
    df_selected['Loan_Status'] = df_selected['Loan_Status'].map({'Y': 'Yes', 'N': 'No'})
    # 用户选择地区类型
    area_options = ['Urban', 'Semiurban', 'Rural']
    selected_area = st.selectbox(' Choose where you live', area_options)
    # 根据所选地区筛选数据
    df_area_selected = df_selected[df_selected['Property_Area'] == selected_area]
    
    # 计算贷款状态的分布
    loan_status_distribution = df_area_selected[['Loan_Status']].value_counts(normalize=True)
    data_pair = [list(z) for z in zip(loan_status_distribution.index.tolist(), loan_status_distribution.values.tolist())]

    
    # 创建饼图
    pie_chart = (
        Pie()
        .add("", data_pair)
        .set_global_opts(title_opts=opts.TitleOpts(title=f"{selected_area} Area Loan Approval Rates"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c} ({d}%)"))
        
    )
    st_pyecharts(pie_chart)
    # 使用st_pyecharts在Streamlit中渲染饼图
    return None

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


