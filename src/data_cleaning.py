import pandas as pd
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

input_file = BASE_DIR / "data" / "raw" / "claims_data.csv"

output_dir = BASE_DIR / "data" / "processed"
output_dir.mkdir(parents=True, exist_ok=True)

# Load dataset
df = pd.read_csv(input_file)

# Convert date columns
date_columns = [
    "Intake_Date",
    "Initial_Review_Date",
    "Medical_Review_Date",
    "Pend_Start_Date",
    "Pend_Resolved_Date",
    "Decision_Date",
    "Payment_Date"
]

for col in date_columns:
    df[col] = pd.to_datetime(df[col], errors="coerce")

# Remove duplicate claims
df = df.drop_duplicates(subset=["Claim_ID"])

# Remove invalid claim amounts
df = df[df["Claim_Amount"] > 0].copy()

# Stage duration calculations
df["Initial_Review_Days"] = (
    df["Initial_Review_Date"] - df["Intake_Date"]
).dt.days

df["Medical_Review_Days"] = (
    df["Medical_Review_Date"] - df["Initial_Review_Date"]
).dt.days

df["Pending_Days"] = (
    df["Pend_Resolved_Date"] - df["Pend_Start_Date"]
).dt.days

# Completed claim processing TAT
df["Decision_TAT_Days"] = (
    df["Decision_Date"] - df["Intake_Date"]
).dt.days

# Payment TAT
df["Payment_TAT_Days"] = (
    df["Payment_Date"] - df["Intake_Date"]
).dt.days

# Current claim age for open claims
reference_date = pd.Timestamp.today().normalize()

df["Claim_Age_Days"] = (
    df["Decision_Date"].fillna(reference_date)
    - df["Intake_Date"]
).dt.days

df["Claim_Age_Days"] = (
    df["Decision_Date"].fillna(reference_date)
    - df["Intake_Date"]
).dt.days

# Configurable demo SLA
SLA_DAYS = {
    "Inpatient": 30,
    "Outpatient": 30,
    "Pharmacy": 30
}

df["SLA_Days"] = df["Claim_Type"].map(SLA_DAYS)

# SLA status
df["SLA_Status"] = np.where(
    df["Decision_TAT_Days"].isna(),
    "Pending",
    np.where(
        df["Decision_TAT_Days"] <= df["SLA_Days"],
        "Within SLA",
        "Breached"
    )
)

# Stage validation
duration_columns = [
    "Initial_Review_Days",
    "Medical_Review_Days",
    "Pending_Days",
    "Decision_TAT_Days",
    "Payment_TAT_Days"
]

for col in duration_columns:
    df.loc[df[col] < 0, col] = np.nan


# Current pending age
reference_date = pd.Timestamp.today().normalize()

df["Current_Pending_Age"] = np.where(
    df["Claim_Status"] == "Pending",
    (reference_date - df["Pend_Start_Date"]).dt.days,
    np.nan
)

# Save cleaned dataset
output_file = output_dir / "claims_enriched.csv"

df.to_csv(output_file, index=False)

print("Data cleaning completed!")
print("Total records:", len(df))
print("Pending claims:", (df["Claim_Status"] == "Pending").sum())
print("SLA breaches:", (df["SLA_Status"] == "Breached").sum())
print("Saved:", output_file)
