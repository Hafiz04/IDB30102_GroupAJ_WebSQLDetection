# Summary of Evaluation Metrics Used in SQLi Detection Research

| Metric | Definition | Why It Matters | Target for This Research |
|---|---|---|---|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | Overall performance measure | > 95% |
| **Precision** | TP / (TP + FP) | How many predicted attacks are real attacks | High |
| **Recall** | TP / (TP + FN) | How many actual attacks are detected | High |
| **F1-Score** | Harmonic mean of Precision and Recall | Balances precision and recall | High |
| **False Positive Rate (FPR)** | FP / (FP + TN) | How many benign requests are flagged as attacks | < 5% |
| **ROC-AUC** | Area under ROC curve | Model's ability to distinguish classes | High |
| **Processing Latency** | Time taken per request (ms) | Suitability for real-time deployment | < 30ms |
| **Detection Rate** | TP / (TP + FN) | Percentage of attacks detected | > 90% on obfuscated payloads |

---

## Common Baselines Used in Literature

| Baseline | Description | Reference |
|---|---|---|
| **ModSecurity (OWASP CRS)** | Traditional signature-based WAF | Industry standard |
| **SVM** | Classical machine learning baseline | Aburashed et al. (2024) |
| **Random Forest** | Classical machine learning baseline | Crespo-Martinez et al. (2023) |
| **CNN-LSTM** | Deep learning baseline | Panadiya & Singhal (2024) |
