# Literature Review Analysis Table

## SQL Injection Detection Using Machine Learning (2022-2026)

This table summarizes the key findings from 50 peer-reviewed studies analyzed in the Systematic Literature Review (Assignment 1).

---
## Theme 1: Classical and Ensemble Machine Learning Classifiers

| Study | Method | Dataset | Key Finding | Limitation |
|---|---|---|---|---|
| Crespo-Martinez et al. (2023) | Random Forest, Logistic Regression, SVM | NetFlow traffic data | Achieved >97% detection with <0.07% false-alarm rate | Vulnerable to advanced structural obfuscation |
| Aburashed et al. (2024) | Random Forest, SVM, Logistic Regression | Kaggle SQLi Dataset | Ensemble models consistently outperform standalone classifiers | Relies on manual feature engineering |
| Michael Dass & Mohd Foozy (2022) | Random Forest, SVM | HTTP request logs | Random Forest outperforms SVM on imbalanced data | Brittle against zero-day payloads |

---
## Theme 2: Deep Learning Architectures (CNN/LSTM)

| Study | Method | Dataset | Key Finding | Limitation |
|---|---|---|---|---|
| Panadiya & Singhal (2024) | CNN-LSTM hybrid | HTTP CSIC 2010 | <0.8% false-positive rate; high detection on zero-day payloads | Requires GPU; high computational cost |
| Ghosh et al. (2024) | LSTM with lexical n-grams | HTTP CSIC 2010 | Outperforms traditional rule-based filters | High memory overhead during vectorization |
| Tadhani et al. (2024) | CNN-LSTM + Word2Vec | HTTP CSIC 2010, GitHub repositories | >99% accuracy across multiple repositories | Significant hardware requirements |

---
