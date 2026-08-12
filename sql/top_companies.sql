-- Research Question 1
-- Which companies received the most credit card complaints from Virginia consumers?
-- Purpose: Identifies the companies with the highest number of complaints in the dataset.

SELECT TOP 10
    Company,
    COUNT(*) AS Complaint_Count
FROM ConsumerComplaints
GROUP BY Company
ORDER BY COUNT(*) DESC;
