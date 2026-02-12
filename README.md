# Jaya Jaya Maju Human Resources Analytics Dashboard

## Bussiness Understanding

Jaya Jaya Maju, a multinational company operating since 2000 with more than 1,000 employees, is currently facing significant challenges in human resource management. The main issue is the increasing attrition rate, which has exceeded the 10% threshold. To mitigate the risk of further talent loss, the HR department requires an in-depth analysis of the key factors driving employee resignations, along with a comprehensive business dashboard to continuously monitor retention-related indicators.

## Business Problems

- The employee attrition rate has exceeded 10%, indicating serious talent retention issues.

- The company does not yet clearly understand the significant factors driving employees to resign.

- The HR department lacks a real-time business dashboard to monitor key metrics related to employee loyalty and workforce profiles.

## Project Scope

- Preparation: Setting up programming libraries and loading the `employee_data.csv` dataset.

- Data Understanding: Examining data structure, descriptive statistics, and identifying missing values.

- Data Preprocessing: Removing irrelevant data, handling missing values, and transforming data formats to prepare it for modeling.

- Exploratory Data Analysis (EDA): Identifying key trends and patterns related to employee attrition through visualization.

- Modeling: Building Machine Learning models to predict future attrition risk.

- Evaluation: Testing model performance and identifying the most influential factors.

- Visualization (Dashboard): Developing a business dashboard to help HR monitor employee metrics in real time.

## Preparation

The following are the steps to set up the environment:

**Data Source:**  
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

Based on the analysis conducted, the high attrition rate at Jaya Jaya Maju is primarily driven by workload and compensation factors, where overtime policies and monthly income levels are the most significant predictors of employee resignation. The developed machine learning models (such as Random Forest, XGBoost, and SVM) successfully identified high-risk employees with strong predictive performance. Through the interactive business dashboard, management now has a real-time monitoring tool that enables a shift from reactive policies to proactive, data-driven retention strategies aimed at reducing employee turnover below 10%.

## Recommended Action Items

- Action Item 1: Evaluate Workload and Overtime Policies
The company should conduct a thorough review of departments with the highest overtime rates and redesign workload distribution more equitably. Implementing maximum overtime limits and offering competitive compensation or incentives for extra working hours is strongly recommended to prevent physical and mental burnout, which is a primary driver of employee resignation.

- Action Item 2: Optimize Career Development and Employee Well-Being
HR management should establish transparent career development programs and provide clear internal promotion pathways based on objective performance metrics. Additionally, improving workplace quality through work-life balance initiatives and adjusting salary standards to match market value will significantly enhance employee loyalty and reduce the likelihood of employees seeking opportunities elsewhere.
