# Risk Assessment of Publicly Available Health Datasets

## Course Information

*DPI 617 : Law, Order, and Algorithms*

*Spring 2024*

## Research Question
As time passes, more data gets released for general use. Consequently, the feasibility of malicious actors deanonymizing aggregated data rises dangerously. What is the quantifiable risk to individuals when health information of varying anonymization is published? Can we develop an effective risk and privacy algorithm to measure that risk? What protections, legal and otherwise, fail to keep re-identification at bay? 


## Team Members
|             |         |                 |
| ----------- | ------- | --------------- |
| [Sudhan Chitgopkar](mailto:sudhanchitgopkar@g.harvard.edu) | Harvard | MS CSE |
| [Abigail Kinaro](mailto:akinaro@g.harvard.edu) | Harvard | MS Data Science |
| [Hope Neveux](mailto:hopeneveux@g.harvard.edu) | Harvard | MS Data Science |
| [Helen Webley-Brown](mailto:helenwb@mit.edu) | MIT | PhD Political Science|

## Methodology

1. Locate currently available health datasets, focusing on mental health if possible. 
Privacy Risk Assessments and Anonymity and De-Identification Assessments are often performed to express the privacy concerns we are interested in. 
2. Consider the features available and their granularity. Different features are pre-identified to be more personal and riskier than others. This is a take on attribution analysis.
3. Assess privacy risk through unique identifiers, rare or unusual attributes, or combinations of attributes that become within themselves PII. We can also look very closely for outliers, patterns, and atypical correlations, as these individuals are always at higher risk of re-identification. 
4. Formally assign a risk score to the dataset even as 3rd-party onlookers.

## Potential Impact

- Shed light on the status quo of publicly available health data and dangers of publishing open-source health datasets, and the need for limited access even when published.
- Design a risk assessment algorithm that considers both Privacy Risk Assessment and Anonymity And De-Identification Assessment methodologies to produce a concrete number on risk. 
- Explore the implications of personal information breaches in various aspects of a person’s life.
- Propose guidance on the choice of epsilon in Differential Privacy methods or enhance methods for anonymization (should time permit)
Understand where legal protections fail and suggest ways to patch common loopholes if they exist.
- Highlight variation in state-level policies to protect sensitive health data and how this interacts with inertia in federal-level policymaking. This may particularly interest reproductive health organizations following the 2022 Supreme Court ruling on *Dobbs v Jackson*. Post-Roe, there have been increased concerns about privacy protections for reproductive health data and how data brokers and law enforcement may use health data to prosecute individuals.
