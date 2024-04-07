# Risk Assessment of Public Criminal Rescords

## Course Information

*DPI 617: Law, Order, and Algorithms*

*Spring 2024*

## Research Question
As time passes, more data is released for general use. Consequently, the feasibility of malicious actors deanonymizing aggregated data rises dangerously. What is the quantifiable risk to individuals when vehicle stop data from law enforcement with varying anonymization is published? Can we develop an effective risk and privacy algorithm to measure that risk? What protections, legal and otherwise, fail to keep re-identification at bay?

## Team Members
|             |         |                 |
| ----------- | ------- | --------------- |
| [Sudhan Chitgopkar](mailto:sudhanchitgopkar@g.harvard.edu) | Harvard | MS CSE |
| [Abigail Kinaro](mailto:akinaro@g.harvard.edu) | Harvard | MS Data Science |
| [Hope Neveux](mailto:hopeneveux@g.harvard.edu) | Harvard | MS Data Science |

## Methodology
1. Data Collection: Locate readily available vehicle stop data from law enforcement agencies.
2. Privacy Risk Assessment: Conduct Privacy Risk Assessments and Anonymity and De-Identification Assessments to evaluate the level of privacy risk associated with the published vehicle stop data. Identify sensitive attributes and assess the effectiveness of anonymization techniques used in the dataset.
3. Feature Analysis: Analyze the granularity of features within the dataset. Identify and evaluate features that may pose higher privacy risks to individuals, such as unique identifiers, demographic information, and location data.
4. Risk Score Assignment: Formally assign a risk score to the dataset, considering factors such as unique identifiers, rare attributes, and patterns that could lead to re-identification of individuals within the dataset.
   
## Potential Impact
- Shed light on the dangers of releasing open-source datasets without adequate privacy protections, emphasizing the need for caution and limited access to such sensitive information.
- Design a risk assessment algorithm that considers both Privacy Risk Assessment and Anonymity And De-Identification Assessment methodologies to produce a concrete number on risk. 
- Explore the implications of personal information breaches in various aspects of a person’s life.
- Propose guidance on enhancing privacy protections for vehicle stop data, including recommendations for improving anonymization techniques and implementing differential privacy methods. Address common loopholes in legal protections and suggest measures to mitigate re-identification risks.
- Highlight variations in state-level policies governing the protection of sensitive law enforcement data and their interaction with federal-level policymaking.

## Repo Structure

```
.
  |-filescan.ipynb
  |-requirements.txt
  |-archive
  |  |-MHCLD.ipynb
  |  |-chicago.ipynb
  |-Makefile
  |-README.md
  |-.gitignore
  |-data
  |  |-README.md
  |  |-Parole pop subset.xlsx
  |  |-Strategic_Subject_List_-_Historical_20240320.csv
  |  |-chicagoParole.csv
  |-tree.txt
  |-pii.py
```