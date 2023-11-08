# streamlitapp-home-loan-approval-eda
## The Introduction

This APP is committed to showing the relationship between various aspects and whether the user can borrow according to the user's selection conditions. This app is a user page with strong interaction with users. Here's how to use it:
* The page has a sidebar for users to choose according to their own ideas, and this sidebar has three major blocks. The "Navigate" block allows the user to select different graphs (heat maps, bar charts, etc.) to show the relationship between each condition and the success of the loan, for example, clicking on the Plot_bar will show the average personal income of the male and female successful loan (in the data we collect). In the "The size of data" block, the user drags and drops the displayed line to select the cardinality of the dataset, for example, if you select 0.5, the displayed data analysis will be performed in the first half of the dataset we collected. The last block is to let the user select the condition to better query the information, for example, select "true" in "graduate", and the chart will only show the data analysis graph of the graduated population.
* The main page of the page is selected by the "Navigate" block. The "home" page is a brief introduction to the app and the publication of our dataset. The "Plot" page is a display of charts, and there are also blocks on the charts for users to select conditions, so as to show the data analysis graphs that users need in more detail. On the rest of the pages, there will be detailed questions that are of common interest to users, and users can follow the page introduction and get some data sheets.

## Dataset Source
Home Loan Approval (loan_sanction_train.csv)\
https://www.kaggle.com/datasets/rishikeshkonapure/home-loan-approval?select=loan_sanction_train.csv
About the company Dream Housing Finance Corporation. They have a presence in all urban, semi-urban and rural areas. They would like to present the relevant charts based on the details of the customer provided when filling out the online application form. These details include the borrower's gender, marital status, educational background, employment situation, income situation, co-applicant income, loan amount required, repayment time, number of loans, place of residence, etc. Here, they provide a partial data set.

## The Process of Development
Our team used two versions in the process of building the APP. In order to show the completeness of the team work, we will briefly introduce the two versions of our app before and after. The following is the completed version of our first version:
![version1_homepage](https://github.com/dionysus23334/streamlitapp-home-loan-approval-eda/blob/main/version1_Home_page.jpg)
![version1_plot](https://github.com/dionysus23334/streamlitapp-home-loan-approval-eda/blob/main/version1_plot.jpg)

Here's an introduction to the first version:
This APP is committed to showing the relationship between various aspects and whether the user can borrow according to the user's selection conditions. This app is a user page with strong interaction with users. Here's how to use it:
* The page has a sidebar for users to choose according to their own ideas, and this sidebar has three major blocks. The "Navigate" block allows the user to select different graphs (heat maps, bar charts, etc.) to show the relationship between each condition and the success of the loan, for example, clicking on the Plot_bar will show the average personal income of the male and female successful loan (in the data we collect). In the "The size of data" block, the user drags and drops the displayed line to select the cardinality of the dataset, for example, if you select 0.5, the displayed data analysis will be performed in the first half of the dataset we collected. The last block is to let the user select the condition to better query the information, for example, select "true" in "graduate", and the chart will only show the data analysis graph of the graduated population.\
* The main page of the page is selected by the "Navigate" block. The "home" page is a brief introduction to the app and the publication of our dataset. The "Plot" page is a display of charts, and there are also blocks on the charts for users to select conditions, so as to show the data analysis graphs that users need in more detail. On the rest of the pages, there will be detailed questions that are of common interest to users, and users can follow the page introduction and get some data sheets.\
The following is the introduction of the second version: (The second version is the completed version of our APP, and the detailed page can be directly viewed with our APP)
The second version is an improvement over the first version, the second version has three more pages than the first version, a total of four pages, users can choose what they want to know according to the page blocks on the sidebar, which is more intuitive and clear than the first version, and we have added the result analysis of the data, which can better help users judge whether they are likely to succeed in the loan.\
Finally, here's what we do in the group (names in alphabetical order)\
Junjie Zheng completed plot-heatmap,questions, loan success rate data result analysis and text filling\
Tangyu Guo completes the analysis of the data results of home, plot-bar, plot-box, plot-pie and the text filling and all the editing of the readme section\
Tianqi Liu completes question2 Code editing for the page\
Xintong Hu Complete question1 Code editing for the page\
Yanlin Liu completes loan success rate Code editing for the page\
Yuxi Guo completes the data screening, overall code architecture and diagramming\


## Conclusion

### Revenue:
1. The wage demand for men with successful loan conditions is slightly higher than that of women
2. Graduate loan success conditions have higher salary requirements than non-graduates
3. The salary requirement of unmarried users is slightly higher than that of married users
4. The wage demand of rural hukou users is slightly higher than that of urban hukou users
5. The wage demand of the successful conditions of the loan for the entrepreneurial group is higher than that of the working group users
6. The above conditions are similar to the relationship between the co-applicant's income\

### Loan Amount:
1. Men usually have more money to borrow than women
2. Graduates usually borrow more than non-graduates
3. Married users can usually borrow more than unmarried people
4. Rural accounts usually have more borrowing amounts than urban accounts
5. Entrepreneurs usually have more borrowing money than working people
6. People who do not have a loan record usually have more borrowing amount than users who have a record
7. The above conditions are similar to the relationship between the borrowing time and the duration of the loan


