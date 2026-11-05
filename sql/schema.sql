
CREATE TABLE Claims (

    Claim_ID VARCHAR(20) PRIMARY KEY,

    Claim_Type VARCHAR(30),

    Claim_Amount DECIMAL(12,2),

    Intake_Date DATE,

    Initial_Review_Date DATE,

    Medical_Review_Date DATE,

    Pend_Start_Date DATE,

    Pend_Resolved_Date DATE,

    Decision_Date DATE,

    Payment_Date DATE,

    Adjudicator_Tier VARCHAR(20),

    Claim_Status VARCHAR(20),

    Decision_TAT_Days INTEGER,

    Pending_Days INTEGER,

    Current_Pending_Age INTEGER,

    SLA_Days INTEGER,

    SLA_Status VARCHAR(20)

);
