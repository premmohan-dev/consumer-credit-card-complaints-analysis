SELECT
    Company,
    COUNT(*) AS Complaint_Count
FROM complaints
GROUP BY Company
ORDER BY Complaint_Count DESC
LIMIT 10;
