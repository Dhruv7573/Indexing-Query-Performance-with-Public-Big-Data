import mysql.connector
import time

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="DhruvPass!9062297",
    database="nyc311"
)
cur = conn.cursor()

queries = {
    "Count per borough 2024": """
        SELECT borough, COUNT(*) AS cnt
        FROM service_requests
        WHERE created_date BETWEEN '2024-01-01' AND '2024-12-31'
        GROUP BY borough;
    """,
    "Avg time to close Noise - Residential": """
        SELECT AVG(TIMESTAMPDIFF(HOUR, created_date, closed_date)) AS avg_hours
        FROM service_requests
        WHERE complaint_type = 'Noise - Residential';
    """,
    "Count for ZIP 10027 since 2024-01-01": """
        SELECT COUNT(*)
        FROM service_requests
        WHERE incident_zip = '10027' AND created_date >= '2024-01-01';
    """
}

for name, q in queries.items():
    start = time.time()
    cur.execute(q)
    result = cur.fetchall()
    end = time.time()
    print(f"\nQuery: {name}")
    print("Time (s):", round(end - start, 4))
    print(result)

cur.close()
conn.close()
