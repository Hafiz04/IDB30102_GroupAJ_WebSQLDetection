# Research Proposal for SQL Injection Detection using Ensemble Learning

### Repository Name: IDB30102_GroupAJ_WebSQLDetection

---

# Section A: Submission Details

* **Course Code and Name:** IDB30102 Research Methodology (BCSS)
* **Course Lecturer:** Dr. Delina Beh Mei Yin
* **Group Identifier:** Group AJ
* **Assigned Research Area:** Website Security (SQL Injection Detection)

---

# Project Metadata Tracker

* **Proposal Word Count:** Below 5,000 words
* **AI In-Text Generation Ratio:** Maintained according to academic integrity requirements
* **Target Security Framework Baseline:** OWASP Web Security Testing Guide (WSTG)

---

# Project Matrix and Contribution Map

# Project Matrix and Contribution Map

| Student Name | Student ID | Primary Technical Contribution |
| :--- | :--- | :--- |
| Muhammad Hafiz Hakimi Bin Mazuki | 52215125763 | Chapter 1: Introduction, Research Background, Research Problem Statements, Research Aim, Research Objectives, and Research Scope Development |
| Adam Izzuddin Bin Rashidi | 52215125114 | Chapter 3 (Part A): Research Methodology Selection, Design Science Research Methodology (DSRM) Application, System Architecture Design, Flowchart Development, and Repository Structure Planning |
| Afiq Naqiuddin Bin Shafie | 52215125765 | Chapter 3 (Part B): Dataset Preparation, Data Collection Procedures, SQL Injection Sample Input Management (`05_Data_or_Sample_Input`), Evaluation Metrics Design, and GitHub Data Management |
| Ahmad Fahmie Bin Mohd Khairy | 52215125925 | Expected Output Documentation, Preliminary Result Analysis, Performance Output Organisation, and Results Management (`06_Results_or_Expected_Output`) |
| Haziq Fahmi Bin Abd Aziz | 52215125155 | Reference Management, APA 7th Edition Citation Formatting, External Resource Documentation, Dataset Reference Management, and Repository References Organisation (`07_References`) |

---

# 1. Project Overview

## 1.1 Research Problem Statements

* **Problem Statement 1 (Detection Limitation Against SQL Injection Variations):**

Traditional SQL Injection detection methods such as signature-based detection and rule-based Web Application Firewalls (WAF) may have limitations when detecting new or modified SQL Injection attack patterns. Attackers can apply different payload structures, encoding methods and query modifications to bypass existing detection rules.

* **Problem Statement 2 (Machine Learning Detection Performance Challenges):**

Existing machine learning approaches for SQL Injection detection may experience limitations when handling diverse attack patterns and maintaining effective detection performance. Therefore, an improved approach is required to enhance classification capability while reducing incorrect detection.

---

# 1.2 Research Aim and Objectives

The primary aim of this research is to design and develop an SQL Injection detection prototype using an Ensemble Learning approach for identifying malicious SQL queries in web environments.

## Research Objectives

* **RO1:** To study and analyse existing SQL Injection attack patterns, detection techniques and available datasets to establish a foundation for feature extraction.

* **RO2:** To design and implement an Ensemble Learning detection prototype integrating Random Forest and XGBoost classifiers with SQL query preprocessing techniques.

* **RO3:** To evaluate the performance of the proposed ensemble framework using suitable machine learning evaluation metrics.

---

# 1.3 Research Scope

This research focuses on detecting SQL Injection attacks in web environments using an Ensemble Learning approach.

The scope of this research includes:

- Analysis of SQL Injection attack patterns and payload structures.
- Preparation and preprocessing of SQL query datasets.
- Development of an Ensemble Learning detection prototype using Random Forest and XGBoost classifiers.
- Evaluation of model performance using classification metrics.

The research is limited to controlled experimental environments and publicly available datasets. No testing will be conducted on real production websites or unauthorized systems.

---

# 1.4 Significance of Study

This research contributes to improving web application security by exploring the application of machine learning techniques for SQL Injection detection.

