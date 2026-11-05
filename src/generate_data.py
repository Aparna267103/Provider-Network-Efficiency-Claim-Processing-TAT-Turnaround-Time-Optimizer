import pandas as pd
import numpy as np
from pathlib import Path

# Reproducible sample data
np.random.seed(42)

# Number of claims
N = 3000

# Fixed date range for reproducible synthetic data
START_DATE = pd.Timestamp("2026-01-01")
END_DATE = pd.Timestamp("2026-11-05")

today = END_DATE
period_start = START_DATE

# Project folders
BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = BASE_DIR / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

# Claim categories
claim_types = ["Inpatient", "Outpatient", "Pharmacy"]

tiers = ["Tier 1", "Tier 2", "Tier 3"]

statuses = ["Approved", "Denied", "Pending"]

data = []

for i in range(N):

    claim_type = np.random.choice(
        claim_types,
        p=[0.35, 0.40, 0.25]
    )

    tier = np.random.choice(
        tiers,
        p=[0.50, 0.30, 0.20]
    )

    status = np.random.choice(
        statuses,
        p=[0.65, 0.25, 0.10]
    )

    # Different processing complexity
    if claim_type == "Inpatient":
        amount = np.random.randint(30000, 300000)
        initial_days = np.random.randint(1, 6)
        medical_days = np.random.randint(3, 12)

    elif claim_type == "Outpatient":
        amount = np.random.randint(1000, 50000)
        initial_days = np.random.randint(1, 4)
        medical_days = np.random.randint(1, 6)

    else:
        amount = np.random.randint(500, 15000)
        initial_days = np.random.randint(1, 3)
        medical_days = np.random.randint(1, 4)

    # Tier-specific workload delay
    tier_delay = {
        "Tier 1": 1,
        "Tier 2": 3,
        "Tier 3": 5
    }

    if status == "Pending":
        earliest_intake = max(period_start, today - pd.Timedelta(days=75))
        latest_intake = today - pd.Timedelta(days=23)
    else:
        earliest_intake = period_start
        latest_intake = today - pd.Timedelta(days=58)

    intake_days = (latest_intake - earliest_intake).days
    intake = earliest_intake + pd.Timedelta(
        days=np.random.randint(0, intake_days + 1)
    )

    initial_review = intake + pd.Timedelta(
        days=initial_days
    )

    medical_review = initial_review + pd.Timedelta(
        days=medical_days + tier_delay[tier]
    )

    pend_days = np.random.randint(0, 25)

    pend_start = medical_review + pd.Timedelta(days=1)

    if status == "Pending":
        pend_resolved = pd.NaT
    else:
        pend_resolved = pend_start + pd.Timedelta(
            days=pend_days
        )

    decision = pend_resolved + pd.Timedelta(
        days=np.random.randint(1, 7)
    )

    # Some claims are still pending
    if status == "Pending":
        decision = pd.NaT
        payment = pd.NaT

    elif status == "Approved":
        payment = decision + pd.Timedelta(
            days=np.random.randint(1, 6)
        )

    else:
        payment = pd.NaT

    # Randomly simulate claims that are not yet completed
    data.append({
        "Claim_ID": f"CLM{i+1:05d}",
        "Claim_Type": claim_type,
        "Claim_Amount": amount,
        "Intake_Date": intake,
        "Initial_Review_Date": initial_review,
        "Medical_Review_Date": medical_review,
        "Pend_Start_Date": pend_start,
        "Pend_Resolved_Date": pend_resolved,
        "Decision_Date": decision,
        "Payment_Date": payment,
        "Adjudicator_Tier": tier,
        "Claim_Status": status
    })

df = pd.DataFrame(data)

# Save raw data
output_file = RAW_DIR / "claims_data.csv"

df.to_csv(output_file, index=False)

print("Claims dataset generated successfully!")
print("Total claims:", len(df))
print("Saved at:", output_file)

print(df.head())
