# -*- coding: utf-8 -*-
"""EDA Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OeZnE20SWMorF_Q3mR0tSCU7PSZ2IQB2

# **Project Name**    - Hotel Booking data

##### **Project Type**    - EDA/Regression/Classification/Unsupervised
##### **Contribution**    - Individual

# **Project Summary -**

Hotel booking data analysis and prediction is very important for business as it recognizes the growth and the customer behaviour and interst and growth rate of hotel

In hotel industry,customers are able to choose from one hotel to another and find best . In this highly competitive market ,the hotel industry every customer is important to the businees. By the analysis and hotel industy well know about the customer behavior and customer demand. by that hotel industry get information about how to and what to done by hotel from which a customer get happy by hotel services

# **GitHub Link -**

https://github.com/padmaSAINI-bot/Padma-SAINI--AlmaBetter/blob/1e044aab1dfbf19a29c131f92ff2bfb180451dfb/Module_2_EDA_Project.ipynb

# **Problem Statement**

**Write Problem Statement Here.**

#### **Define Your Business Objective?**

Increasing hotel booking and well management of hotel

# **General Guidelines** : -

1.   Well-structured, formatted, and commented code is required.
2.   Exception Handling, Production Grade Code & Deployment Ready Code will be a plus. Those students will be awarded some additional credits.
     
     The additional credits will have advantages over other students during Star Student selection.
       
             [ Note: - Deployment Ready Code is defined as, the whole .ipynb notebook should be executable in one go
                       without a single error logged. ]

3.   Each and every logic should have proper comments.
4. You may add as many number of charts you want. Make Sure for each and every chart the following format should be answered.
        

```
# Chart visualization code
```
            

*   Why did you pick the specific chart?
*   What is/are the insight(s) found from the chart?
* Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

5. You have to create at least 20 logical & meaningful charts having important insights.


[ Hints : - Do the Vizualization in  a structured way while following "UBM" Rule.

U - Univariate Analysis,

B - Bivariate Analysis (Numerical - Categorical, Numerical - Numerical, Categorical - Categorical)

M - Multivariate Analysis
 ]

# ***Let's Begin !***

## ***1. Know Your Data***

### Import Libraries
"""

# Import Libraries
import pandas as pd
import numpy as np

"""### Dataset Loading"""

# Load Dataset
from google.colab import drive
drive.mount('/content/drive')

hotel_df=pd.read_csv('/content/drive/MyDrive/Hotel Bookings.csv')

"""### Dataset First View"""

# Dataset First Look
hotel_df.head()

"""### Dataset Rows & Columns count"""

# Dataset Rows & Columns count
hotel_df.shape

"""### Dataset Information"""

# Dataset Info
hotel_df.info()

"""#### Duplicate Values"""

# Dataset Duplicate Value Count
hotel_df.duplicated().sum()

"""#### Missing Values/Null Values"""

# Missing Values/Null Values Count
hotel_df.isna().sum().sum()

# Visualizing the missing values
hotel_df.isna().sum()

"""### What did you know about your dataset?

The dataset given is a set from hotel and its services and we have to analysis the booking of hotels.
the goal is to understand and take steps how to increase hotel booking and how to statisfied customer by servicing and increase booking

## ***2. Understanding Your Variables***
"""

# Dataset Columns
hotel_df.columns

# Dataset Describe
hotel_df.describe()

"""### Variables Description

* **Hotel** : there are 2 hotels
* **is canceled**: which customer cancelled booking
* **Lead time** : Time taken by the customer to reach at hotel after placing booking
* **Arrival date year** : Booking/arrival  year
* **Arrival date month** : Booking/arrivalmonth  
* **Arrival date weeek number** : Arrival date and week number
* **Arrival date day of month** : Information about the date on which customer come in hotel
* **Stay in weekend nights** : Customer who stays in week end nights
* **adults** : Person who's age more then 18 booked hotel
* **Agent** : person through which hotel booked
* **Company** : company of agent
* **Days in waiting list** : waiting list for booking
* **Customer type** : customer type transient or contract or tranaient-party or group
* **Adr** : total adr
* **Required car parking spaces** : spaces fro paarking for each customer
* **Total of special requests** : special requests by customers
* **Reservation status** : reservation status check-out or cancelled
* **Reservation staus date** : status on reservation date
"""

