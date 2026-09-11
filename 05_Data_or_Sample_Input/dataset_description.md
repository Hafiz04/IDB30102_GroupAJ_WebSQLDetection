# SQL Injection Dataset Description

## Dataset Overview

This dataset contains sample SQL query inputs used for SQL Injection detection research and prototype development.

The dataset is prepared to support the development of an Ensemble Learning-based SQL Injection detection system.

The main purpose of this dataset is to classify SQL queries into two categories:

- Normal SQL Query
- SQL Injection Attack


---

## Dataset Label Classification

The dataset uses a binary classification label system.

| Label | Category | Description |
|---|---|---|
| 0 | Normal SQL Query | Legitimate SQL query without malicious intention |
| 1 | SQL Injection Attack | Malicious SQL query designed to manipulate database operations |


---

## Dataset Attributes

The dataset contains two main columns:

| Attribute | Description |
|---|---|
| query | Contains SQL query statements or input strings |
| label | Represents the classification category of the query |


---

## Sample Data Example

### Normal SQL Query

Example:
