# Evaluation Metrics


## Overview

The proposed Ensemble Learning model for SQL Injection Detection will be evaluated using several classification performance metrics.

These evaluation metrics are used to measure the ability of the model in distinguishing between normal SQL queries and SQL Injection attack payloads.


---

# 1. Accuracy

Accuracy measures the overall percentage of correctly classified samples from the total dataset.

It shows how many SQL queries are correctly identified by the proposed model.


Formula:

Accuracy = (True Positive + True Negative) / Total Samples


---

# 2. Precision

Precision measures the proportion of correctly detected SQL Injection attacks compared with all samples predicted as attacks.

A higher precision value indicates fewer false positive detections.


Formula:

Precision = True Positive / (True Positive + False Positive)


---

# 3. Recall

Recall measures the ability of the model to identify actual SQL Injection attacks.

A higher recall value indicates that the model can detect more malicious queries successfully.


Formula:

Recall = True Positive / (True Positive + False Negative)


---

# 4. F1-Score

F1-Score provides a balance between precision and recall.

It is useful when the dataset contains different numbers of normal and malicious SQL query samples.


Formula:

F1-Score = 2 × (Precision × Recall) / (Precision + Recall)


---

# 5. False Positive Rate (FPR)

False Positive Rate measures the number of normal SQL queries that are incorrectly classified as SQL Injection attacks.

A lower false positive rate indicates better classification reliability.


Formula:

False Positive Rate = False Positive / (False Positive + True Negative)


---

# Evaluation Environment

The proposed model evaluation will be conducted using:

- Programming Language: Python 3.10+
- Machine Learning Framework: Scikit-learn
- Ensemble Algorithm: Random Forest and XGBoost
- Feature Extraction Method: TF-IDF Vectorization
- Dataset: SQL Injection query dataset


---

# Expected Evaluation Outcome

The evaluation process is expected to demonstrate the effectiveness of the proposed Ensemble Learning approach in detecting SQL Injection attacks.

The results will be analysed based on:

- Detection capability
- Classification performance
- Error rate reduction
- Model reliability