hotel_df.head()

"""### Check Unique Values for each variable."""

# Check Unique Values for each variable.
unique_values = hotel_df.apply(lambda x:x.unique())
unique_values

for i in hotel_df.columns.tolist():
  print("No. of unique values in ",i,"is",hotel_df[i].nunique(),".")

"""## 3. ***Data Wrangling***

### Data Wrangling Code
"""

# Write your code to make your dataset analysis ready.
print(hotel_df.head())
print(hotel_df.info())
print(hotel_df.describe())

# creating copy of current dataset
df=hotel_df.copy()

# finding the hotel data between 60 to 70 rows using loc method
df.loc[60:70,['lead_time','arrival_date_year','arrival_date_month','stays_in_week_nights']]

#using iloc method
iloc_df=df.iloc[:10,4:8]  # index 10 & 8 is excluded

iloc_df

"""Rename"""

df.columns

# Rename a column
df.rename(columns={'is_canceled':'cancelled'},inplace=True)

df.head(1)

"""NEW COLUMN"""

# Creating a new column
df.loc[:,'half_lead_time']=df.loc[:,'lead_time']*0.5

df.head(1)

"""Drop columns & rows"""

df.columns

# drop a column (i'm not doing inplace = ture because of i i want my raw data same)
df.drop(['total_of_special_requests'],axis=1).head(1)

# Drop rows
df.drop([0,1,3],axis=0).head(5)

"""Handling missing values"""

df.shape

df.info()

#
df.loc[:,'company'].isna()

# Remove all rows having nan value anywhere
df.dropna()

#FILL NAN VALUE with method fillna()

df.fillna('no data found ').head(5)

# fillna on a specific column
df.loc[:,['agent']]=df.loc[:,['agent']].fillna('whatever')

df['agent'].head(5)

"""Sorting and handling duplicates"""

# Sorting the values of lead_time
df.sort_values(by='lead_time').head(5)

"""Drop duplicates

"""

#droping the duplicates
df.drop_duplicates(subset=['arrival_date_week_number'],keep='first').head(5)

"""Aggregation"""

df.lead_time.mean()

#Creating mean lead_time column
df['mean_lead_time']=df.lead_time.mean()

df.head()

#Max lead__time
df.lead_time.max()

# MIn leadtime
df.lead_time.min()

"""Group by"""

#Doing group by on a column
df.groupby('arrival_date_month').count().reset_index()

# Group by on multiple columns
df.groupby('hotel','reservation_status', 'lead_time', 'adults').count().reset_index()

"""Joining dataset"""

#Concat two datasets
df_Transient=df.loc[df.customer_type=='Transient']
df_other=df.loc[df.customer_type=='Transient']

pd.concat([df_Transient,df_other],axis=1).head()

"""Replace"""

df.deposit_type.value_counts()

#Replace a value from another whichever we want
df.deposit_type.replace({'No Deposit':'not recevied','Non Refund':'Not refundable','Refundable':'refundable'}).value_counts()

"""Apply"""

#we replace rest to others? --> We use apply with custom function

def dps_typ(l):
  if l=='No Deposit':
    return 'not recevied'
  elif l =='Non Refund':
    return 'Not refundable'
  else:
    return 'refundable'

dps_typ(l='No Deposit')

#apply function on a column
df.deposit_type.apply(dps_typ)

"""Dealing with strings"""

df.info()

#looking for  nan values
df.agent.str.contains('NaN').head()

df.head()

