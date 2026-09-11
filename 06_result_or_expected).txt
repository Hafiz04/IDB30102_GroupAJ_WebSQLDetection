Expected Results / Expected Output

This research is expected to develop a more effective SQL Injection (SQLi) detection system by using an ensemble machine learning approach that combines Random Forest and XGBoost with a structural preprocessing module. The proposed approach aims to improve detection accuracy while maintaining faster processing performance compared with complex deep learning models.

1. Improved SQL Injection Detection Performance

The proposed model is expected to achieve better detection performance compared with individual machine learning algorithms. By combining multiple classifiers, the model can analyse different characteristics of SQL queries and make more accurate decisions.

The expected performance of the proposed model is:

Evaluation Metric	Expected Result
Accuracy	Above 95%
Precision	High precision in identifying malicious queries
Recall	High ability to detect actual SQL injection attacks
F1-Score	Balanced performance between precision and recall
False Positive Rate	Below 5%

This improvement is expected because ensemble learning allows different models to work together, reducing the weaknesses of individual classifiers.

2. Improved Detection of Obfuscated SQL Injection Attacks

One of the main challenges in SQL injection detection is handling obfuscated payloads, where attackers modify the structure of malicious queries to avoid detection. The proposed structural preprocessing module is expected to improve the ability of the system to recognize these modified attack patterns.

For example, attackers may use techniques such as:

Adding comments inside SQL commands.
Changing uppercase and lowercase characters.
Using encoding methods.
Modifying spaces and query structures.

By normalizing and analysing these patterns before classification, the proposed system is expected to detect a wider range of SQL injection attacks compared with traditional approaches.

3. Reduction of False Positive Results

The proposed system is also expected to reduce false positive detection, where legitimate user requests are incorrectly identified as attacks.

By combining Random Forest and XGBoost predictions, the system can make more reliable decisions before blocking a request. This can help prevent unnecessary blocking of normal users while maintaining strong protection against malicious activities.

The expected outcome is:

More accurate classification of normal and malicious queries.
Improved reliability for real-world web application security.
Reduced disruption to legitimate users.
4. Better Balance Between Accuracy and Processing Speed

Although deep learning models such as CNN-LSTM can achieve very high accuracy, they usually require more computational resources and longer processing time. The proposed ensemble approach aims to provide a balance between detection performance and efficiency.

The expected result is that the proposed model can achieve high detection accuracy while maintaining low processing latency, making it more suitable for real-time web application protection.

The expected processing time is:

Less than 30 milliseconds per SQL query.

5. Development of a SQL Injection Detection Prototype

The research is expected to produce a prototype system that can analyse incoming SQL queries and classify them as either normal or malicious.

The system workflow will include:

Receiving user input or HTTP request data.
Performing structural preprocessing to normalize SQL queries.
Extracting important features from the query.
Applying Random Forest and XGBoost classifiers.
Generating the final prediction result.

Example output:

Input Query:

username='admin' OR 1=1--

System Result:

Prediction: SQL Injection Attack Detected
Confidence Level: 98%
Action: Block Request
6. Expected Research Contribution

This research is expected to contribute to the field of web security by providing:

A more robust SQL injection detection approach that can handle obfuscated attacks.
An ensemble machine learning framework that improves detection reliability.
A lightweight alternative to computationally expensive deep learning approaches.
A practical solution that can potentially be integrated into Web Application Firewall (WAF) systems.
Overall Expected Outcome

Overall, the proposed research is expected to demonstrate that an ensemble learning approach can provide effective SQL injection detection with high accuracy, lower computational requirements, and better resistance against evolving attack techniques.
