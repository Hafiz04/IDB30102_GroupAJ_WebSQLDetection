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
## Theme 3: Lightweight Models for WAF Deployment

| Study | Method | Dataset | Key Finding | Limitation |
|---|---|---|---|---|
| Casmiry et al. (2025) | 1D-CNN, LMH-SA | Multi-vendor SQL datasets | Model footprint <2MB; optimized for edge proxies | Reduced accuracy on nested payloads |
| Li et al. (2025) | Lightweight edge models | Multi-vendor database traces | Handles multi-user concurrent connections | Slight reduction in contextual accuracy |

---
## Theme 4: NLP and Semantic Pipelines

| Study | Method | Dataset | Key Finding | Limitation |
|---|---|---|---|---|
| Bakir (2025) | Word2Vec, FastText | Word/Sentence SQL Corpora | Detects hidden logical anomalies | Massive computational demand |
| Tasdemir et al. (2023) | Cascaded NLP | High-speed data center logs | Preserves positional relationships in queries | High processing overhead |
| Zulu et al. (2024) | BERT Fine-Tuning, RoBERTa | Benchmark datasets | Identifies malicious tautologies in legitimate text | Sensitive to vocabulary changes |

---

## Theme 5: Adversarial Evasion and Automated Testing

| Study | Method | Dataset | Key Finding | Limitation |
|---|---|---|---|---|
| Dasari et al. (2025) | VAE, CWGAN-GP | Synthetic SQL payloads | Proactive structural defense | High architectural training complexity |
| Yang et al. (2024) | Automated testing frameworks | Firewall configurations | Dynamic vulnerability testing | Complex hyperparameter tuning |
| Floris et al. (2025) | Generative augmentation | Synthetic target generation | Resilient against rule-bypass strategies | Risk of overfitting to synthetic parameters |
