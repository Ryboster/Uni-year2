import pandas


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


print("="*30)
print("... Summarizing initial data ...")
print("="*30)
print(f"... Record count: {len(df.index)}\n","="*30)
print(f"... Target data types: \n{outputDF.dtypes}\n","="*30)

presenter.PresentMissingValuesPerColumn()

print("... Sampling problematic values: ")
sampler.SampleProblematicValues()
