-- LeetCode 579 – Find Cumulative Salary of an Employee

SELECT 
    Id,
    `Month`,
    Salary,
FROM(
    SELECT
        Id,
        `Month`,
        SUM (Salary) OVER(
            PARTITION BY Id,
            ORDER BY `Month`,
            ROWS BETWEEN 2 PRECEEDING AND CURRENT ROW
        ) AS Salary,
        MAX(`Month`) OVER(
            PARTITION BY Id
        ) AS MaxMonth
    FROM Employee
)t
WHERE `Month`!=MaxMonth
ORDER BY Id, `Month` DESC;