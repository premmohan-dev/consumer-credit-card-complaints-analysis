-- Research Question 3
-- How did complaint volume change over the study period?
-- Purpose: Calculates monthly complaint volume over time.

SELECT
    LEFT([Date Received],4) AS ComplaintYear,
    MID([Date Received],6,2) AS ComplaintMonth,
    COUNT(*) AS Complaint_Count
FROM ConsumerComplaints
GROUP BY
    LEFT([Date Received],4),
    MID([Date Received],6,2)
ORDER BY
    LEFT([Date Received],4),
    MID([Date Received],6,2);
