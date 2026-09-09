# Summary of Methods and Algorithms Identified from Previous Studies

## Classical Machine Learning

| Algorithm | Strengths | Weaknesses | Best Use Case |
|---|---|---|---|
| **Random Forest** | High accuracy, handles imbalanced data, interpretable | Vulnerable to obfuscation | General SQLi detection |
| **XGBoost** | Fast, high performance, handles missing values | Requires careful tuning | High-speed detection |
| **SVM** | Effective in high-dimensional spaces | Sensitive to parameter tuning | Smaller datasets |
| **Logistic Regression** | Simple, interpretable, fast | Limited capacity for complex patterns | Baseline comparison |

---

## Deep Learning

| Algorithm | Strengths | Weaknesses | Best Use Case |
|---|---|---|---|
| **CNN** | Automatic feature extraction, captures local patterns | Requires large datasets | Pattern-based detection |
| **LSTM** | Captures long-range dependencies | High computational cost | Sequence-based detection |
| **CNN-LSTM Hybrid** | Combines spatial and sequential features | Very high computational cost | Complex payload detection |
| **Transformer/BERT** | Semantic understanding, contextual | Massive resources required | Advanced NLP-based detection |

---

## Ensemble Methods

| Algorithm | Strengths | Weaknesses | Best Use Case |
|---|---|---|---|
| **Bagging (Random Forest)** | Reduces overfitting, handles noise | Less interpretable than single tree | General detection |
| **Boosting (XGBoost)** | High accuracy, handles complex patterns | Sensitive to outliers | Performance-critical applications |
| **Stacking** | Combines multiple models, high accuracy | Complex to implement | When high accuracy is critical |

---

## Lightweight Models

| Algorithm | Strengths | Weaknesses | Best Use Case |
|---|---|---|---|
| **1D-CNN (pruned)** | Small footprint, edge-ready | Reduced accuracy on complex payloads | WAF integration |
| **LMH-SA** | Low latency, optimized attention | Reduced contextual understanding | Edge proxy deployment |
