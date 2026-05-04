import pandas
from lib.Standardizer import Standardizer
from lib.Sampler import Sampler
from lib.Cleaner import Cleaner
from lib.Presenter import Presenter
from lib.Pruner import Pruner
from lib.Visualizer import Visualizer


'''
This script defines two separate DataFrame objects; df and outputDf, and
two separate data type schemas; SAFE_MAP and CORRECTED_MAP.

SAFE_MAP is used within the df object's creator to read the csv file provided.
It casts every column to string for safety due to the fact that the csv data is messy.

CORRECTED_MAP is the target map applied to the OutpuDF object. In it, every column
is given its target type. outputDF is populated after each cleaning step, and at
the end of the process, it is saved to output.csv.
'''

### ========================================
### Constants
### ========================================

INPUT_FILE = "UI108006_scottish_health_dataset.csv"
OUTPUT_FILE = "output.csv"

SAFE_MAP = {
    "Patient_ID": str,
    "patient_name": str,
    "Email Address": str,
    "Phone": str,
    "post_code": str,
    "Health Board": str,
    "SPECIALTY": str,
    "Wait_Time_Days": str,
    "Outcome": str,
    "Duration (mins)": str,
    "Cost": str,
    "satisfaction_score": str
}

CORRECTED_MAP = {
    "Patient ID": pandas.Series(dtype="string"),
    "Patient Name": pandas.Series(dtype="string"),
    "Date of Birth": pandas.Series(dtype="datetime64[ns]"),
    "Email Address": pandas.Series(dtype="string"),
    "Phone": pandas.Series(dtype="string"),  # better than int for phone numbers
    "Post Code": pandas.Series(dtype="string"),
    "Health Board": pandas.Series(dtype="string"),
    "Specialty": pandas.Series(dtype="string"),
    "Appointment Date": pandas.Series(dtype="datetime64[ns]"),
    "Wait Time Days": pandas.Series(dtype="int"),
    "Outcome": pandas.Series(dtype="string"),
    "Duration Minutes": pandas.Series(dtype="int"),
    "Follow Up Required": pandas.Series(dtype="bool"),
    "Satisfaction Score": pandas.Series(dtype="int"),
    "Cost": pandas.Series(dtype="float")
}

### ========================================
### Initialization
### ========================================

# Load csv into a dataframe object
df = pandas.read_csv(INPUT_FILE, 
                     dtype={
                     "Patient_ID": str,
                     "patient_name": str,
                     "Email Address": str,
                     "Phone": str,
                     "post_code": str,
                     "Health Board": str,
                     "SPECIALTY": str,
                     "Wait_Time_Days": str,
                     "Outcome": str,
                     "Duration (mins)": str,
                     "Cost": str,
                     "satisfaction_score": str})

# Rename columns within the dataframe object to target names.
df = df.rename(columns={
              "Patient_ID": "Patient ID",
              "patient_name": "Patient Name",
              "post_code": "Post Code",
              "SPECIALTY": "Specialty",
              "Wait_Time_Days": "Wait Time Days",
              "satisfaction_score": "Satisfaction Score",
              "appointment_date": "Appointment Date",
              "Duration (mins)": "Duration Minutes"})


# Target Dataframe object where all data is saved after cleaning
outputDF = pandas.DataFrame(CORRECTED_MAP)


cleaner = Cleaner(df, outputDF)
standardizer = Standardizer(df, outputDF)
sampler = Sampler(df, outputDF)
presenter = Presenter(df, outputDF)
pruner = Pruner(df, outputDF)

### ========================================
### Function definitions
### ========================================


def CopyRemainingValues():
    '''
    Executed after cleaning all other fields. This function simply
    copies remaining value to the new dataframe for saving.
    '''
    for i, (_, row) in enumerate(df.iterrows()):
        outputDF.loc[i, "Patient ID"] = row["Patient ID"]
        outputDF.loc[i, "Email Address"] = row["Email Address"]
        outputDF.loc[i, "Phone"] = row["Phone"]


### ========================================
### Summary 
### ========================================

print("="*30)
print("... Summarizing initial data ...")
print("="*30)
print(f"... Record count: {len(df.index)}\n","="*30)
print(f"... Target data types: \n{outputDF.dtypes}\n","="*30)

presenter.PresentMissingValuesPerColumn()

print("... Sampling problematic values: ")
sampler.SampleProblematicValues()

standardizer.StandardizeAll()
cleaner.CleanAll()

CopyRemainingValues()

### Handle duplicates
outputDF = pruner.PruneAllDuplicates()
outputDF.to_csv(OUTPUT_FILE)

summary = outputDF[[
    "Wait Time Days",
    "Duration Minutes",
    "Satisfaction Score",
    "Cost"
]].describe()

print(summary)

y = Visualizer(outputDF)
y.VisualizeWaitTimeDistributionOverall()
y.VisualizeWaitTimeDistributionByBoard()
y.VisualizeDnaRatesBySpecialty()
y.VisualizeSatisfactionScoreDistributionBySpecialty()
y.VisualiseRelationshipBetweenWaitTimeAndConsultationDuration()

#outputDF.plot.bar()
#plt.show()



totalOver = 0
dnasOver = 0

totalUnder = 0
dnasUnder = 0
for i, (_, rec) in enumerate(outputDF.iterrows()):
    if rec["Wait Time Days"] > 90:
        if rec["Outcome"] == "DNA":
            dnasOver += 1        
        totalOver += 1

    else:
        if rec["Outcome"] == "DNA":
            dnasUnder += 1
        totalUnder += 1


x = totalOver / dnasOver
y = totalUnder / dnasUnder


totalRec = 0
followupReqRec = 0
for (_, rec) in outputDF.iterrows():
    if rec["Satisfaction Score"] < 3:
        totalRec += 1

        if rec["Follow Up Required"]:
            followupReqRec += 1


totalLothian = 0
totalLothianWaitTime = 0

totalHighland = 0
totalHighlandWaitTime = 0

lothianWaits = []
highlandWaits = []

for (_, rec) in outputDF.iterrows():
    if rec["Health Board"] == "NHS Lothian":
        lothianWaits.append(rec["Wait Time Days"])
        totalLothian += 1
        totalLothianWaitTime += rec["Wait Time Days"]
    elif rec["Health Board"] == "NHS Highland":
        highlandWaits.append(rec["Wait Time Days"])
        totalHighland += 1
        totalHighlandWaitTime += rec["Wait Time Days"]