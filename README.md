# Provider Network Efficiency & Claim Processing TAT Optimizer

## Project Overview

This project analyzes healthcare insurance claims processing efficiency, identifies operational bottlenecks, monitors Service Level Agreement (SLA) compliance, and forecasts future claim volumes.

The solution integrates Python, SQL, and Power BI to transform synthetic healthcare claims data into actionable operational insights.

## Business Objectives

- Monitor total, completed, and pending insurance claims.
- Analyze claim processing Turnaround Time (TAT).
- Identify delays across different claim processing stages.
- Monitor SLA compliance and SLA breaches.
- Identify overdue and at-risk pending claims.
- Compare processing performance across adjudicator tiers.
- Forecast upcoming weekly claim volumes.
- Support workload planning and operational decision-making.

## Tools & Technologies

- **Python:** Data generation, cleaning, exploratory analysis, and forecasting.
- **SQL:** Data querying and analytical transformations.
- **Power BI:** Interactive dashboards and KPI reporting.
- **Pandas & NumPy:** Data manipulation and processing.
- **Statsmodels:** Exponential Smoothing forecasting.
- **DAX:** Measures and calculated columns for Power BI analytics.

## Dataset

This project uses a synthetic healthcare insurance claims dataset containing 3,000 records.

- **Date Range:** January 1, 2026 – November 5, 2026.
- **Claim Types:** Inpatient, Outpatient, and Pharmacy.
- **Adjudicator Tiers:** Tier 1, Tier 2, and Tier 3.
- **Claim Statuses:** Approved, Denied, and Pending.

The dataset is generated using Python with a fixed random seed and reference date to support reproducible analysis.

No real patient or personally identifiable information is used.

## Project Workflow

1. Generate 3,000 synthetic healthcare claims using Python.
2. Clean and transform the raw claims dataset.
3. Calculate claim processing durations and SLA indicators.
4. Perform analytical queries using SQL.
5. Build interactive Power BI dashboards using DAX.
6. Forecast weekly claim volumes using Exponential Smoothing.
7. Identify operational bottlenecks and prioritize pending claims.

### Run the Project

From the project root, run the scripts in this order:

```bash
python src/generate_data.py
python src/data_cleaning.py
python src/eda_analysis.py
python src/forecasting.py
```

## Power BI Dashboard

The interactive Power BI report is available here:

[View Power BI Dashboard](./PowerBi%20Visuals.pbix)

### Page 1 – Executive Overview

- Total Claims
- Completed Claims
- Pending Claims
- SLA Compliance %
- SLA Breached
- Total Claim Amount
- Monthly Claim Trend
- Claim Type Distribution

![Executive Overview](screenshots/Executive%20Overview.png)

### Page 2 – Process Bottleneck & Workforce Intelligence

- Average Claim Processing TAT
- Average Claim Amount
- Initial Review and Medical Review Delays
- Pending Days and Payment TAT
- Adjudicator Tier Performance
- Claim Type Analysis
- Claim Processing Bottlenecks

![Process Bottleneck & Workforce Intelligence](screenshots/Process%20Bottleneck%20%26%20Workforce%20Intelligence.png)

### Page 3 – SLA Monitoring & Predictive Operations

- Overdue Claims
- At-Risk Claims
- Average Pending Age
- Claims Aging Distribution
- SLA Risk Distribution
- Priority Claims Requiring Immediate Action
- Weekly Actual vs Forecast Claim Volume

![SLA Monitoring & Predictive Operations](screenshots/SLA%20Monitoring%20%26%20Predictive%20Operations.png)

## Forecasting Approach

Weekly claim volumes are calculated using historical claim intake dates.

The Exponential Smoothing model from Statsmodels is used to forecast claim volumes for the next eight weeks.

Historical actual values and future predicted values are combined into a forecast dataset for Power BI visualization.

## Key Business Outcomes

The dashboard is designed to help healthcare operations teams:

- Identify claims approaching or exceeding SLA limits.
- Monitor delays across claim processing stages.
- Understand workload distribution across adjudicator tiers.
- Prioritize high-risk pending claims.
- Support resource planning using forecasted claim volumes.

## Assumptions & Limitations

- All claims data is synthetic and intended for demonstration purposes.
- SLA thresholds are configurable demo assumptions, not official payer-specific SLA standards.
- Forecasts are based on historical synthetic claim volumes and should not be interpreted as actual business forecasts.
- SLA risk indicators support operational prioritization and do not represent clinical or regulatory decisions.

## Project Status

Completed – Python data generation and preprocessing, SQL analysis, Power BI dashboards, and eight-week claims volume forecasting.

## Author

**Aparna V**

**Skills Demonstrated:** Python | SQL | Power BI | DAX | Pandas | Data Analytics | SLA Monitoring | Time-Series Forecasting
