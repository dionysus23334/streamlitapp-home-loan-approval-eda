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
    df_selected=data_selected()
    st.dataframe(df_selected)
    st.write('asdfghjkl')
    return None

#Author:Yuxi Guo
#To plot the mean value of the variables and make it visible in a bar plot.
def page_plot_bar():
    plt.style.use("ggplot")
    df_selected=data_selected()
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
            labels.append(f'{choice_x}:{i}')
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

def plot_pei_LiuYanLin():
    # 设置图表样式
    plt.style.use("ggplot")
    # 获取筛选后的数据
    df_selected = data_selected()
    # 用户选择分类方式
    choice_x = st.selectbox('选择分类方式', df_selected.columns.tolist())
    # 分组数据
    df_grouped = df_selected.groupby(choice_x).size().reset_index(name='counts')
    # 判断数据集是否为空
    if df_grouped.empty:
        st.text('您选择的数据集为空，请取消一些选择器。')
        return None
    # 构造饼图数据
    data_pair = [list(z) for z in zip(df_grouped[choice_x], df_grouped['counts'])]
    # 创建饼图
    pie_chart = (
        Pie(init_opts=opts.InitOpts(bg_color="#2c3e50"))  # 可以设置背景色等初始化选项
        .add(
            series_name="贷款状态",
            data_pair=data_pair,
            radius=["40%", "75%"],
            label_opts=opts.LabelOpts(
                position="outside",
                formatter="{b|{b}: }{c}  ({d}%)",
                background_color="#eee",
                border_color="#aaa",
                border_width=1,
                border_radius=4,
                rich={
                    "b": {"fontSize": 16, "lineHeight": 33},
                    "per": {"color": "#eee", "backgroundColor": "#334455", "padding": [2, 4], "borderRadius": 2},
                },
            ),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter=JsCode("function(x){return x.data.name + ': ' + x.data.value;}")))
    )
    # 在Streamlit中渲染饼图
    st_pyecharts(pie_chart)


#Author:Yuxi Guo
def main():
    #This section is to implement the control flow of our app, where the pages designing are implemented.
    session_state=st.session_state
    if 'page' not in session_state:
        session_state['page']='Home'
    page=st.sidebar.radio('Navigate',['Home','Plot_bar','Plot_box','Plot_pie','Plot_heatmap','LiuYanLin_pie'])
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
    elif page=='LiuYanlin_pie':
        plot_pei_LiuYanLin()    
main()
