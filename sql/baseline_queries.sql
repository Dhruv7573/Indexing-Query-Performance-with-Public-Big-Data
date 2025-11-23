USE nyc311;

-- 1) Count requests per borough for 2024
SELECT borough, COUNT(*) AS cnt
FROM service_requests
WHERE created_date BETWEEN '2024-01-01' AND '2024-12-31'
GROUP BY borough;

-- 2) Average time to close request (in hours) for selected complaint type
SELECT AVG(TIMESTAMPDIFF(HOUR, created_date, closed_date)) AS avg_hours
FROM service_requests
WHERE complaint_type = 'Noise - Residential';

-- 3) Filter by ZIP and date range
SELECT COUNT(*) 
FROM service_requests
WHERE incident_zip = '10027' AND created_date >= '2024-01-01';

-- EXPLAIN example (for the first query)
EXPLAIN ANALYZE
SELECT borough, COUNT(*) AS cnt
FROM service_requests
WHERE created_date BETWEEN '2024-01-01' AND '2024-12-31'
GROUP BY borough;
