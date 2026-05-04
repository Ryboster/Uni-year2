
import pandas
from lib.Presenter import Presenter
import re

'''
This script handles cleaning of incorrect values within the dataset.
This includes pruning, casting, and enforcement of custom rules.
'''


class Cleaner(Presenter):
    def __init__(self, _df, _outputDf):
        self.df = _df
        self.outputDF = _outputDf

    def CleanAll(self):
        self.CleanCost()
        self.CleanDuration()
        self.CleanSatisfactionScore()
        self.CleanWaitTime()

    def CleanCost(self):
        '''
        Wront values in this column include symbols and characters.
        Pound symbols and currency codes are stripped. Nulls are replaced
        with 0s.
        '''
        print("... Cleaning Cost column ... ", end="")
        affectedCount = 0
        for i, val in enumerate(self.df["Cost"]):
            new_val = ""
            if pandas.isna(val):
                val = float(0.0)
                affectedCount += 1

            elif "£" in val:
                val = val.replace("£", "")
                affectedCount +=1

            elif "GBP" in val:
                val = val.replace("GBP", "")
                affectedCount +=1

            new_val = float(val)
            self.outputDF.loc[i, "Cost"] = float(new_val)
        self.PresentAffectedCount(affectedCount)

    def CleanSatisfactionScore(self):
        '''
        Wrong values in this column are either out of range, null, or
        decimal. Decimals are rounded to the nearest integer. Out of
        range values are capped at 5. 
        '''
        print("... Cleaning Satisfaction Score column ... ", end="")
        affectedCount = 0
        for i, val in enumerate(self.df["Satisfaction Score"]):
            if pandas.isna(val):
                self.outputDF.loc[i, "Satisfaction Score"] = 0
                affectedCount += 1
                continue

            if re.search(r"^[1-5]$", val):
                self.outputDF.loc[i, "Satisfaction Score"] = int(val)
                continue # value is correct

            affectedCount += 1
            if "." in val:
                val = int(round(float(val)))

            new_val = int(val)

            if new_val > 5:
                new_val = 5

            self.outputDF.loc[i, "Satisfaction Score"] = new_val

        self.PresentAffectedCount(affectedCount)

    def CleanDuration(self):
        '''
        Wrong values in this column are null. Nulls are converted to 0.
        '''
        print("... Cleaning Duration Minutes column ... ", end="")
        affectedCount = 0
        for i, val in enumerate(self.df["Duration Minutes"]):
            new_val = ""

            if pandas.isna(val):
                affectedCount += 1
                val = 0

            new_val = int(val)
            self.outputDF.loc[i, "Duration Minutes"] = new_val
        self.PresentAffectedCount(affectedCount)


    def CleanWaitTime(self):
        '''
        Wrong values in this column are either null or less than 0.
        Since Wait Time Days column is of type integer, nulls are converted to 0.
        Negative values are assumed to be clerical errors and inverted to positive values.
        '''

        print("... Cleaning Wait Time Days column ... ", end="")
        affectedCount = 0
        for i, val in enumerate(self.df["Wait Time Days"]):
            new_val = ""

            if pandas.isna(val) or (isinstance(val, str) and val.isalpha()):
                val = 0
                affectedCount += 1

            new_val = int(val)
            if new_val < 0:
                new_val = -new_val
                affectedCount += 1

            self.outputDF.loc[i, "Wait Time Days"] = new_val

        self.PresentAffectedCount(affectedCount)