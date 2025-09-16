import pandas as pd

# Load the dataset (from Kaggle or UCI after download)
data = pd.read_csv("adult.csv", na_values=[" ?"])

# Rename columns to match your code
data = data.rename(columns={
    "workclass": "JobType",
    "education": "EdType",
    "sex": "gender",
    "native-country": "nativecountry",
    "income": "SalStat",
    "capital-gain": "capitalgain",
    "capital-loss": "capitalloss"
})

# Keep only the 10 columns you need
data = data[['age','JobType','EdType','occupation','gender',
             'race','nativecountry','SalStat','capitalgain','capitalloss']]

# Save as income.csv
data.to_csv("income.csv", index=False)