"""### What all manipulations have you done and insights you found?

Answer Here.

According to my idea, we will get a clear view of the customers who arn't book hotel or cnacel hotel booking . we have to deep dive into the customer booking and those behaviour and to search for some hypotheical statmets and insights which mights lead us to the reason or cancellation of booking . thats why i look the hotel booking data to find out the booking and cancellation and in which hotel have more booking and best facilities.Then I experiment with diffrent logics to extract some insights. I creat some new coloumns like mean lead time and half lead time and do some manipulation on exisitinh columns. and get a better vision for hotel booking data. furture i apply some method for treating null or nan values and do some rename in hotel booking data.Put some aggregation on booking data.

## ***4. Data Vizualization, Storytelling & Experimenting with charts : Understand the relationships between variables***
"""

import seaborn as sns
import matplotlib.pyplot as plt

"""#### Chart - 1"""

# Chart - 1 visualization code
for col in df.describe().columns:
  fig=plt.figure(figsize=(9,6))
  ax=fig.gca()
  feature= (df[col])
  sns.histplot(df[col],kde =True) # bin can be mentioned, if required
  ax.axvline(feature.mean(),color='magenta', linestyle='dashed', linewidth=2)
  ax.axvline(feature.median(),color='cyan', linestyle='dashed', linewidth=2)
  ax.set_title(col)
plt.show()

"""##### 1. Why did you pick the specific chart?

The histogram is a popular graphing tool. It is used to summarize discrete or continuous data that are measured on an interval scale. It is often used to illustrate the major features of the distribution of the data in a convenient form. It is also useful when dealing with large data sets (greater than 100 observations). It can help detect any unusual observations (outliers) or any gaps in the data.

Thus, I used the histogram plot to analysis the variable distributions over the whole dataset whether it's symmetric or not.

##### 2. What is/are the insight(s) found from the chart?

IN every histplot chart every coulmn made a relationship with each other like cancelled made a relation of count and just like that other columns have a relation with other.

##### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

Just a histogram and box plot cannot define business impact. It's done just to see the distribution of the column data over the dataset.

#### Chart - 2
"""

# Chart - 2  visualization code
# Visualizing code of box plot for each columns to know the data distibution
for col in df.describe().columns:
    fig = plt.figure(figsize=(9, 6))
    ax = fig.gca()
    df.boxplot( col, ax = ax)
    ax.set_title('Label by ' + col)
plt.show()

"""##### 1. Why did you pick the specific chart?

Visualizing Distribution and Summary Statistics: Box plots provide a clear visual summary of the distribution of your data, including information about the median, quartiles, and any potential outliers. This can be particularly useful when you want to understand the central tendency and spread of your data at a glance.

And it helps in to identify outliers

##### 2. What is/are the insight(s) found from the chart?

In this boxplot chart have different years and every year have different stay in weekdays night  and also we have each possibility chart from the hotel booking data colummns and helps us to more readable and visulazation of data.

##### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

With the help of these charts I find both negative and positive insights like in cancelled data i found outliers that's not good form the busniees prospective. the outliers shows the more cancellation of booking. And in other chart i found the positive outliers like in weekdays or weekend days the outliers shows the more booking made by the customers. so we found both positive and negative insights.

#### Chart - 3
"""

# Chart - 3 visualization code

# Creat a box plot chart to visualize the relation between reservation status and lead time
sns.barplot(data=hotel_df.head(20), x='reservation_status', y='lead_time')
# Creat title
plt.title('Lead time for Reservation status ')
plt.xlabel('reservation_status')
plt.ylabel('lead_time')
plt.figure(figsize=(20,15))
plt.show()

"""##### 1. Why did you pick the specific chart?

Bar charts show the frequency counts of values for the different levels of a categorical or nominal variable. Sometimes, bar charts show other statistics, such as percentages.

##### 2. What is/are the insight(s) found from the chart?

I found lead time for Reservation status. the mean lead time for both check-out or cancelled.

##### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

No,Here only shows the mean lead time of reservation status.it's only good for self or busniess understanding.Its gives a raw idea about the mean lead time of both reservation status.
there are some basic understaning about there are manage the canceled lead time reservation status.

#### Chart - 4
"""

