-- Research Question 4
-- What themes appeared most frequently in consumer complaint narratives?
-- Purpose: Retrieves complaint narratives used for theme analysis.

SELECT
    [Consumer complaint narrative]
FROM ConsumerComplaints
WHERE [Consumer complaint narrative] IS NOT NULL
      AND [Consumer complaint narrative] <> '';
