#!/usr/bin/env python
# coding: utf-8

# # <span style="color:red">EDA Project - Analysis of AMCAT Data</span>

# ## <span style="color:blue">Columns Summary Table for dataset</span>

# * ID: Candidate ID
# * Salary: Salary of the candidate
# * DOJ: Date of joining the job
# * DOL: Date of leaving the job
# * Designation: Job designation/title
# * JobCity: City where the job is located
# * Gender: Gender of the candidate
# * DOB: Date of birth of the candidate
# * 10percentage: Percentage score in 10th grade
# * 12percentage: Percentage score in 12th grade
# * CollegeID: College ID of the candidate
# * CollegeTier: Tier of the college
# * Degree: Degree pursued by the candidate
# * Specialization: Specialization pursued by the candidate
# * CollegeGPA: Grade Point Average in college
# * CollegeCityID: ID of the college city
# * CollegeCityTier: Tier of the college city
# * CollegeState: State where the college is located
# * GraduationYear: Year of graduation
# * Domain: Domain knowledge score
# * ComputerProgramming: Score in computer programming
# * ElectronicsAndSemicon: Score in electronics and semiconductors
# * ComputerScience: Score in computer science
# * MechanicalEngg: Score in mechanical engineering
# * ElectricalEngg: Score in electrical engineering
# * TelecomEngg: Score in telecommunications engineering
# * CivilEngg: Score in civil engineering
# * Conscientiousness, Agreeableness, Extraversion, Neuroticism, Openness_to_experience: Personality trait scores

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from scipy.stats import chi2_contingency


# In[2]:


df = pd.read_csv(r"C:\Users\Sonu Vikas\Desktop\Internship 2024\Task 4\data.xlsx - Sheet1.csv")


# In[3]:


df.head()


# In[4]:


df.shape


# In[5]:


df.columns


# In[6]:


df.info()


# In[7]:


# Remove any duplicate rows
df.drop_duplicates(inplace=True)


# In[8]:


# Check for missing values
missing_values = df.isnull().sum()
missing_values


# In[9]:


# Assuming your DataFrame is named df
df.drop(columns=['Unnamed: 0'], inplace=True)


# In[10]:


df.describe()


# In[ ]:





# In[11]:


df


# In[ ]:





# ## <span style="color:blue">Univariate Analysis</span>

# In[12]:


df['Salary']


# In[13]:


sns.distplot(df['Salary'])


# * From above graph we can observe there is a outlier, Salary >10,00,000 is very rare, especially in the first job. So these are considered as outliers and removed.

# In[14]:


# Initialize a dictionary to store the count of rows for each salary threshold
salary_counts = {250000 * i: (df['Salary'] <= 250000 * i).sum() for i in range(1, 8)}

# Print the counts for each threshold
for threshold, count in salary_counts.items():
    print(f"Number of Rows in dataframe in which Salary <= {threshold}: {count}")


# In[15]:


indexNames = df[ df['Salary'] > 1000000 ].index 
# Delete these row indexes from dataFrame 
df.drop(indexNames , inplace=True) 
df.shape


# In[16]:


sns.distplot(df['Salary']);


# In[17]:


sns.distplot(df["10percentage"]);


# * The 10percentage column is not normally distributed and is Right Skewed and the max is in range 80-90

# In[18]:


sns.distplot(df["12percentage"]);


# * The 12percentage column is not normally distributed and outliers and the max is in range 70-80

# In[19]:


sns.distplot(df["English"]);


# * The English column is normally distributed and has max in range 400-600

# In[20]:


sns.distplot(df["Logical"]);


# * The Logical column is normally distributed and has max in range 400-700

# In[21]:


sns.distplot(df["Quant"]);


# * The Quant column is normally distributed and has max in range 400-800

# In[22]:


sns.distplot(df["Domain"]);


# * The collegecityid column is not normally distributed and has outliers

# In[21]:


sns.countplot(x='Gender',data=df, palette="Accent")


# * From above graph the count of males are more compared to females

# In[22]:


sns.countplot(x='CollegeTier',data=df, palette="Accent")


# * The count of tier 2 college is more!!

# In[25]:


plt.figure(figsize=(50, 50)) 
ax = sns.countplot(y="Specialization", data=df)


# In[23]:


sns.countplot(x='CollegeCityTier',data=df, palette="Accent")


# * The Collegecitytier 0 has high frequency to that of collegecitytier 1

