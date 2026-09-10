# Research Proposal for SQL Injection Detection using Ensemble Learning
### Repository Name: IDB30102_GroupAJ_WebSQLDetection

## Section A: Submission Details
* **Course Code and Name:** IDB30102 Research Methodology (BCSS)
* **Course Lecturer:** Dr. Delina Beh Mei Yin
* **Group Identifier:** Group AJ
* **Assigned Research Area:** Website Security (SQL Injection Detection, Payload Obfuscation, WAF Optimization)

### Project Metadata Tracker
* **Proposal Word Count:** 4,850 words (Compliant with < 5,000-word limit threshold)
* **AI In-Text Generation Ratio:** < 25% (Compliant with academic integrity standards)
* **Target Security Framework Baseline:** OWASP Web Security Testing Guide (WSTG v5)

### Project Matrix and Contribution Map

| Student Name | Student ID | Primary Technical Contribution |
| :--- | :--- | :--- |
| Adam Izzuddin Bin Rashidi | 52215125114 | Chapter 3 (Part A): Methodology Framework Selection, SDLC Model Customization, Architecture Diagram Blueprinting, System Flowchart Engineering, and Repository Structure Mapping. |
| Muhammad Hafiz Hakimi Bin Mazuki | 52215125763 | Chapter 2: Systematic Literature Review Synthesis, Thematic Identification Matrices, Critical Summary Table Formulation, and Research Gap Isolation. |
| Ahmad Fahmie Bin Mohd Khairy | 52215125925 | Chapter 1: Cybersecurity Introduction, Background of Study Contextualization, Problem Statements Isolation, Project Scope Boundaries, and Overall Document Integration. |
| Haziq Fahmi Bin Abd Aziz | 52215125155 | Chapter 3 (Part B): Data Collection Protocols, Hardware/Software Bed Constraints, Evaluation Metrics Execution, and Project Timeline/Gantt Chart Formulation. |
| Afiq Naqiuddin Bin Shafie | 52215125765 | Review and Quality Control: Content Consistency Verification, Payload Obfuscation Mapping, APA 7th Edition Reference Cross-Checking, and Git Log Compliance Management. |

---

## 1. Project Overview
### 1.1 Research Problem Statements
* **Problem Statement 1 (Vulnerability to Structural Obfuscation):** Classical signature-matching mechanisms and static Web Application Firewalls (WAFs) fail to detect highly obfuscated SQL Injection (SQLi) attacks. Attackers bypass rule vectors using multi-vendor syntax adjustments, hexadecimal string encoding, inline comment insertion, and whitespace manipulation. Classical machine learning systems rely on manual keyword counts that degrade rapidly when processing obfuscated dynamic variants.
* **Problem Statement 2 (Real-Time Edge Latency Contradiction):** While hybrid deep learning networks (e.g., CNN-LSTM) demonstrate high accuracy against complex sequential payloads, they generate severe computational processing overhead. These deep models require graphics processing hardware and introduce substantial inference latency, creating request processing bottlenecks that prevent their inline deployment in live, high-throughput production environments.

### 1.2 Research Aim and Measurable Objectives
The primary aim of this research is to design and develop an intelligent, high-performance SQL Injection detection prototype using an Ensemble Learning approach. This framework secures web application parameters against obfuscated payloads while maintaining low operational processing latency suitable for real-time edge filtering.

* **RO1:** To study and analyze existing SQL Injection attack patterns, structural evasion techniques, and public benchmark datasets (Kaggle SQLi Corpus and HTTP CSIC 2010) to establish a feature extraction baseline.
* **RO2:** To design, develop, and implement an Ensemble Learning detection prototype integrating parallel Random Forest and XGBoost classifiers with a robust structural tokenization preprocessing module.
* **RO3:** To test, validate, and evaluate the performance of the proposed ensemble framework using standard validation metrics (Accuracy, Precision, Recall, F1-Score, False Positive Rate) and processing latency metrics.

---

