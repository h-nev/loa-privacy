# Risk Assessment of Public Criminal Rescords

## Table of Contents

- [Course Information](#course-information)
- [Research Question](#research-question)
- [Team Members](#team-members)
- [Methodology](#methodology)
- [Potential Impact](#potential-impact)
- [Datasets](#datasets)
- [Repo Structure](#repo-structure)
- [Running the File Auto-Scan Method](#running-the-file-auto-scan-method)
- [Running All Data Files at Once](#running-all-data-files-at-once)

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

## Datasets & Supplemental Data

- [Illinois Parole](https://corrections.il.readydata.org/parole-dashboard)
  - [Parole Registary](https://prb.illinois.gov/content/dam/soi/en/web/prb/documents/parole-registry/Regparda.pdf)
- [NYC Arrests](https://data.cityofnewyork.us/Public-Safety/NYPD-Arrest-Data-Year-to-Date-/uip8-fykc/data_preview)
- [Dallas Arrests](https://www.dallasopendata.com/Public-Safety/Police-Arrests/sdr7-6v3j/about_data)
- [Seattle Arrests](https://data.seattle.gov/Public-Safety/SPD-Crime-Data-2008-Present/tazs-3rd5/about_data)
- [Los Angeles Arrests](https://data.lacity.org/Public-Safety/Arrest-Data-from-2020-to-Present/amvf-fr72/about_data)
- [San Diego Arrests](https://data.sandiegodata.org/dataset/arjis-org-crime-victims-pra/)
- [Atlanta Arrests](https://opendata.atlantapd.org/)
- [Cambridge Crime](https://data.world/data-society/cambridge-crime-data-2009-2016)
- [Baltimore Crime](https://data.world/baltimore/baltimore-crime-data)
- [Hatford Crime](https://data.world/johnsnowlabs/hartford-police-incident-reports)
- [Kansas City Crime](https://data.world/data-society/kansas-city-crime-data)
- [Louisville Metro Crime](https://catalog.data.gov/dataset/louisville-metro-ky-crime-data-2022)
- [Detroit Crime](https://data.world/johnsnowlabs/detroit-all-crime-incidents)
- [Nashville](https://openpolicing.stanford.edu/data/)


## Repo Structure

```
.
  |-requirements.txt
  |-archive
  |  |-MHCLD.ipynb
  |  |-chicago.ipynb
  |-Makefile
  |-runall.sh
  |-__pycache__
  |  |-pii.cpython-312.pyc
  |-README.md
  |-.gitignore
  |-dev
  |  |-filescan.ipynb
  |  |-readpdf.ipynb
  |-data
  |  |-SeattleArrests.csv
  |  |-NYPD_Arrest_Data__Year_to_Date__20240410.csv
  |  |-Illinois_parole_reg.pdf
  |  |-README.md
  |  |-Parole pop subset.xlsx
  |  |-LAArrests.csv
  |  |-DallasArrests.csv
  |  |-AtlantaArrests.csv
  |  |-SanDiegoArrests.csv
  |-tree.txt
  |-pii.py
  |-reports
  |  |-chicagoParole_report.txt
  |  |-Parole pop subset_report.txt
  |  |-LAArrests_report.txt
  |  |-AtlantaArrests_report.txt
  |  |-SanDiegoArrests_report.txt
  |  |-NYPD_Arrest_Data__Year_to_Date__20240410_report.txt
  |  |-DallasArrests_report.txt
  |  |-SeattleArrests_report.txt
```

## Running the File Auto-Scan Method

### 0. Enviornment Setup

To make sure everything runs, make sure that all the requirements are installed. If you are using a python venv, make sure this is activated first. Then run:

```
pip install -r requirements.txt
```

### 1. Save CSV or XLSX Files Locally 

You can say the data anywhere locally that makes sense. In this example, we save the `chicagoParole.csv` file to the `data` folder.

>CAUTION:
>
> Please **do not** commit any csv or xlsx files to the repo.

### 2. Run the `pii.py` Script

We can run the script two ways. The first option will use the default options for the roots, which will look for any features that contain any of the following words:

- Name
- Date
- Time
- Address
- Street
- Residence
- Country
- County
- State
- District
- Code
- Number
- Age
- Ethnicity
- Gender
- Occupation
- Status
- DOB
- Year
- Month
- Day

When running either of the options below, the report will both print to the console *as well as make a txt file containing the report located in the `reports` folder*. 

#### Option 1: Default Roots

```{python}
>> python pii.py "data/chicagoParole.csv"

 File: chicagoParole 
 File Type: csv 
 Features: 30 
 Records: 15630 

 Possible PII Matches: 12 
 Hit Rate: 0.4 

 Possible Matches: ['Age', 'County of Residence', 'Current Admission Date', 'Custody Date', 'Date of Birth', 'MSR/Parole Date', 'Name', 'Projected Discharge Date', 'Residence Zip Code', 'Sentence Date', 'Sentencing County', 'Veteran Status'] 
 Keyword List: ['name', 'date', 'time', 'address', 'street', 'residence', 'country', 'county', 'state', 'district', 'code', 'number', 'age', 'ethnicity', 'gender', 'occupation', 'status', 'dob', 'year', 'month', 'day']
```

#### Option 2: Custom Roots

```{python}
>> python pii.py "data/chicagoParole.csv" "['name', 'date']"

 File: chicagoParole 
 File Type: csv 
 Features: 30 
 Records: 15630 

 Possible PII Matches: 7 
 Hit Rate: 0.23 

 Possible Matches: ['Current Admission Date', 'Custody Date', 'Date of Birth', 'MSR/Parole Date', 'Name', 'Projected Discharge Date', 'Sentence Date'] 
 Keyword List: ['name', 'date']
```
## Running all Data Files at Once

With a lot of datasets or chnages to the `pii.py` method, it would be tedious to do it all by hand. To run the default `pii.py` (using the default roots / keywords), run the following in terminal.

```{bash}
bash runall.sh
```

The output for each is directed to the `reports` folder as normal.  