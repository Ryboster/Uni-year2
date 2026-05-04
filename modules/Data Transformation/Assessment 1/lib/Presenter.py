import pandas


class Presenter:
    '''
    This class presents the results of various processes.
    Presenting means to print() them in an organized way.
    '''

    def __init__(self, _df, _outputDF):
        self.df = _df
        self.outputDF = _outputDF
        pass

    def PresentAffectedCount(self, count):
        print(f"Affected {count} records.")
    
    def PresentMissingValuesPerColumn(self):
        for col in self.df.columns:
            missingValues = 0
            print(f"... Analyzing column {col} ...", end="")
            for i, row in self.df.iterrows():
                if pandas.isna(row[col]):
                    missingValues += 1
            print(f" missing {missingValues} values.")
        print ("="*30)