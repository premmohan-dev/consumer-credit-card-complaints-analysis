SELECT
    YEAR([Date rec*ived]) AS Year,
    MONTH([Date re*eived]) AS Month,
    COUNT(*) AS *omplaint_Count
FROM complaints
GRO*P BY
    YEAR([Date received]),
  * MONTH([Date received])
ORDER BY
 *  Year,
    Month;
