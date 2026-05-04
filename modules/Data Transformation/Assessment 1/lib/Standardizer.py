import pandas
from datetime import datetime
import calendar
import re
from lib.Presenter import Presenter


'''
This script handles enforcement of standard formats within the dataset.
'''

class Standardizer(Presenter):
    def __init__(self, _df, _outputDf):
        self.df = _df
        self.outputDF = _outputDf

    def StandardizeAll(self):
        self.StandardizeHealthBoard()
        self.StandardizeSpecialty()
        self.StandardizeOutcome()
        self.StandardizeFollowUp()
        self.StandardizeDatesInColumn("Appointment Date")
        self.StandardizeDatesInColumn("Date of Birth")
        self.StandardizeNames()
        self.StandardizePostCodes()

    def StandardizeNames(self):
        """
        Standardizes patient names within the dataset to the following format: 'Fname Lname'
        """
        print("=" * 30)
        print("... Standardizing patient names ... ", end="")
        affectedCount = 0
        for i, name in enumerate(self.df["Patient Name"]):

            if pandas.isna(name):
                self.outputDF.loc[i, "Patient Name"] = pandas.NA
                affectedCount += 1
                continue

            nameParts = name.split(", ")
            new_name = name
            if len(nameParts) > 1:
                affectedCount += 1
                new_name = f"{nameParts[1]} {nameParts[0]}"

            self.outputDF.loc[i, "Patient Name"] = new_name
        self.PresentAffectedCount(affectedCount)


    def StandardizePostCodes(self):
        """
        Ensures every letter in post codes value is capitalized.
        e.g. 'g22 7qt' -> 'G22 7QT'
        """
        print("=" * 30)
        print("... Standardizing post codes ... ", end="")
        affectedCount = 0
        for i, code in enumerate(self.df["Post Code"]):
            if pandas.isna(code):
                self.outputDF.loc[i, "Post Code"] = pandas.NA
                affectedCount += 1
                continue

            if re.search("[a-z]", code):
                affectedCount += 1

            newCode = code.upper()
            self.outputDF.loc[i, "Post Code"] = newCode
        self.PresentAffectedCount(affectedCount)


    def StandardizeHealthBoard(self):
        _map = {
            "nhs": "NHS",
            "and": "&",
        }

        print("=" * 30)
        print(f"... Standardizing Health Board ... ", end="")
        affectedCount = 0
        for i, val in enumerate(self.df["Health Board"]):
            valParts = val.split(" ")
            result = []
            for word in valParts:
                if word.lower() in _map.keys():
                    result.append(_map[word.lower()])
                    continue

                if (len(word) > 3):
                    result.append(word.title())
                else:
                    result.append(word)


            affectedCount += 1
            if result == valParts:
                affectedCount -= 1 
            
            self.outputDF.loc[i, "Health Board"] = " ".join(result)

        self.PresentAffectedCount(affectedCount)

            
    def StandardizeSpecialty(self):
        _map = {
            "nhs": "NHS",
            "and": "&",
            "ent": "ENT"
        }

        print("=" * 30)
        print(f"... Standardizing Specialty ... ", end="")
        affectedCount = 0
        for i, val in enumerate(self.df["Specialty"]):
            ValParts = val.split(" ")
            result = []

            for word in ValParts:
                if word.lower() in _map.keys():
                    result.append(_map[word.lower()])
                else:
                    result.append(word.title())

            affectedCount += 1
            if ValParts == result:
                affectedCount -= 1
            
            self.outputDF.loc[i, "Specialty"] = " ".join(result)

        self.PresentAffectedCount(affectedCount)


    def StandardizeOutcome(self):
        _map = {
            "dna": "DNA",
            "cbp": "CBP",
            "cbh": "cbh",
            "cancelled by patient": "CBP",
            "cancelled by hospital": "CBH",
            "attended": "A",
            "did not attend": "DNA"
        }

        print("=" * 30)
        print(f"... Standardizing Outcome records ... ", end="")
        affectedCount = 0

        for i, val in enumerate(self.df["Outcome"]):
            result = ""

            if isinstance(val, str) and val.lower() in _map.keys():
                result = _map[val.lower()]

            affectedCount += 1
            if result == val:
                affectedCount -= 1
        
            self.outputDF.loc[i, "Outcome"] = result

        self.PresentAffectedCount(affectedCount)


    def StandardizeFollowUp(self):
        _map = {
            "1": 1,
            "0": 0,
            "true": 1,
            "false": 0,
            "yes": 1,
            "no": 0,
            "n": 0,
            "y": 1
        }

        print("=" * 30)
        print(f"... Standardizing Follow Up Required ... ", end="")
        affectedCount = 0

        for i, val in enumerate(self.df["Follow Up Required"]):
            result = 0

            if pandas.isna(val):
                result = 0

            elif isinstance(val, str):

                if val.lower() in _map.keys():
                    result = _map[val.lower()]
                
            affectedCount += 1
            if str(val) == str(result):
                affectedCount -= 1
            
            self.outputDF.loc[i, "Follow Up Required"] = result
        
        self.PresentAffectedCount(affectedCount)


    def StandardizeDatesInColumn(self, col):
        """
        Standardizes all date values to the following format: YYYY-mm-dd.
        Impossible dates are rolled back to the last possible day to avoid data loss.
        """
        print("=" * 30)
        print(f"... Standardizing {col} dates ... ", end="")
        affectedCount = 0
        for i, dob in enumerate(self.df[col]):
            
            if isinstance(dob, str) and len(dob) > 0: # date exists
                dobParts = dob.split("/") if "/" in dob else dob.split("-")

                if len(dobParts[0]) == 4: # date has YYYY-mm-dd format
                    dobParts.reverse()
    
                if dobParts[1].isalpha(): # Normalize months
                    dobParts[1] = datetime.strptime(dobParts[1], "%b").strftime("%m")
    
                if len(dobParts[2]) < 4: # Normalize years
                    dobParts[2] = f'19{dobParts[2]}' if int(dobParts[2]) > 26 else f'20{dobParts[2]}'
                    
                # Roll back impossible dates
                max_day = calendar.monthrange(int(dobParts[2]), int(dobParts[1]))[1]
                if int(dobParts[0]) > int(max_day):
                    dobParts[0] = max_day
    
                d = datetime.strptime(f"{dobParts[0]}-{dobParts[1]}-{dobParts[2]}", '%d-%m-%Y')

                if str(d.date()) == dob:
                    affectedCount -= 1

                self.outputDF.loc[i, col] = d

            else: # date is null
                self.outputDF.loc[i, col] = pandas.NaT

            affectedCount += 1
        
        self.PresentAffectedCount(affectedCount)