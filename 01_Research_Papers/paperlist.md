# Research Papers for SQL Injection Detection

This document lists the key research papers used to support the Literature Review (Chapter 2) of the Research Proposal.

---

## Paper 1

| **Item** | **Details** |
|---|---|
| **Paper Title** | SQL injection attack detection in network flow data |
| **Author(s)** | Crespo-Martinez, I. S., Campazas-Vega, A., Guerrero-Higueras, A. M., Riego-DelCastillo, V., Álvarez-Aparicio, C., & Fernández-Llamas, C. |
| **Year** | 2023 |
| **Research Problem** | Detecting SQL injection attacks in network flow data using machine learning |
| **Method / Technique** | Random Forest, Logistic Regression, SVM |
| **Dataset / Tools** | NetFlow traffic data |
| **Main Findings** | Achieved over 97% detection with false-alarm rate below 0.07% |
| **Limitation** | Vulnerable to advanced structural obfuscation |
| **Relevance to Proposed Research** | Demonstrates that ensemble models (Random Forest) outperform standalone classifiers, supporting our choice of ensemble learning |

---

## Paper 2

| **Item** | **Details** |
|---|---|
| **Paper Title** | Advanced detection and prevention of SQL injection attacks using machine learning techniques for enhanced web security |
| **Author(s)** | Panadiya, P., & Singhal, M. K. |
| **Year** | 2024 |
| **Research Problem** | Detecting SQL injection attacks using hybrid deep learning models |
| **Method / Technique** | CNN-LSTM hybrid model |
| **Dataset / Tools** | HTTP CSIC 2010 database |
| **Main Findings** | Achieved over 99% accuracy; maintained false-positive rate under 0.8% |
| **Limitation** | High computational overhead; requires GPU for inference |
| **Relevance to Proposed Research** | Highlights the trade-off between accuracy and computational cost, which our ensemble approach aims to balance |

---

## Paper 3

| **Item** | **Details** |
|---|---|
| **Paper Title** | Securing web applications against XSS and SQLi attacks using a novel deep learning approach |
| **Author(s)** | Tadhani, J. R., Vekariya, V., Sorathiya, V., Alshathri, S., & El-Shafai, W. |
| **Year** | 2024 |
| **Research Problem** | Detecting XSS and SQL injection using deep learning |
| **Method / Technique** | CNN-LSTM with Word2Vec tokenization |
| **Dataset / Tools** | HTTP CSIC 2010, public GitHub SQLi repositories |
| **Main Findings** | Achieved over 99% accuracy across multiple repositories |
| **Limitation** | High computational resources required |
| **Relevance to Proposed Research** | Shows the effectiveness of hybrid models while confirming the latency challenge we aim to solve |

---

## Paper 4

| **Item** | **Details** |
|---|---|
| **Paper Title** | Enhanced SQL injection detection using chi-square feature selection and machine learning classifiers |
| **Author(s)** | Casmiry, M., Mduma, N., & Sinde, R. |
| **Year** | 2025 |
| **Research Problem** | Lightweight SQL injection detection for WAF deployment |
| **Method / Technique** | 1D-CNN, Lightweight Multi-Head Self-Attention |
| **Dataset / Tools** | Multi-vendor dynamic SQL datasets |
| **Main Findings** | Reduced model footprint to under 2MB; optimized for edge proxy engines |
| **Limitation** | Reduced contextual accuracy on long/nested payloads |
| **Relevance to Proposed Research** | Demonstrates the accuracy-speed trade-off in lightweight models, which our ensemble approach addresses |

---

## Paper 5

| **Item** | **Details** |
|---|---|
| **Paper Title** | Enhancing SQL injection detection and prevention using generative models |
| **Author(s)** | Dasari, N. S., Badii, A., Moin, A., & Ashlam, A. |
| **Year** | 2025 |
| **Research Problem** | Improving SQLi detection robustness using adversarial training |
| **Method / Technique** | Generative Augmentation (VAE, CWGAN-GP) |
| **Dataset / Tools** | Synthetic SQL payload blends |
| **Main Findings** | Proactive structural defense; prioritizes vulnerability tests against dynamic rule bypass |
| **Limitation** | High architectural training complexity; risk of model overfitting |
| **Relevance to Proposed Research** | Informs our approach to handling obfuscated payloads and adversarial evasion |
