# Research Gap Analysis

## SQL Injection Detection Using Machine Learning

Based on the synthesis of 50 reviewed studies (2022-2026), the following research gaps have been identified:

---

### Gap 1: Limited Detection Capability Against Obfuscated SQLi Payloads

**Evidence from Literature:**
- Crespo-Martinez et al. (2023) noted a sharp drop in detection accuracy on heavily obfuscated payloads.
- Aburashed et al. (2024) confirmed that classical models struggle with advanced structural obfuscation.
- Classical ML models rely on manually engineered features that are easily disrupted by encoding, comment insertion, and structural changes.

**Impact:**
Attackers can modify malicious queries to bypass detection mechanisms, leaving web applications vulnerable.

**How This Research Addresses the Gap:**
This research proposes a structural preprocessing module designed to counter obfuscation techniques before feature extraction.

---

### Gap 2: Computational Trade-off in Detection Models

**Evidence from Literature:**
- Panadiya & Singhal (2024) noted that CNN-LSTM architectures require dedicated GPU resources.
- Tadhani et al. (2024) highlighted the high computational overhead of hybrid models.
- Deep learning models provide superior detection but introduce significant latency, making them impractical for real-time WAF deployment.

**Impact:**
Organisations face a choice between high accuracy (slow) and low latency (less accurate).

**How This Research Addresses the Gap:**
This research proposes an Ensemble Learning approach that combines multiple classifiers to achieve high accuracy while maintaining low latency.

---

### Gap 3: Limited Research on Ensemble Approaches Specifically for SQLi Detection

**Evidence from Literature:**
- Ensemble methods are well-established in other cybersecurity domains (intrusion detection, malware classification).
- Limited research has applied ensemble methods specifically to SQLi detection with a focus on obfuscated payloads.

**Impact:**
The full potential of ensemble methods for SQLi detection has not been explored.

**How This Research Addresses the Gap:**
This research contributes new knowledge on the application of ensemble methods (Random Forest + XGBoost) to SQLi detection, particularly for obfuscated payload detection.

---

### Summary of Research Gaps Addressed

| Gap | Description | Proposed Solution |
|---|---|---|
| Gap 1 | Vulnerability to obfuscated payloads | Structural preprocessing module |
| Gap 2 | Accuracy vs. latency trade-off | Ensemble Learning approach |
| Gap 3 | Limited ensemble research for SQLi | Novel application of ensemble methods |
