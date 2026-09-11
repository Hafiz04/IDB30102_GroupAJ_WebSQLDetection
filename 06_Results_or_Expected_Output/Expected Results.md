# Expected Results / Expected Output

## Research Title

Detecting SQL Injection Attacks in Web Environments Using an Ensemble Learning Approach


## Expected System Outcome

This research is expected to develop an SQL Injection detection prototype using an Ensemble Learning approach that combines Random Forest and XGBoost classifiers with SQL query preprocessing techniques.

The proposed system aims to improve SQL Injection detection capability by analysing SQL query patterns and classifying inputs into normal queries and malicious attack payloads.


# 1. Expected SQL Injection Detection Performance

The proposed Ensemble Learning model is expected to provide effective detection performance by combining multiple machine learning classifiers.

The performance of the model will be evaluated using:

| Evaluation Metric | Purpose |
|---|---|
| Accuracy | Measures overall classification performance |
| Precision | Measures correctly identified SQL Injection attacks |
| Recall | Measures ability to detect actual attacks |
| F1-Score | Measures balance between precision and recall |
| False Positive Rate | Measures incorrect attack detection |


# 2. Expected Detection of Obfuscated SQL Injection Attacks

The proposed preprocessing module is expected to improve detection capability against modified SQL Injection payloads.

The system will analyse different SQL query structures including:

- Modified query formats
- Special characters
- Different query patterns
- Payload variations


# 3. Expected Reduction of False Positive Results

The Ensemble Learning approach is expected to improve classification reliability by combining predictions from multiple classifiers.

The expected outcome includes:

- Better separation between normal and malicious queries.
- Reduced incorrect attack classification.
- Improved reliability for web security applications.


# 4. Expected System Workflow

The proposed prototype will follow these steps:

1. Receive SQL query input.
2. Perform data preprocessing.
3. Extract features using TF-IDF.
4. Apply Random Forest and XGBoost classifiers.
5. Generate final classification result.


Example:

Input Query:

' OR '1'='1


Expected Output:

Prediction:
SQL Injection Attack Detected

Classification:
Malicious Query


# 5. Expected Research Contribution

This research is expected to contribute by:

- Providing an Ensemble Learning approach for SQL Injection detection.
- Improving automated detection of malicious SQL queries.
- Demonstrating the application of machine learning techniques in web security.
- Providing supporting research for future Web Application Firewall (WAF) improvements.


# Overall Expected Outcome

Overall, the proposed research is expected to demonstrate that Ensemble Learning can be applied as an effective approach for detecting SQL Injection attacks while maintaining suitable computational efficiency