The proposed Ensemble Learning approach may assist developers and security researchers in identifying malicious SQL queries more effectively compared to traditional rule-based detection methods.

The study also provides understanding of how machine learning techniques can support automated cybersecurity threat detection.

---

# 2. Research Methodology and Engineering Framework

## 2.1 Research Methodology Application

* **Selected Methodology:** Design Science Research Methodology (DSRM)

DSRM is selected because this research focuses on designing and evaluating a technical artifact, which is an Ensemble Learning based SQL Injection detection prototype.

The research process follows these phases:

1. Problem Identification  
2. Define Solution Objectives  
3. Design and Development  
4. Demonstration  
5. Evaluation  
6. Communication  

The methodology supports the development and validation of the proposed detection approach.

---

## 2.2 Software Development Lifecycle Model

* **Selected Model:** Evolutionary Prototyping Model

The Evolutionary Prototyping Model is selected because the proposed system requires iterative improvement of preprocessing methods, machine learning models and evaluation processes during the research development phase.

---

# 3. System Architecture and Process Flow

The proposed system architecture represents the workflow of the SQL Injection detection framework.

## 3.1 Proposed System Architecture

<img width="626" height="787" alt="system_architecture" src="https://github.com/user-attachments/assets/57ef91c9-5695-4f25-9d23-d1c947700da1" />


## 3.2 System Flowchart

<img width="620" height="780" alt="system_flowchart" src="https://github.com/user-attachments/assets/746bedb6-a92e-409f-a530-87df383d448d" />


---

# 3.3 Proposed Evaluation Plan

The proposed Ensemble Learning model will be evaluated based on classification performance.

## Evaluation Metrics

| Metric | Purpose |
|---|---|
| Accuracy | Measures overall classification correctness |
| Precision | Measures correctly detected SQL Injection attacks |
| Recall | Measures the ability to identify actual attacks |
| F1-Score | Provides balance between precision and recall |
| False Positive Rate | Measures incorrect attack detection |

## Testing Environment

- Programming Language: Python 3.10+
- Machine Learning Framework: Scikit-learn and XGBoost
- Feature Extraction: TF-IDF Vectorization
- Dataset: SQL Injection sample dataset and public benchmark datasets

---

# 4. Technical Repository Structure and Objective Mapping

The repository structure is organised according to the research objectives.

* **`01_Research_Papers/` and `02_Literature_Review/` (Supports RO1):**

Contains research papers, literature analysis and research gap identification related to SQL Injection detection and machine learning security approaches.

* **`03_Architecture_and_Flowchart/` and `04_Source_Code/` (Supports RO2):**

Contains system architecture diagrams, flowcharts, preprocessing scripts and Ensemble Learning implementation using Random Forest and XGBoost.

* **`05_Data_or_Sample_Input/` and `06_Results_or_Expected_Output/` (Supports RO3):**

Contains SQL query datasets, sample attack payloads, evaluation configuration and expected performance outputs.

* **`07_References/`:**

Contains academic references and external resources formatted according to APA 7th Edition style.

---

# 5. Target Technical Stack and Compliance

## 5.1 Technology Architecture

* **Programming Language:** Python 3.10+

* **Feature Extraction:** Scikit-learn TF-IDF Vectorizer

* **Machine Learning Classifiers:**
  - Random Forest Classifier
  - XGBoost Classifier

* **Data Processing:**
  - Pandas
  - NumPy

* **Evaluation Metrics:**
  - Accuracy
  - Precision
  - Recall
  - F1-Score


## 5.2 Regulatory and Ethical Compliance Declaration

All technical activities including dataset processing, model training and evaluation are conducted in a controlled research environment.

The research does not involve testing on real production systems, private user information or unauthorised networks.

The project follows ethical cybersecurity research practices and focuses only on defensive security improvement.

---

# Conclusion

This repository provides supporting materials for the research proposal entitled:

**"Detecting SQL Injection Attacks in Web Environments Using an Ensemble Learning Approach."**

The repository demonstrates the relationship between research problems, literature review, methodology, technical implementation and evaluation planning.