## 2. Research Methodology and Engineering Framework
### 2.1 Layer 1: Research Methodology Application
* **Selected Methodology:** Design Science Research Methodology (DSRM)
* **Justification Matrix:** DSRM is selected because the core contribution of this project is the conceptualization, deployment, and validation of a concrete technical artifact (an ensemble machine learning detection engine) designed to solve an operational system vulnerability. The framework maps to the 6-phase DSRM model:
  1. *Problem Identification:* Documented in Sections 1.3.1 and 1.3.2.
  2. *Objectives for a Solution:* Defining accuracy parameters (>98%) and sub-millisecond local processing bounds.
  3. *Design and Development:* Implementing the TF-IDF feature pipeline and voting algorithms in `04_Source_Code`.
  4. *Demonstration:* Deploying the script context inside a local, isolated virtual server sandbox environment.
  5. *Evaluation:* Conducting automated pipeline fuzzing using synthetically obfuscated query strings.
  6. *Communication:* Fulfilled via this GitHub repository documentation, the written report, and presentation media.

### 2.2 Layer 2: Software Development Lifecycle Model
* **Selected Model:** Evolutionary Prototyping Model
* **Justification Matrix:** Given the fixed timeline constraints of the research proposal phase, an evolutionary prototyping lifecycle enables the group to implement early exploratory parsing scripts and iteratively tune hyperparameter weights, vector distributions, and threshold boundaries without breaking downstream system modules.

---

## 3. System Architecture and Process Flow
Below are the finalized engineering layouts governing the execution parameters of the proposed web filtering pipeline.

### 3.1 Proposed System Architecture
<img width="626" height="787" alt="system_architecture" src="https://github.com/user-attachments/assets/57ef91c9-5695-4f25-9d23-d1c947700da1" />

### 3.2 System Flowchart
<img width="620" height="780" alt="system_flowchart" src="https://github.com/user-attachments/assets/746bedb6-a92e-409f-a530-87df383d448d" />

---

## 4. Technical Repository Structure and Objective Mapping
To guarantee technical traceability, all folders are organized according to the course brief and map directly back to the core Research Objectives:

* **`01_Research_Papers/` and `02_Literature_Review/` (Supports RO1):** Formulates the empirical foundation. Houses 50 peer-reviewed journal papers (2022–2026), the Systematic Literature Review matrix, the 5-theme analysis table, and the evidence-based research gap identification profiles.
* **`03_Architecture_and_Flowchart/` and `04_Source_Code/` (Supports RO2):** Holds the engineering blueprints and structural source files, including the string tokenizers, the TF-IDF feature vector extractors, and parallel classifier configuration scripts.
* **`05_Data_or_Sample_Input/` and `06_Results_or_Expected_Output/` (Supports RO3):** Hosts the evaluation verification infrastructure. Contains sample rows of benign web request strings, clean SQLi injection payloads, synthetically obfuscated test arrays, and the tracking metrics configuration logs.
* **`07_References/`:** Consolidated academic resource bibliography formatted strictly to the APA 7th Edition style manual.

---

## 5. Target Technical Stack and Compliance
### 5.1 Technology Architecture
* **Programming Core Language:** Python 3.10+
* **Feature Vectorization Engine:** Scikit-learn TF-IDF Vectorizer Module
* **Machine Learning Classifiers:** Scikit-learn Random Forest Classifier & XGBoost Open-Source Library
* **Natural Language Processing Assets:** Natural Language Toolkit (NLTK) Tokenizer
* **Baseline Validation Corpora:** Kaggle SQL Injection Dataset & HTTP CSIC 2010 Reference Database

### 5.2 Regulatory and Ethical Compliance Declaration
All technical execution scripts, mock injection data vectors, and evaluation fuzzing activities are conducted inside an isolated, local virtual development context. The research activities do not engage live production networks, real corporate environments, or private human user information, maintaining compliance with the **Malaysian Computer Crimes Act 1997** and the **Personal Data Protection Act (PDPA) 2010**.
