# Tata iQ – GenAI Powered Data Analytics & Risk Strategy

## Project Overview
This project was completed as part of the **Tata iQ GenAI Powered Data Analytics Job Simulation** on Forage. Serving in the role of an **AI Transformation Consultant**, the engagement focused on diagnosing credit card delinquency drivers for **Geldium Finance**, designing an explainable predictive model, and architecting an ethical, agentic AI collections framework.

---

## Repository Structure
```text
├── data/          # Cleaned customer demographic and credit performance data
├── notebooks/     # Exploratory data analysis, data quality checks, and risk scoring
├── reports/       # Executive stakeholder report and AI intervention strategy
├── src/           # Modular Python preprocessing and scoring scripts
├── requirements.txt
└── README.md
```

---

## Workflow & Key Deliverables

1. **Exploratory Data Analysis & Data Quality Assessment (`01_exploratory_data_analysis.ipynb`)**
   - Profiled 600 customer records to detect anomalies, missing values, and high credit-utilization outliers.
   - Identified critical early indicators of delinquency (debt-to-income ratio, payment history trends, and credit utilization spikes).

2. **Predictive Modeling & Explainability Framework (`02_risk_modeling_and_explainability.ipynb`)**
   - Formulated a predictive model strategy prioritizing explainable algorithms (Logistic Regression) to comply with financial lending regulations.
   - Evaluated model using **ROC-AUC (0.88+)**, Precision, Recall, and confusion matrix.
   - Standardized feature coefficients directly illustrate risk impact for regulatory compliance.

3. **Executive Stakeholder Report & Actionable Interventions (`reports/`)**
   - Synthesized analytical findings into a structured report for the Head of Collections.
   - Developed targeted intervention workflows (proactive restructuring, flexible repayment schedules) based on segmented risk tiers.

4. **Autonomous AI Collections Architecture & Ethics**
   - Designed a high-level system framework incorporating agentic AI for automated, personalized customer outreach.
   - Integrated strict Ethical AI guardrails: fairness monitoring, demographic parity checks, and automated human-in-the-loop review triggers for vulnerable accounts.

---

## Setup & Reproduction
```bash
git clone https://github.com/riyaz2018786/tata-genai-data-analytics.git
cd tata-genai-data-analytics
pip install -r requirements.txt
```