# Chart - 4 visualization code
# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
#Plot 1 - scatter plot
sns.scatterplot(data=df, x='adr', y='stays_in_weekend_nights', ax=axes[0, 0], hue = 'arrival_date_year')
axes[0, 0].set_title('adr acoording to stays_in_weekend_nights  ')
axes[0, 0].set_xlabel('adr')
axes[0, 0].set_ylabel('stays_in_weekend_nights')


# Add vertical and horizontal lines
axes[0, 0].axvline(x=6, color='red', linestyle='--')
axes[0, 0].axhline(y=3, color='green', linestyle='--')

# Plot 2 - Box plot
sns.boxplot(data=df, x='hotel', y='lead_time', ax=axes[0, 1])
axes[0, 1].set_title('Lead time hotel wise ')
axes[0, 1].set_xlabel('Hotel')
axes[0, 1].set_ylabel(' Lead time ')

# Add grid
axes[0, 1].grid(True)

# Plot 3 - Violin plot
sns.violinplot(data=df, x='arrival_date_year', y='mean_lead_time', ax=axes[1, 0])
axes[1, 0].set_title('mean lead time of year 2015')
axes[1, 0].set_xlabel('year')
axes[1, 0].set_ylabel('Mean Lead time ')

# Add grid and xticks
axes[1, 0].grid(True)
axes[1, 0].set_xticks(range(len(df['arrival_date_year'].unique())))

# Plot 4 - KDE plot
sns.kdeplot(data=df, x='stays_in_week_nights', hue='hotel', fill=True, ax=axes[1, 1])
axes[1, 1].set_title('Hotel and stays in week nights ')
axes[1, 1].set_xlabel('week nights ')
axes[1, 1].set_ylabel('')

# Add text on the chart
axes[1, 1].text(9.8, 0.1, 'resort hotel', fontsize=10, color='blue')
axes[1, 1].text(5.6, 0.2, 'city hotel', fontsize=10, color='red')

# Adjust layout
plt.tight_layout() # Automatically Adjust

# Show plot
plt.show()

"""##### 1. Why did you pick the specific chart?

In this chart there are many charts to show the diffrent diffrent relation with each other .charts like scatter, box plot , violion plot and kde plot.

##### 2. What is/are the insight(s) found from the chart?

In the first chart i found the relation between adr and stay in week end nights. and in second chart found  hotel wise lead time and in next chart clearly see the year wise mean lead time. and  in the last chart found the hotel and stay in week night

##### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

In the box plot there are many lead time  outliers that shows the postive growth of busniess. and in the last chart city hotel have more week nights booking that's good for that hotel but less booking by resort hotel that is not a good nature of businees there should be few steps taken by resort hotel.

#### Chart - 5
"""

# Chart - 5 visualization code
sns.kdeplot(data=df['total_of_special_requests'],fill=True,color='blue')
plt.title('Kernel Density Estimate (KDE) of Quantity')
plt.xlabel('total_of_special_requests')
plt.ylabel('density')

plt.show()

"""##### 1. Why did you pick the specific chart?

I choose kde plot because the kde plot is shown best relation of density.
so kde plot is very useful to shown the density of special requests.

##### 2. What is/are the insight(s) found from the chart?

I found the insights in this chart is there are liner density in special repquests like zero special request density is the most and then there are liner reductionin density if special request increase then density decrease and vice-versha.

##### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

This insights not lead more negative impacts because the special request base on others factors that's not lead negative impacts on the busniess.

#### Chart - 6
"""

iscancelled=df[df['cancelled'] == 1].groupby('arrival_date_year').size().reset_index(name='count')

iscancelled

#Bar plot
x = list(iscancelled['arrival_date_year'])
y = list(iscancelled['count'])
sns.barplot(x= x, y=y)
plt.title('Year wise cancelled booking')
plt.xlabel('year')
plt.ylabel('cancelled')
plt.show

"""##### 1. Why did you pick the specific chart?

The bar graph is used to compare the items between different groups over time. Bar graphs are used to measure the changes over a period of time.
Thus, i have used bar chart to show the year wise cancelled booking.

##### 2. What is/are the insight(s) found from the chart?

I found the year wise cancellation.I found in 2016 there are the most cancellation of booking then in 2017 less then 2016 cancelled booking. and in 2015 all time low booking cancelled.

##### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

This chart creating impact on business by analysing this chart a manager or other managment person can a better decision about the why this year has more cancelled booking what the reason behidnd it and what step should be taken by managment so this type of condition not happens in the future.

#### Chart - 7
"""

# Chart - 7 visualization code
x = list(iscancelled['arrival_date_year'])
y = list(iscancelled['count'])
plt.pie(y,labels=x,autopct='%1.1f%%')
plt.title('Year wise cancellation percentage')
plt.show

"""##### 1. Why did you pick the specific chart?

A pie chart expresses a part to whole relationship in your data. It's to explain the percentage comparison through area covered in a cricle with diffrent colors.Where differenet percentage comparison comes into action pie chart is used frequently. So, I used Pie chart and which helped me to get the percentage comparision of the dependant variable.

##### 2. What is/are the insight(s) found from the chart?

From the above chart I got to know that there are three diffrent years and years have cancellation data. In 2015 hoel have overall 18.4% cancellation and in 2016 hotel have 46% of cancellation and in 2017 35.6% cancellation. that's means a good number of customer cancen their booking., immediate action should be taken

##### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

It's easy to loss customers but too difficult to aquire one.One happy customer will make 3-4  customer and vice-versha. in 2015 less cancellation compare to 2016 . 2016 have too much cancellation compare to other years this year negatively impact hotel booking . and in 2017 it decreses by approx 10% they might should have take right decision for booking and hotel services

#### Chart - 8
"""

# Chart - 8 visualization code
for col in df.describe().columns:
  fig=plt.figure(figsize=(9,6))
  ax=fig.gca()
  feature= (df[col])
  sns.lineplot(df[col]) # bin can be mentioned, if required
  ax.axvline(feature.mean(),color='magenta', linestyle='dashed', linewidth=2)
  ax.axvline(feature.median(),color='cyan', linestyle='dashed', linewidth=2)
  ax.set_title(col)
plt.show()

"""##### 1. Why did you pick the specific chart?

I choose this line chart beacause this chart give a brief explanation about each columns relationship with other . its give a very clear relation between each of them that's why i choose this chart.

##### 2. What is/are the insight(s) found from the chart?

Answer Here

##### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

there are many insights both negative and positive insights i found in charts and there are few step sholud be taken by managment how to overcome from mistakes and how to expend busniess.

#### Chart - 9
"""

# Chart -9 visualization code
# Select columns for the line plot
x_column = 'customer_type'
y_column = ['lead_time']

# Plot the data
plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")  # Set the style to whitegrid for a cleaner look

# Plot the line with smoothened trend
for i in y_column:
  sns.lineplot(data=df, x=x_column, y=i, linewidth=2, label = i)



# Add labels and title
plt.xlabel(x_column, fontsize=12, fontweight='bold', color='gray')
plt.ylabel('lead_time',fontsize=12, fontweight='bold', color='gray')
plt.title(f'customer type wise lead time ', fontsize=16, fontweight='bold')

# Customize tick parameters
plt.tick_params(axis='both', which='major', labelsize=10, colors='black')
plt.legend()
# Customize spine colors
plt.gca().spines['top'].set_color('none')
plt.gca().spines['right'].set_color('none')
plt.gca().spines['bottom'].set_color('gray')
plt.gca().spines['left'].set_color('gray')

# Show plot
plt.tight_layout()
plt.show()

"""##### 1. Why did you pick the specific chart?

I choose this line chart beacause this chart give a brief explanation about customer type and lead time. its give a very clear relation between both of them that's why i choose this chart.

##### 2. What is/are the insight(s) found from the chart?

I found the insight in this lineplot is the diffrent type of customer have diffrent lead time in this plot contract customer type have more lead time then others cutomer type and lowest lead time group customer type.

##### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

yes, these gained insights helps to creating positive business impact.by this plot a analysier get all infromation about which type of customer have more lead time and which type of customer have less lead time in hotel.

#### Chart - 10
"""

