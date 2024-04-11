import pandas as pd
import numpy as np
from pathlib import Path
import sys
import ast

class PIIScan():
    def __init__(self, filePath: str, pii = ['Name', 'Date', 'Time', 'Address', 'Street', 'Residence', 'Country', 'County', 'State', 'District', 'Code', 'Number', 'Age', 'Ethnicity', 'Gender', 'Occupation', 'Status', 'DOB', 'Year', 'Month', 'Day']):
        '''
        Reads a dataset (csv or xlsx supported) given a filepath, saves it and the metadata, and checks for partial or complete PII matches.

        Inputs:
            - (str) filePath: the relative or full path to the CSV or XLSX file
            - (list-like) pii: optional list of custom key words that we want to locate in the dataset features that may be PII. Default provided.

        Returns:
            - None. All information is saved to the object.

        Attributes Defined Here:
            - (str) filePath: The relative or full path to the data that was provided
            - (str) fileName: The name of the file minus the extension
            - (str) fileExtension: The extension name like 'csv' or 'xlsx'
            - (list: str) features: All column (feature) names
            - (list: str) roots: All key words that we assume are associated with PII (default provided)

        Attributes Defined Elsewhere:
            - (pd.DataFrame) df: Data stored in DataFrame format
            - (list: str) matches: List of unique column (feature) names that were found to be partial or complete matches to something in the PII list
            - (float) hitRate: Proportion of possibly PII columns in the dataset. Rounded to 2 decimal places)
            - (pd.Series) nan: Feature name and proportion of it's entries that are NAN
        '''
        
        # save the file path, name, and extension (mainly for report purposes)
        self.filePath = filePath
        self.fileName = Path(filePath).stem
        self.fileExtension = filePath.split('.')[-1]

        # get and save the data
        self._readFile()
        self.features = list(self.df.columns)

        # save the lowercase version of roots passed in or used from default
        self.roots = [root.lower() for root in pii]

        # check for PII hits
        print('Checking for PII Violations...')
        self._piiViolation()

        print('Reporting...\n')

        print(self)

    def __str__(self):
        return f' File: {self.fileName} \n File Type: {self.fileExtension} \n Features: {len(self.features)} \n Records: {len(self.df)} \n\n Possible PII Matches: {len(self.matches)} \n Hit Rate: {self.hitRate} \n\n Possible Matches: {self.matches} \n Keyword List: {self.roots}'

    def _readFile(self):
        '''
        Reads the datafile into a pandas DataFrame. Used in the initialization of the object.

        Inputs:
            - None

        Returns:
            - None

        Attributes Defined Here:
            - (pd.DataFrame) df: Data stored in DataFrame format
            - (pd.Series) nan: Feature name and proportion of it's entries that are NAN
        '''
        
        if self.fileExtension == 'csv':
            print('Reading CSV...')
        
            self.df = pd.read_csv(self.filePath)
        
        elif self.fileExtension == 'xlsx':
            print('Reading XLSX...')

            self.df = pd.read_excel(self.filePath)
        
        else:
            print(f'Extension not recognized: {self.fileExtension}')

        # Feature NAN analysis (what proportion of the feature is NAN?)
        print('Running feature NAN Analysis...')
        self.nan = self.df.isna().mean()
        
    def _piiViolation(self):
        '''
        Runs the PII-matching method. Given the pandas representation of the data, look at the columns (features) and record the ones that contain the PII keywords we defined.

        Inputs:
            - None

        Returns:
            - None

        Attributes Defined Here:
            - (list: str) matches: List of unique column (feature) names that were found to be partial or complete matches to something in the PII list
            - (float) hitRate: Proportion of possibly PII columns in the dataset. Rounded to 2 decimal places)
        '''
                
        # container for the hit columns
        suspected_pii = []

        # check each of the columns against our pii_roots (the default or a custom one)
        for col in self.features:
            # make sure everything is the same regardless of casing
            lowercol = col.lower()

            # check the lower case versions, but append the normal column
            if len(set(lowercol.split(' ')).intersection(self.roots)) > 0:
                # the roots matched, so the column(s) have a space as a delimiter
                suspected_pii.append(col)

            elif len(set(lowercol.split('_')).intersection(self.roots)) > 0:
                # the roots matched, so the column(s) have '_' as a delimiter
                suspected_pii.append(col)

            elif len(set(lowercol.split('-')).intersection(self.roots)) > 0:
                # the roots matched, so the column(s) have '-' as a delimiter
                suspected_pii.append(col)

        # get rid of any duplicates we've amassed and save it
        self.matches = list(np.unique(suspected_pii))
        self.hitRate = round(len(suspected_pii) / len(self.features), 2)

    def getData(self):
        '''
        Getter for the dataframe and the possible PII matches. 

        Inputs:
            - None

        Returns:
            - (pd.DataFrame) df: Data stored in DataFrame format
            - (list: str) matches: List of unique column (feature) names that were found to be partial or complete matches to something in the PII list
        '''
        return self.df, self.matches
    
    def getMatchSet(self):
        '''
        Getter for the auto-subset df of the possible matches.

        Inputs:
            - None

        Returns:
            - (pd.DataFrame): Subset data stored in DataFrame format
        '''
        return self.df[self.matches]
    
    def getMatchSet_Latex(self, rows = 5):
        '''
        Getter for the auto-subset df of the possible matches, but in latex format.

        Inputs:
            - None

        Returns:
            - (str): Latex tabular representation of the head of the data
        '''
        return print(self.df[self.matches].head(rows).to_latex(index = False))
    
    def getNan(self):
        '''
        Returns the columns that have some number of NANs in them.

        Inputs:
            - None

        Returns:
            - (pd.Series): Column (feature) names that have a proportion of NANs that greater than 0
        '''

        return self.nan[self.nan > 0]
    
if __name__ == "__main__":
    # default len of arguments is 1
    if len(sys.argv) > 3 or len(sys.argv) <= 1:
        raise ValueError('Too many or too few arguments.')
    
    elif len(sys.argv) == 2:
        # just pass the path to the file
        pii = PIIScan(sys.argv[1])
    
    else:
        rootList = ast.literal_eval(sys.argv[2])

        # the path to the file and the custom root search
        pii = PIIScan(sys.argv[1], rootList)

    with open(f'reports/{pii.fileName}_report.txt', "w") as file:
        file.write(pii.__str__())