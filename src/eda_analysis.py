import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

file_path = BASE_DIR / "data" / "processed" / "claims_enriched.csv"

report_dir = BASE_DIR / "reports"
report_dir.mkdir(exist_ok=True)

df = pd.read_csv(file_path)

# Convert relevant columns
df["Intake_Date"] = pd.to_datetime(df["Intake_Date"])

# --------------------------------
# 1. Overall KPI
# --------------------------------

total_claims = len(df)

completed = df["Decision_TAT_Days"].notna().sum()

pending = df["Decision_TAT_Days"].isna().sum()

breached = (
    df["SLA_Status"] == "Breached"
).sum()

sla_compliance = (
    (df["SLA_Status"] == "Within SLA").sum()
    / completed * 100
) if completed > 0 else 0

avg_tat = df["Decision_TAT_Days"].mean()

print("\nOVERALL PERFORMANCE")

print("Total Claims:", total_claims)
print("Completed Claims:", completed)
print("Pending Claims:", pending)
print("SLA Breaches:", breached)
print("SLA Compliance:", round(sla_compliance, 2), "%")
print("Average TAT:", round(avg_tat, 2), "days")

# --------------------------------
# 2. TAT by claim type
# --------------------------------

claim_analysis = df.groupby(
    "Claim_Type"
).agg(
    Total_Claims=("Claim_ID", "count"),
    Average_TAT=("Decision_TAT_Days", "mean"),
    Average_Pending=("Pending_Days", "mean")
).round(2)

print("\nCLAIM TYPE ANALYSIS")
print(claim_analysis)

claim_analysis.to_csv(
    report_dir / "claim_type_analysis.csv"
)

# --------------------------------
# 3. Bottleneck analysis
# --------------------------------

stages = [
    "Initial_Review_Days",
    "Medical_Review_Days",
    "Pending_Days"
]

bottleneck = df[stages].mean().sort_values(
    ascending=False
)

print("\nBOTTLENECK ANALYSIS")
print(bottleneck)

# Chart 1
plt.figure(figsize=(10, 6))

sns.barplot(
    x=bottleneck.values,
    y=bottleneck.index
)

plt.title("Average Processing Time by Stage")
plt.xlabel("Average Days")
plt.ylabel("Processing Stage")

plt.tight_layout()

plt.savefig(
    report_dir / "bottleneck_analysis.png",
    dpi=300
)

plt.show()

# --------------------------------
# 4. Tier-wise workload
# --------------------------------

tier_analysis = df.groupby(
    "Adjudicator_Tier"
).agg(
    Total_Claims=("Claim_ID", "count"),
    Average_TAT=("Decision_TAT_Days", "mean"),
    Pending_Claims=(
        "Claim_Status",
        lambda x: (x == "Pending").sum()
    )
).round(2)

print("\nTIER ANALYSIS")
print(tier_analysis)

tier_analysis.to_csv(
    report_dir / "tier_analysis.csv"
)

# --------------------------------
# 5. SLA status distribution
# --------------------------------

sla_counts = df["SLA_Status"].value_counts()

plt.figure(figsize=(8, 6))

plt.pie(
    sla_counts.values,
    labels=sla_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Claim SLA Status Distribution")

plt.tight_layout()

plt.savefig(
    report_dir / "sla_distribution.png",
    dpi=300
)

plt.show()

# --------------------------------
# 6. Claim amount vs TAT
# --------------------------------

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df.dropna(
        subset=["Decision_TAT_Days"]
    ),
    x="Claim_Amount",
    y="Decision_TAT_Days",
    hue="Claim_Type"
)

plt.title("Claim Amount vs Processing TAT")

plt.tight_layout()

plt.savefig(
    report_dir / "amount_vs_tat.png",
    dpi=300
)

plt.show()

print("\nEDA COMPLETED SUCCESSFULLY!")
