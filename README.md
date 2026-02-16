# Jaya Jaya Maju Human Resources Analytics Dashboard

## Bussiness Understanding

Jaya Jaya Maju, a multinational company operating since 2000 with more than 1,000 employees, is currently facing significant challenges in human resource management. The main issue is the increasing attrition rate, which has exceeded the 10% threshold. To mitigate the risk of further talent loss, the HR department requires an in-depth analysis of the key factors driving employee attrition, along with a comprehensive business dashboard to continuously monitor retention-related indicators.

## Business Problems

- The employee attrition rate has exceeded 10%, indicating serious talent retention issues.

- Identifying the key driver factors of employee attrition remains a challenge for the company, hindering effective retention strategies.

- The HR department lacks a real-time business dashboard to monitor key metrics related to employee loyalty, workforce demographics, and attrition trends.

## Project Scope

- **Preparation:** Setting up programming libraries and loading the `employee_data.csv` dataset.

- **Data Understanding:** Examining data structure, descriptive statistics, and identifying missing values.

- **Data Preprocessing:** Removing irrelevant data, handling missing values, and transforming data formats to prepare it for modeling.

- **Exploratory Data Analysis (EDA):** Identifying key trends and patterns related to employee attrition through visualization.

- **Modeling:** Building Machine Learning models to predict future attrition risk.

- **Evaluation:** Testing model performance and identifying the most influential factors.

- **Visualization (Dashboard):** Developing a business dashboard using Looker Studio to help HR monitor employee metrics in real time.
  
- **Conclusion and Recommended Action Items:** This section summarizes the key findings from the data analysis and provides actionable strategies to mitigate employee attrition.

## Preparation

The following are the steps to set up the environment:

### Data Source  
https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee  

### Environment Setup

If you install Python using Anaconda or Miniconda, you can use Conda as both a package manager and environment management system. Below are the steps to create a virtual environment for running the prediction:

1. Open Terminal or PowerShell.
2. Run the following command to create a new virtual environment:

```
conda create --name prediksi_attrition python=3.12.12
```

3. Activate the virtual environment:

```
conda activate prediksi_attrition
```

4. Install all required libraries:

```
pip install -r requirements.txt
```

5. Launch Jupyter Notebook:

```
jupyter-notebook
```

6. Open the `prediction.py` file.
7. Enter the data you want to predict into the data_baru variable.
8. Run the code.
9. The prediction results along with their description will be displayed.

## Business Dashboard

The Jaya Jaya Maju Business Dashboard is designed as a visual tool for the HR Department to monitor key indicators and factors contributing to high attrition rates.

**Looker Studio Dashboard Link:**
https://lookerstudio.google.com/u/0/reporting/4385e235-3535-4e86-9e9d-38938a6eb1e4/page/XtDQF

## Conclusion

Employee attrition at the company is mainly driven by workload and personal demographics. **OverTime_Yes** is the strongest factor, showing that excessive work and poor work-life balance are the primary reasons for employee attrition. Additionally, employees with the status of **MaritalStatus_Single** or those who fall under **BusinessTravel_Travel_Frequently** are more likely to experience attrition, as these factors often disrupt their personal stability.

From an operational side, roles like **JobRole_Sales Representative** and **JobRole_Laboratory Technician** have the highest turnover, likely due to high targets or repetitive tasks. Practical issues, such as a long **DistanceFromHome** and a history of frequently changing jobs (**NumCompaniesWorked**), also clearly predict who might experience attrition. On the other hand, a higher **MonthlyIncome**, better **JobLevel**, and more **TotalWorkingYears** act as "anchors" that keep employees loyal to the company.

To manage this risk, the company should use predictive technology. The **Random Forest** model is the most effective tool, with an impressive **94.51% accuracy** and an **AUC of 0.9827**. Because this model is so stable and accurate, the company can use it to identify "at-risk" employees early and create better strategies to keep them.

## Recommended Action Items

- **Review Workload and Overtime Policies**

The company should review how daily tasks are distributed, because heavy workloads and frequent overtime are major drivers of employee attrition. Management must ensure that employees have enough rest time to protect their physical and mental health, so productivity can remain stable over time.

- **Improve the Work Environment for Sales Representative and Lab Technician Roles**

Sales Representatives and laboratory technicians face high pressure and are at greater risk of burnout, which can increase attrition. The company should create a more supportive work environment and provide proper recognition for their achievements so they feel appreciated and valued.

- **Provide Flexible Work Options for Distance and Travel Issues**

Employees who live far from the office or travel frequently for work may experience high levels of fatigue, which can contribute to attrition. The company should offer flexible work options, such as remote work or improved travel scheduling. Transportation support or special allowances can also help reduce daily stress.

- **Strengthen Retention Programs for Single and Experienced Employees**

Single employees and those who frequently change jobs may have higher mobility, which can lead to higher attrition rates. The company should build a stronger sense of belonging through social activities or internal communities. Clear career development plans are also important so employees feel they have a stable and promising future within the company.
