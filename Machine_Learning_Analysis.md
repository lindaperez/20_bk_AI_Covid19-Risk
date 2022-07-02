# Machine Learning Analysis Summary

## Overview and Purpose
As Mexico is listed in the top 5 countries with the most COVID death rate , we are going to look into the factors that may be significantly relevant to death, based on which we would like to classify the high risks group and the low risk groups in face with COVID.

<br>At the end of the analysis, we are planning to use the machine learning model to provide the initial screening of the patients who are potentially infected with COVID, and classify them into high risk or low risk group for further diagnosis and treatment.

## Hypothesis and Data Preprocessing 
Given the purpose of the analysis, we found the COVID patient data for the machine learning model, released by [**Mexico Government**](https://datosabiertos.salud.gob.mx/gobmx/salud/datos_abiertos/datos_abiertos_covid19.zip), which includes basic info of patients, as well as the status of underlying medical conditions, hospitalization status and deceased info. 

<Br> The hypothesis is that, patients who have medical underlying conditions are more likely to be faced with severe situation, even death from COVID infection, and are supposed to be classified as high risk group of COVID.

<Br>A glance of columns, data types and initial data preprocessing decision as follows:
![data_and_preprocessing](./Image/data_and_preprocessing.png)

<Br>As the end goal is to create a Machine Learning model and make predications of high/low risk groups of COVID, we are going to focus on the data: 

- Whose COVID results were positive
- Whose columns show the medical underlying conditions, age, gender that may be significant relevant to the result 'Death'
- Other info which may help with the prediction, such as ['closed_contact'] and ['other_complication'].

<Br>After the initial preprocesing, We dropped couple irrelevant and duplicate info columns and advance into the second stage of the preprocessing -- <strong>regroup and data cleaning</strong>.

<Br>We further regroup and clean the remaining columns to address following issues:

- ['date_patient_death'] is further categorized and labeled as '0' for 'alive', '1' for 'deceased' based on the date input
- ['age'] is regrouped and labeled from 1 to 5. The regrouped age category indicates below:
    - Child(0-16) : 1
    - Young_Adults(17-32) : 2
    - Middle_age_Adults(33-48) : 3
    - Old_age_Adults(49-64) : 4
    - Senior_Adults(65-90) : 5
* We also analyzed the ['age'] column and get the 1st Quartile,median, and 3rd Quartile. Based on the definition of Outlier, age above 91 is considered outlier. We further dropped the outliers.
- Rest of the columns are showing the categorical integer. We further regroup the category ['Unknown'] or ['N/A'] to ['No'], so that each medical conditions or features have clean input - Yes and No. 

## Preliminary Feature Engineering and Feature Selection
After the data preprocessing, we are having an all-integer full datasets, with each input as categorical numeric. We are clear that ['Death'] is going to be the target. We would like to decide on the features that will be used to fit into the model. 

### Statistical Analysis for Underlying Medical Conditions using R Language 
As both the target and potential features are categorical numeric, we are using Chi-squared test and logistic Regression in R to validate if the underlying medical conditions are significant relevant to the target ['Death']. The result shows almost all the medical conditions, as well as age(Adults and senior people) are significant relative to the target ['Death'] based on the clean patient data(P value is smaller than 0.05), except the condition - ['pregnant'] and ['cardiovascular']. The result as follows:
![Statistical_Analysis_in_R](./Image/Statistical_Analysis_in_R.png)
<br> So preliminarily, the features are relevant to the target. Even though ['pregnant'] and ['cardiovascular'] didn't appear significant to the target ['Death'], we are still going to proceed with them as they would be valuable info for the doctors to prepare further diagnosis and treatment.

## Machine Learning Analysis
After data preprocessing and preliminary feature engineering, we are ready to fit the data into the machine learning models. 
<br> As we figure, the class of '1' accounts for only 11% of the entire dataset, we are focusing on the techiniques and models that can handle the impact of the imbalanced dataset well.

<br> Here's the scope of the machine learning analysis:
<br> We are trying to compare the balanced accuracy score and false negative cases in the combination of following parameters:

- Targets: ['DEATH']
- Features: ['gender','pneumonia', 'new_age','pregnant', 'diabetes', 'copd','asthma', 'immunosup', 'hypertension','cardiovascular', 'obesity', 'renal_chronic', 'tobacco', 'another_complication','closed_contact']
- Resampling techniques: SMOTE vs SMOTEENN
- Machine Learning models: 
    - Logistic Regression Classifier
    - Support Vector Machines (SVM)
    - Gradient Boosting Classifier
    - Decision Tree Classifier
    - Random Forest Classifier
    - Balanced Random Forest Classifier
    - Easy Ensemble Classifier
    - Deep Learning


### Data split for Machine Learning training and testing Purpose
