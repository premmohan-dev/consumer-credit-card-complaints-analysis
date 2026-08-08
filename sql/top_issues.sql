SELECT
    Issue,
    COUNT(*) AS Complaint_Count
FROM complain*s
GROUP BY Issue
ORDER BY Complain*_Count DESC
LIMIT 10;
