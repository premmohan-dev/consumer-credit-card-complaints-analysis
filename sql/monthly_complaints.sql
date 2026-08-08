SELECT
    YEAR([Date received]) AS Year,
    MONTH([Date received]) AS Month,
    COUNT(*) AS Complaint_Count
FROM complaints
GROUP BY
    YEAR([Date received]),
    MONTH([Date received])
ORDER BY
    Year,
    Month;
