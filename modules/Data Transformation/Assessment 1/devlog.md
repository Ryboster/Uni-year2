# Devlog

27/04/2026 9am: Set up virtual environment and installed Pandas
27/04/2026 9:20am: Obtained and printed total record count
27/04/2026 9:30am: defined GetMissingValuesPerColumn(). Obtained and printed number of missing values per column. 
27/04/2026 9:40am: Since every field has some problematic values, every field will be sampled.
27/04/2026 2:30pm: Sampled every field. Presented samples
28/04/2026 8:30am:  Standardised all date columns to a single ISO format with the datetime library. Handled impossible dates by rolling them back to the closest possible date. Where date was missing, inserted pandas.NaT for consistency.
28/04/2026 10:50am: Cleaned and standardised all categorical columns. Opted for acronyms where possible to minimize value length within the set. Normalised casing. Replaced every occurence of "and" with "&" for consistency.
28/04/2026 12:30pm: 
28/04/2026 1:20pm: Cleaned all numeric columns. Removed currency symbols. Normalized nulls to 0s. Converted text values to appropriate types (e.g. "N/A" in "Wait_Time_Days" became 0). Since negative values make no sense, I treated them as clerical error and converted them directly to positive values. zero-duration attendances make sense since they only occur when patient has not attended or appointment was cancelled so the value of 0 is justified.

29/04/2026 2:10am: Removed exact duplicates. Counted occurences. Displayed count.

29/04/2026 4:45am: Decided that this pruning won't be fully accurate until I standardize names.

29/04/2026 6am: Standardized post codes and patient names.

29/04/2026 2pm: Refactored code. Created 4 classes; Presenter, Cleaner, Sampler, Standardizer. Moved functions to those classes.  Reduced line count of main.py to <200.

30/04/2026 7pm - 

29/04/2026 4:30am  

29/04/2026 4:30am

29/04/2026 4:30am
