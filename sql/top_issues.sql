SELECT
    Issue,
    COUNT(*) AS Complaint_Count
FROM complaints
GROUP BY Issue
ORDER BY Complaint_Count DESC
LIMIT 10;
