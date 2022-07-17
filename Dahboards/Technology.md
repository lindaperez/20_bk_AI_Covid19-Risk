# Technologies Used
## Data Cleaning and Analysis
- <strong>Python, including Pandas,Matplotlib,etc. </strong> will be used to clean the data, perform an exploratory analysis and plot the data. 
- <strong>R</strong> will be used to perform statistical analysis to figure out the significance level and p value of hypothesis attributing the features to the target result.

## Database Storage
- <strong>AWS</strong> is the database we intend to use, and we will integrate <strong>Tableau</strong> to visualize the data.
[**Detail Database Environment Setting**](https://github.com/lindaperez/bk-covid19/blob/5bd45b69571221eb52bc8112af03995194ef379a/provisional_data/database_storage.md)

## Machine Learning
- <strong>SciKitLearn</strong> and <strong>TensorFlow</strong> are the Machine Learning libraries we'll be using to create a classifier. We will be creating and comparing different machine learning models over the COVID patient dataset. Training and testing details as follows:
    - Class: define "High Risk Patient" and "Low Risk Patient" by either one of the result: "date_patient_death", "intubated", "icu", "type_patient_Hospitalized"
    - Features: underlying medical conditions and other features including: 'gender', 'pneumonia', 'age', 'pregnant', 'diabetes', 'copd', 'asthma', 'immunosup', 'hypertension','cardiovascular', 'obesity', 'renal_chronic', 'tobacco';
    - Train/Test percentage: default training on 75% of the dataset and test the machine learning model performance on 25% of the dataset;
    - Normalization/Standardization/Encoding: using StandardScaler(), OneHotEncoder() to preprocess the datasets for ML models
    - Machine Learning Models: Logistic Regression, Support Vector Machine(SVM), GradientBoost Tree, Easy Ensemble Learning, Neural Network/Deep Learning model;
    - Resampling techniques: undersampling, oversampling and SMOTEENN for imbalanced result dataset;
    - Evaluation: using "Accuracy Score"/"balanced_accuracy_score", "classification_report"/"classification_report_imbalanced"
    - Goal of model performance: Accuracy score between 91 - 95%
    - Feature Importance Exploration: using Machine Learning model's built-in function ".feature_importances_" to get insights of feature importances.

## Visualization and Deployment
In addition to using <strong>Tableau</strong> for dashboards, we are going to use <strong>JavaScript, CSS, and HTML</strong> to create an interactive function helping users get an understanding of the risk level when exposed to COVID, based on the best-performing Machine Learning Model of the project analysis. 

