import pandas
from lib.Presenter import Presenter


'''
This script handles all the sampling of the dataset.
'''

class Sampler(Presenter):
    def __init__(self, _df, _outputDf):
        self.df = _df
        self.outputDF = _outputDf

    def SampleProblematicValues(self):
        '''
        Iterates over each field seeking incorrectly formatted data as outlined in the "About the Dataset" table.
        Matches are catalogued and the catalogue is presented via a print() statement.
        '''

        samples = {x: [] for x in self.df.columns}

        for col in self.df.columns:

            # Column names are inconsistent and thus are subject to change.
            # Due to that, they're identified by their index which won't mutate.
            colIndex = self.df.columns.get_loc(col)
            colVals = self.df[col]

            if colIndex == 0: # Patient ID
                samples[col] = colVals[colVals.astype(str).str.len() != 6].values

            elif colIndex == 1: # Patient Name
                samples[col] = colVals[colVals.astype(str).str.contains(",")].values

            elif colIndex == 2: # Date of Birth
                samples[col] = colVals[colVals.astype(str).str.contains("-")].values

            elif colIndex == 3: # Email Address
                samples[col] = colVals[pandas.isna(colVals)].values

            elif colIndex == 4: # Phone
                samples[col] = colVals[colVals.astype(str).str.len() != 10].values

            elif colIndex == 5: # Post Code
                samples[col] = colVals[colVals.astype(str).str.contains(r'[a-z]')].values

            elif colIndex == 6: # Health Board
                samples[col] = colVals[colVals.astype(str).str.contains("nhs")].values

            elif colIndex == 7: # Specialty
                samples[col] = colVals[colVals.astype(str).str.match(r'^[a-z]')].values

            elif colIndex == 8: # Appointment Date
                samples[col] = colVals[colVals.astype(str).str.match("-")].values

            elif colIndex == 9: # Wait Time Days
                samples[col] = list(colVals[colVals.isna()].values)

            elif colIndex == 10: # Outcome
                samples[col] = colVals[colVals.astype(str).str.len() > 3].values

            elif colIndex == 11: # Duration Minutes
                samples[col] = colVals[colVals.isna()].values

            elif colIndex == 12: # Follow Up Required 
                samples[col] = colVals[colVals.astype(str).str.match("([a-z]|[A-Z])")].values

            elif colIndex == 13: # Satisfaction Score
                samples[col] = colVals[colVals.astype(str).str.contains(r"\.")].values

            else: # Cost
                samples[col] = colVals[colVals.astype(str).str.contains("£")].values

        for key, sample in samples.items():
            if len(sample) > 0:
                print(f"... Sample for the column {key} ... {sample[0]}")