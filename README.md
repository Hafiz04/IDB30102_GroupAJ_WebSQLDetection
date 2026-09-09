# Research Proposal for SQL Injection Detection using Ensemble Learning

## 👥 Group Details
* **Group Number:** Group AJ
* **Assigned Research Area:** Website Security (SQL Injection, XSS, CSRF, HTTPS, WAF)

| Student Name | Student ID | Primary Contribution |
| :--- | :--- | :--- |
| [Your Name] | [Your ID] | Chapter 3 (Part A): Methodology selection, Development Model, Architecture Diagram, System Flowchart, and Repository Organization. |
| Hafiz Hakimi Mazuki | Hafiz04 | Chapter 2: Literature Review, synthesis of previous studies, summary table, and research gap analysis. |
| [Member 3 Name] | [Member 3 ID] | Chapter 1: Introduction, Problem Statements, Research Objectives, Scope, and Significance. |
| [Member 4 Name] | [Member 4 ID] | Chapter 3 (Part B): Data Collection, Evaluation Plan, Timeline/Gantt Chart, and Expected Outcomes. |

---

## 📌 Project Overview
### 🔍 Research Problem
* **Problem 1 (Evasion Tactics):** Traditional signature-based Web Application Firewalls (WAFs) fail to detect heavily obfuscated SQL Injection (SQLi) attacks, leading to high false-negative rates.
* **Problem 2 (Model Reliability):** Single machine learning classifiers often suffer from high variance or over-fitting when dealing with dynamic and evolving web traffic payloads.

### 🎯 Research Aim & Objectives
The primary aim of this research is to propose an intelligent SQL Injection detection framework that leverages Ensemble Learning to improve detection accuracy and mitigate obfuscated attack patterns.
1. **RO1:** To study and analyze existing methods, techniques, and machine learning algorithms used for SQL Injection detection.
2. **RO2:** To design and develop an Ensemble Learning-based detection prototype and system architecture.
3. **RO3:** To evaluate and validate the detection performance of the proposed ensemble framework against a standard baseline payload dataset.

---

## ⚙️ Research Methodology & Engineering Framework
### Layer 1: Research Methodology
* **Selected Methodology:** **Design Science Research Methodology (DSRM)**
* **Justification:** DSRM is chosen because the core contribution of this project is the construction and evaluation of a novel technical artifact—specifically, an ensemble machine learning detection pipeline—designed to solve a concrete web vulnerability challenge [0.1.5, 0.1.72, source: 2].

### Layer 2: Development Model
* **Selected Model:** **Prototyping Model**
* **Justification:** Given the rigorous single-semester proposal structure, an evolutionary prototyping approach enables our team to design, evaluate, and incrementally refine the feature extraction and ensemble code models within the timeline.

---

## 🏗️ System Architecture & Process Flow
*Below is the engineering layout of our Web SQLi Detection pipeline.*

### Proposed System Architecture
![System Architecture](./03_Architecture_and_Flowchart/system_architecture.png)

### System Flowchart
![System Flowchart](./03_Architecture_and_Flowchart/system_flowchart.png)

---

## 🗂️ Repository Structure & Objective Mapping
This repository traceably maps our technical work directly back to our core **Research Objectives (RO1, RO2, RO3)**:

* 📂 **`01_Research_Papers/` & `02_Literature_Review/` (Supports RO1):** Formulates our comparison tables and details our research gap analysis.
* 📂 **`03_Architecture_and_Flowchart/` & `04_Source_Code/` (Supports RO2):** Holds our engineering blueprints, tokenization scripts, and ensemble classifier configurations.
* 📂 **`05_Data_or_Sample_Input/` & `06_Results_or_Expected_Output/` (Supports RO3):** Hosts our sample SQLi/Benign query logs, execution baselines, and evaluation metric charts.
* 📂 **`07_References/`:** Consolidated project resources formatted strictly to APA style standards.

---

## 🛠️ Target Technical Stack
* **Domain Standard to Cite:** OWASP Web Security Testing Guide (WSTG)
* **Programming Languages:** Python 3.x
* **Frameworks & Libraries:** Scikit-learn (Ensemble methods), Pandas, NumPy, NLTK (for string tokenization)
* **Datasets / Evaluation Metrics:** Modified Kaggle SQLi Dataset; measured via Precision, Recall, F1-Score, and False Positive Rate (FPR).