# Chart - 10 visualization code
plt.rcParams['figure.figsize'] = (12, 7)
color = plt.cm.copper(np.linspace(0, 0.5, 20))
((df.groupby(['hotel'])['stays_in_week_nights'].mean())*100).sort_values(ascending = False).head(10).plot.bar(color = ['orange','r'])
plt.title(" Hotel with stay in week nights percentage", fontsize = 20)
plt.xlabel('Hotel', fontsize = 15)
plt.ylabel('percentage', fontsize = 15)
plt.show()

"""##### 1. Why did you pick the specific chart?

Bar charts show the frequency counts of values for the different levels of a categorical or nominal variable. Sometimes, bar charts show other statistics, such as percentages.

##### 2. What is/are the insight(s) found from the chart?

In this bar i found that there are two hotel in chart shows both hotel with stay in week nights percentage and i found that resort hotel have more booking in week nights. and cityhotel  made less booking percentage.

##### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

yes. gained insights help to creating a positive business impact. because by this chart city hotel take a postive action how to increase the hotel booking in week nights. what steps should be taken for made more booking and apply more service in hotel. and know the reason behind that why city hotel made less booking then resort hotel.

#### Chart - 11
"""

# Chart - 11 visualization code

plt.figure(figsize=(8,6))
sns.set_style('darkgrid')
# Creat a box plot chart to visualize the relation between arrive date year and stay in weeks nights
plt.scatter(data=hotel_df,x='stays_in_weekend_nights',y='adults')
# Creat title

plt.title('stay in week nights')
plt.xlabel('stay in week end nights')
plt.ylabel('adults')
plt.show()

"""##### 1. Why did you pick the specific chart?

The scatter plot gives the better understading about the variables that we given inside it .
That's why i choose the scatter plot.

##### 2. What is/are the insight(s) found from the chart?

IN this scatter plot i found that nearest second week end nights there are more adults booked hotel.This is the positive hike in hotel booking and then other weekend nights not much booking of adults.

##### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

There are many insights in this chart first is around second weekend nights there are more booking of adults .this is not happening in other week end nights . this is helping to managment what is the resaon behind it and how to solve this obstacles.

#### Chart - 12
"""

df.head()

# Chart - 12 visualization code
# Creating scateer plot for adults in which months coming more adults
sns.scatterplot(x="arrival_date_month", y="adults", hue="hotel", data=df )
plt.title('Relation between Minute and Charge')
plt.xticks(rotation = 45)
plt.show()

"""##### 1. Why did you pick the specific chart?

The scatter plot gives the better understading about the variables that we given inside it .
That's why i choose the scatter plot.

##### 2. What is/are the insight(s) found from the chart?

The insights i found from this chart is there are aarival date month of customers and each month have booking of adults and i found that the october month have the most adults booking in this month and september also have a hike of booking of adults and other months does not have a much booking of adults.

##### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

Yes,this chart gives a impact on the busniess,this chart gives the idea about in which month there are have more adult booking and in which month have less adult booking.by this we found that why other months not done more booking of adults we found the reasin and work on  it this is helping to crating a positive busniess impact.

#### Chart - 13
"""

# Chart - 13 visualization code
plt.rcParams['figure.figsize'] = (12, 7)
color = plt.cm.copper(np.linspace(0, 0.5, 20))
((df.groupby(['hotel'])['stays_in_weekend_nights'].mean())*100).sort_values(ascending = False).head(10).plot.bar(color = ['violet','indigo','b','g','y','orange','r'])
plt.title(" Hotel and stay in weekend nights", fontsize = 20)
plt.xlabel('hotel', fontsize = 15)
plt.ylabel('percentage of stay on weekend nights', fontsize = 15)
plt.show()

