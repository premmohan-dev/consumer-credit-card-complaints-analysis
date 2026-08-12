-- Research Question 2
-- What complaint issues occurred most frequently among Virginia consumers?
-- Purpose: Identifies the most common complaint issues reported by Virginia consumers.

SELECT TOP 10
    Issue,
    COUNT(*) AS Complaint_Count
FROM ConsumerComplaints
GROUP BY Issue
ORDER BY COUNT(*) DESC;
