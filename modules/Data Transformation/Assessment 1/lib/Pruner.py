from lib.Presenter import Presenter
import pandas




class Pruner(Presenter):
    '''
    This class prunes redundant records. Most notably direct and indirect duplicates.
    '''

    def __init__(self, df, outputDF):
        self.df = df
        self.outputDF = outputDF
    
    def PruneAllDuplicates(self):
        '''
        Drops all duplicate and near-duplicate records.
        '''

        print("="*30)
        print("... Removing exact duplicates ... ", end="")
        self.PresentAffectedCount(self.GetDuplicatesCount())
        self.outputDF = self.outputDF.drop_duplicates() # Drop exact duplicates

        print("... Removing near duplicates ... ", end="")
        
        drop_records = self.GetNearDuplicates() # Get near duplicates
        self.PresentAffectedCount(len(drop_records))

        self.outputDF = self.outputDF.drop(drop_records) # & drop them
        return self.outputDF


    def GetDuplicatesCount(self):
        count = 0
        for i, (_, row1) in enumerate(self.outputDF.iterrows()):
            for j, (_, row2) in enumerate(self.outputDF.iterrows()):
                if i == j: # Avoids comparing a record to itself
                    continue

                if row1.equals(row2):
                    count += 1

        return count

    def GetNearDuplicates(self):
        '''
        Get the indexes of all near duplicates and return them.
        Near duplicates will differ in Wait Time Days. One record
        will always differ by 1 from another. This looks like a
        clerical error - An administrator readding the same record
        the next day. As such, the record with the lower Wait Time
        Days value will be pruned. 
        '''
        drop_records = []
        affectedCount = 0
        for i, (_, row1) in enumerate(self.outputDF.iterrows()):
            for j, (_, row2) in enumerate(self.outputDF.iterrows()):    
                if i == j:
                    continue        
                if self.IsNearMatch(row1, row2):
                    affectedCount += 1
                    if row1["Wait Time Days"] > row2["Wait Time Days"]:
                        drop_records.append(j)
                    else:
                        drop_records.append(i)
        return drop_records


    def IsNearMatch(self, row1, row2):
        '''
        A near duplicate is a record that shares the same specialty on the same date.
        While it is possible for a patient to have multiple appointments on
        the same day, realistically, you could only book one per specialty per day.
        '''
        if pandas.isna(row1["Patient ID"]) or pandas.isna(row2["Patient ID"]):
            return False

        if (row1["Patient ID"] == row2["Patient ID"] 
            and row1["Appointment Date"] == row2["Appointment Date"]
            and row1["Specialty"] == row2["Specialty"]):
            return True
        return False