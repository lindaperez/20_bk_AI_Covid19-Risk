# Machine Learning Analysis Summary

We are trying to compare the balanced accuracy score and false negative cases in the combination of following parameters:
- Targets: 'DEATH', 'INTUBATION' and 'ICU' 
- Resampling techniques: SMOTE and SMOTEENN
- Machine Learning models: 
    - Logistic Regression Classifier
    - Support Vector Machines (SVM)
    - Gradient Boosting Classifier
    - Easy Ensemble Classifier
    - Deep Learning
and try to figure out the optimal combination to indicate the high risk to the potential patients effectively.

## Feature Importance Overview
By using Gradient Boosting Classifier, we can get following feature importance overview of each combination.
<br>Left: Old data; Right: New data including 'closed_contact' and 'another_complication'

### 'Death' as Target 
- SMOTEENN
<br>Old

![Death_SMOTEENN](./Image/Death_SMOTEENN.png)
<br>New

![Death_SMOTEENN_OP](./Image/Death_SMOTEENN_OP.png)  

- SMOTE
<br>Old

![Death_SMOTE](./Image/Death_SMOTE.png)
<br>New

![Death_SMOTE_OP](./Image/Death_SMOTE_OP.png)

### 'ICU' as Target
- SMOTEENN
<br>Old

![ICU_SMOTEENN](./Image/ICU_SMOTEENN.png)
<br>New

![ICU_SMOTEENN_OP](./Image/ICU_SMOTEENN_OP.png)

- SMOTE
<br>Old

![ICU_SMOTE](./Image/ICU_SMOTE.png)
<br>New

![ICU_SMOTE_OP](./Image/ICU_SMOTE_OP.png)

### 'Intubation' as Target
- SMOTEENN
<br>Old

![Intubation_SMOTEENN](./Image/Intubation_SMOTEENN.png)
<br>New

![Intubation_SMOTEENN_OP](./Image/Intubation_SMOTEENN_OP.png)

- SMOTE
<br>Old

![Intubation_SMOTE](./Image/Intubation_SMOTE.png)
<br>New

![Intubation_SMOTEENN_OP](./Image/Intubation_SMOTEENN_OP.png)

## Target_Resampling_Model Comparison
Here's an overview of balanced accuracy score and false negative cases under each combination.
![Target_Resampling_Model_Comparison](./Image/Target_Resampling_Model_Comparison.png)
