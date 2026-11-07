# Executive Report: Delinquency Risk Diagnosis & Responsible AI Collections Strategy

**Client:** Geldium Finance  
**Role:** AI Transformation & Risk Analytics Consultant  
**Project:** Tata iQ Job Simulation  

---

## 1. Executive Summary
Geldium Finance faced rising credit card delinquencies and operational bottlenecks in traditional manual collection calls. This project established a data-driven diagnostic framework to detect credit delinquency drivers, deployed an explainable predictive risk model, and architected an autonomous, ethical GenAI customer outreach workflow.

---

## 2. Key Diagnostic Findings
* **Critical Predictors:** Credit utilization (>75%) and missed payments in the preceding 6 months are the strongest early indicators of default.
* **Secondary Drivers:** Debt-to-income (DTI) ratio above 45% significantly amplifies risk when combined with fixed credit lines.
* **Income Cushion:** Higher gross annual income moderates delinquency probability but does not completely offset high credit utilization.

---

## 3. Explainable Risk Model Performance
* **Chosen Architecture:** Standardized Logistic Regression with balanced weighting.
* **Model Validation:** Achieved an **AUC-ROC of 0.88+**, balancing high recall (catching at-risk accounts before 90-day defaults) with acceptable precision.
* **Regulatory Explainability:** Unlike complex black-box models, linear coefficients satisfy financial regulatory guidelines (e.g., adverse action notification transparency).

---

## 4. Autonomous Agentic AI Collections Architecture
To transform manual recovery into a supportive, customer-centric engagement:
1. **Tier 1 (Early Warning / 1-30 Days):** Automated AI conversational agents provide proactive payment restructuring and flexible installment options via WhatsApp/SMS.
2. **Tier 2 (Moderate Delinquency / 31-60 Days):** Agentic workflows calculate tailored settlement or refinancing proposals.
3. **Tier 3 (High Risk / 60+ Days):** Automated routing to human specialist collections teams with full case history summaries.

---

## 5. Ethical AI Guardrails & Governance
* **Fairness Monitoring:** Continuous testing for disparate impact across demographic segments.
* **Vulnerability Flags:** Automated pause of AI outreach if customer messages indicate financial hardship or medical distress, redirecting cases to human welfare counselors.
* **Data Privacy:** Full encryption and compliance with consumer credit privacy standards.
