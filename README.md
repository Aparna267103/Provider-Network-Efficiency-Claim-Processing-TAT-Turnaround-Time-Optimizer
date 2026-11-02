# Provider Network Efficiency & Claim Processing TAT Optimizer

## Project Overview

This project focuses on analyzing healthcare insurance claims processing efficiency, identifying operational bottlenecks, monitoring SLA compliance, and forecasting future claim volumes.

The solution uses Python, SQL, and Power BI to transform synthetic healthcare claims data into actionable business insights.

## Business Objectives

- Monitor total, completed, and pending insurance claims.
- Analyze claim processing Turnaround Time (TAT).
- Identify delays across different claim processing stages.
- Monitor SLA compliance and SLA breaches.
- Identify overdue and at-risk pending claims.
- Compare processing performance across adjudicator tiers.
- Forecast upcoming weekly claim volumes.

## Tools & Technologies

- **Python:** Data cleaning, preprocessing, and time-series forecasting.
- **SQL:** Data querying and analytical transformations.
- **Power BI:** Interactive dashboards and KPI reporting.
- **Pandas:** Data manipulation.
- **Statsmodels:** Exponential Smoothing forecasting.

## Project Workflow

1. Generate and prepare synthetic healthcare claims data.
2. Clean and transform the dataset using Python.
3. Calculate claim processing durations and SLA indicators.
4. Perform analytical queries using SQL.
5. Build interactive Power BI dashboards.
6. Forecast weekly claim volumes using Exponential Smoothing.
7. Identify operational bottlenecks and prioritize pending claims.

## Power BI Dashboard Pages

The interactive Power BI report is available in [PowerBi Visuals.pbix](./PowerBi%20Visuals.pbix).

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

Weekly claim volumes are calculated using historical claim intake dates. The Exponential Smoothing model is used to forecast claim volumes for the next eight weeks.

## Key Business Outcomes

The dashboard is designed to help healthcare operations teams:

- Identify claims approaching or exceeding SLA limits.
- Monitor processing delays across operational stages.
- Understand workload distribution across adjudicator tiers.
- Prioritize high-risk pending claims.
- Plan resources using forecasted claim volumes.

## Dataset

This project uses synthetic healthcare insurance claims data for demonstration and portfolio purposes. No real patient information is intended to be included.

## Project Status

Completed – Python, SQL, Power BI dashboards, and weekly claims forecasting.

## Author

Aparna V

**Skills Demonstrated:** Python | SQL | Power BI | DAX | Data Analytics | Time-Series Forecasting
