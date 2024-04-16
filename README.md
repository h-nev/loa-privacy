# Risk Assessment of Public Criminal Records

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
As time passes, more data is released for general use. Consequently, the feasibility of malicious actors deanonymizing aggregated data rises dangerously. How can crime and arrest datasets be effectively anonymized and published online to safeguard individuals' privacy while maintaining transparency and accountability?

## Team Members
|             |         |                 |
| ----------- | ------- | --------------- |
| [Sudhan Chitgopkar](mailto:sudhanchitgopkar@g.harvard.edu) | Harvard | MS CSE |
| [Abigail Kinaro](mailto:akinaro@g.harvard.edu) | Harvard | MS Data Science |
| [Hope Neveux](mailto:hopeneveux@g.harvard.edu) | Harvard | MS Data Science |

## Methodology
1. Data Collection: Identify and locate crime and arrest datasets from various United States cities.
2. Identification of Identifiable Data: Create a checklist of the identifiable data elements and develop a script or program to systematically scan each dataset for the presence of these data elements.
3. Data Analysis and Reporting: Utilize the script to analyze the datasets, identify instances where the identifiable data elements are present, and generate a summarized report detailing the findings. 
4. Recommendations: Provide recommendations based on the analysis findings and the developed privacy checklist.
   
## Potential Impact
- Raise awareness about privacy risks for publishing crime and arrest datasets online. The developed checklist offers practical guidelines for data publishers and policymakers to ensure individuals' privacy rights are respected when sharing sensitive information.
- Promotes transparency and accountability in data-sharing practices by providing insights into identifiable data types in crime and arrest datasets. Stakeholders, including law enforcement agencies, government bodies, and advocacy groups, can use this information to advocate for responsible data-sharing policies and ensure that individuals' privacy is upheld.
-  Raises important ethical considerations surrounding the collection, use, and dissemination of sensitive personal information, particularly in the context of law enforcement data.

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
- [Nashville Stop Data](https://openpolicing.stanford.edu/data/)
- [Baltimore Arrests](https://data.baltimorecity.gov/datasets/619ec10c14b346f784a5a07bad4c43cd_0/explore?location=39.301657%2C-76.615850%2C12.19)
- [Phoenix Arrests](https://www.phoenixopendata.com/dataset/arrests/resource/1eaee7f1-ccd0-4057-af55-e5749a934258)
- [Philadelphia Stops](https://opendataphilly.org/datasets/vehicle-pedestrian-investigations/)
- [Denver Stops](https://www.denvergov.org/opendata/dataset/city-and-county-of-denver-police-pedestrian-stops-and-vehicle-stops)
- [Memphis Arrests](https://www.memphispolice.org/arrest-data-dashboard/)
- [Tuscon Arrests](https://gisdata.tucsonaz.gov/datasets/a2914a8afcfd442281c5b367ca36c987_0/explore?location=32.152038%2C-110.881858%2C9.85)


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

### 0. Environment Setup

To ensure everything runs, ensure all the requirements are installed. If you are using a Python venv, make sure this is activated first. Then run:

```
pip install -r requirements.txt
```

### 1. Save CSV or XLSX Files Locally 

You can say the data anywhere locally, which makes sense. In this example, we save the `chicagoParole.csv` file to the `data` folder.

>CAUTION:
>
> Please **do not** commit any csv or xlsx files to the repo.

### 2. Run the `pii.py` Script

We can run the script in two ways. The first option will use the default options for the roots, which will look for any features that contain any of the following words:

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

With a lot of datasets or changes to the `pii.py` method, it would be tedious to do it all by hand. To run the default `pii.py` (using the default roots / keywords), run the following in the terminal.

```{bash}
bash runall.sh
```

The output for each is directed to the `reports` folder as normal.  