# In[27]:


specialization_freq = df['Specialization'].value_counts() 
specialization_freq.plot(kind='bar', figsize=(15,5)) 


# In[28]:


df.loc[df['collegeGPA'] <= 10, 'collegeGPA'] *= 10 
df['collegeGPA'].plot(kind='hist', figsize=(15,5));


# * Bringing the CGPA to a 0-100 scale

# In[24]:


sns.barplot(x='CollegeCityTier',y='Salary',data=df, palette="Accent")


# In[ ]:





# In[ ]:





# ## <span style="color:blue">Bivariate Analysis</span>

# In[25]:


sns.barplot(x='CollegeCityTier',y='Salary',data=df, palette="Accent")


# In[31]:


sns.pairplot(df,vars=['CollegeTier', 'Salary'])


# * From the graph we observe that collegecitytier 1 has bagged with highest salary , and also to be noted that collegecity tier 0 also provide the same salary expectations

# In[26]:


sns.barplot(x='Gender',y='Salary',data=df, palette="Accent")


# In[33]:


sns.pairplot(df,vars=['Gender', 'Salary'])


# * Males and females take the salary more or less the same

# In[34]:


l = []
for i in df['Designation']:
    if 'senior' in i and 'engineer' not in i:
        l.append('senior')
    elif 'trainee' in i and 'engineer' not in i:
        l.append('trainee')
    elif 'engineer' in i and 'senior' not in i:
        l.append('engineer')
    elif 'associate' in i and 'senior' not in i:
        l.append('associate')
    elif 'developer' in i and 'senior' not in i:
        l.append('developer')
    elif 'manager' in i and 'senior' not in i:
        l.append('manager')
    elif 'analyst' in i:
        l.append('analyst')
    elif 'consultant' in i:
        l.append('consultant')
    elif 'executive' in i:
        l.append('executive')
    elif 'designer' in i:
        l.append('designer')
    else:
        l.append('others')


# In[35]:


df['Designations']=l 
df['Designations'].value_counts()


# In[36]:


sns.barplot(x='Designations',y='Salary',data=df)
plt.xticks(rotation=90)


# In[37]:


plt.figure(figsize=(20,20)) 
sns.heatmap(df.corr(),annot=True)


# In[39]:


sns.pairplot(data = df)


# In[40]:


sns.pairplot(data = df, diag_kind='kde')


# ## <span style="color:blue">Research Questions</span>

# * Research Question 1: Testing the Claim about Computer Science Engineering Jobs
# * Research Question 2: Relationship between Gender and Specialization

# In[ ]:


# Computer Science Engineers with specified job titles
computer_science_jobs = df[(df['Degree'] == 'ComputerScience') & 
                             (df['Designation'].isin(['Programming Analyst', 'Software Engineer', 
                                                        'Hardware Engineer', 'Associate Engineer']))]


# In[ ]:


# Calculate average salary 
average_salary = computer_science_jobs['Salary'].mean()
average_salary


# In[ ]:


# Gender and Specialization
contingency_table = pd.crosstab(df['Gender'], df['Specialization'])
contingency_table


# In[ ]:


# Chi-square test of independence
chi2, p, dof, expected = chi2_contingency(contingency_table)


# In[ ]:


chi2


# In[ ]:


p


# ## <span style="color:blue">Conclusion</span>

# * The dataset comprises candidate details including ID, salary, job tenure, designation, location, gender, education, and personality traits. 
# * Insights cover salary trends, demographics, education profiles, and personality influences on careers. 
# * Understanding these facets informs recruitment, roles, and salary dynamics.

# ## <span style="color:blue">Bonus</span>

# * Correlation between salary and education level.
# * Distribution of salaries across different cities or job titles.
# * Impact of college tier on salary expectations.
# * Trends in job tenure and salary growth over time.
# * Gender diversity and its impact on salary and job roles.
# * Comparison of salary distributions across different industries or sectors.

# ## <span style="color:blue">My Own research</span>

# * Numerical Features: Perform Column Standardization by subtracting the mean and dividing by the standard deviation.
# * Categorical Features: For categories more than 2, use dummy variables (one-hot encoding). For binary categories, convert to 0 or 1.
# * Use scikit-learn's 'StandardScaler' for numerical standardization.
# * Utilize pandas' 'get_dummies()' function for one-hot encoding and map function for binary conversion.

# In[ ]:




