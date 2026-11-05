-- Query 1 – Claim Type-wise Average TAT 
-- Which claim type takes the longest time?

SELECT
    Claim_Type,
    COUNT(*) AS Total_Claims,
    ROUND(AVG(
        CAST(Decision_TAT_Days AS FLOAT)
    ), 2) AS Average_TAT

FROM Claims

WHERE Decision_TAT_Days IS NOT NULL

GROUP BY Claim_Type

ORDER BY Average_TAT DESC;

-- Query 2 – SLA Breach Percentage
-- What percentage of completed claims result in an SLA miss?

SELECT
    COUNT(*) AS Completed_Claims,

    SUM(
        CASE
            WHEN SLA_Status = 'Breached'
            THEN 1 ELSE 0
        END
    ) AS Breached_Claims,

    ROUND(
        100.0 * SUM(
            CASE
                WHEN SLA_Status = 'Breached'
                THEN 1 ELSE 0
            END
        ) / NULLIF(COUNT(*), 0),
        2
    ) AS Breach_Percentage

FROM Claims

WHERE Decision_TAT_Days IS NOT NULL;

-- Query 3 – Adjudicator Tier Performance
-- In which tier is the backlog the highest?

SELECT
    Adjudicator_Tier,

    COUNT(*) AS Total_Claims,

    SUM(
        CASE WHEN Claim_Status = 'Pending'
        THEN 1 ELSE 0 END
    ) AS Pending_Claims,

    ROUND(
        AVG(CAST(Decision_TAT_Days AS FLOAT)),
        2
    ) AS Average_TAT

FROM Claims

GROUP BY Adjudicator_Tier

ORDER BY Pending_Claims DESC;

-- Query 4 – Longest Pending Claims
-- Which claims require immediate attention?

SELECT
    Claim_ID,
    Claim_Type,
    Claim_Amount,
    Adjudicator_Tier,
    Intake_Date,
    Claim_Status,
    Decision_TAT_Days,
    Pending_Days

FROM Claims

WHERE Claim_Status = 'Pending'

ORDER BY Pending_Days DESC;

-- Query 5 – Monthly Claim Trend
-- SQL Server syntax for Query 5. If using SQLite, you should use `strftime('%Y-%m', Intake_Date)`.

SELECT
    FORMAT(Intake_Date, 'yyyy-MM') AS Claim_Month,

    COUNT(*) AS Total_Claims,

    AVG(
        CAST(Decision_TAT_Days AS FLOAT)
    ) AS Average_TAT

FROM Claims

GROUP BY FORMAT(Intake_Date, 'yyyy-MM')

ORDER BY Claim_Month;