"""##### 1. Why did you pick the specific chart?

Bar charts show the frequency counts of values for the different levels of a categorical or nominal variable. Sometimes, bar charts show other statistics, such as percentages.

##### 2. What is/are the insight(s) found from the chart?

In this bar i found that there are two hotel in chart shows bot hotel with stay in weekend  nights percentage and i found that resort hotel have more booking in weekend  nights. and cityhotel  made less booking percentage.

##### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

yes. gained insights help to creating a positive business impact. because by this chart city hotel take a postive action how to increase the hotel booking in week nights. what steps should be taken for made more booking and apply more service in hotel. and know the reason behind that why city hotel made less booking then resort hotel.

#### Chart - 14 - Correlation Heatmap
"""

# Chart - 14 visualization code
# Creating a beautiful heatmap
corr = df[df.describe().columns].corr()
# Create a beautiful heatmap
plt.figure(figsize=(10, 8))
sns.set(font_scale=1.2)  # Increase font size for readability

# Define custom color palette with more contrast
cmap = sns.diverging_palette(220, 20, as_cmap=True)

# Draw the heatmap with improved annotation and aesthetics
sns.heatmap(corr, cmap=cmap, annot=False, fmt=".2f", annot_kws={"size": 12, "weight": "bold"},
            linewidths=0.5, cbar_kws={"shrink": 0.8, "label": "Correlation Coefficient"},
            square=True, linecolor='white', vmin=-1, vmax=1)

# Add title
plt.title('Correlation Heatmap', fontsize=18)

# Rotate y-axis labels for better readability
plt.yticks(rotation=0)

# Show plot
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()

"""##### 1. Why did you pick the specific chart?

A correlation matrix is a table showing correlation coefficients between variables. Each cell in the table shows the correlation between two variables. A correlation matrix is used to summarize data, as an input into a more advanced analysis, and as a diagnostic for advanced analyses. The range of correlation is [-1,1].

Thus to know the correlation between all the variables along with the correlation coeficients, i used correlation heatmap.

##### 2. What is/are the insight(s) found from the chart?

From the above cprrelation heatmap i found relation between data like cancelled,lead time ,aarival date year,arrival date week number,arrival date day of month,stay in weekend nights,adults children and etc. on every column correlation applied.

#### Chart - 15 - Pair Plot
"""

# Chart - 15 visualization code
sns.pairplot(df, hue = 'hotel')

# Show plot
plt.show()

"""##### 1. Why did you pick the specific chart?

Pair plot is used to understand the best set of features to explain a relationship between two variables or to form the most separated clusters. It also helps to form some simple classification models by drawing some simple lines or make linear separation in our data-set.

Thus, I used pair plot to analyse the patterns of data and realationship between the features. It's exactly same as the correlation map but here you will get the graphical representation.

##### 2. What is/are the insight(s) found from the chart?

From the above chart I got to know, there are less linear relationship between variables and data poiunts aren't linearly separable. there are many chart each and every chart have their impoertance.the pair plot is the overall conclusion of data because there are many reltional chart.

## **5. Solution to Business Objective**

#### What do you suggest the client to achieve Business Objective ?
Explain Briefly.

* **.** Should be focus on how to reduce cancellation and find the most common reson of cancellation.
* **.** Be proactive with  customers communication and satisfy customers by services.
* **.** Periodically throw Offers to retain customers offer should be on vaction or on fastival time to attract more customers for booking the hotel.
* **.** Look at the customers facing problem with the service or booking or any problem happen journally with customer and resolve this.
* **.** Ask for feedback customer who chech-out from hotel this idea gives a beeter understanding about the where is mistake and wher is good in hotel service.
* **.** How to attract new customer or random customer for booking should define a roadmap and work on it.
* **.** Stay competitive.
* **.** Should provide special treatment for bookings.

# **Conclusion**

Overall conclusion is work on cancellation and increase special requests and booking in hotel and attarct city peopel as well as tourist. Make more reliable policies and attact customer by provding them the most services.

### ***Hurrah! You have successfully completed your EDA Capstone Project !!!***
"""