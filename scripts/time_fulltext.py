# scripts/time_fulltext.py
import mysql.connector
import time

# MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DhruvPass!9062297",
    database="nyc311"
)

cursor = conn.cursor()

# FULLTEXT query
query = "SELECT unique_key, complaint_type, descriptor FROM service_requests WHERE MATCH(descriptor) AGAINST('Noise');"

print("Running FULLTEXT query: 'Noise'...")

start = time.time()
cursor.execute(query)
results = cursor.fetchall()
end = time.time()

print(f"Time (s): {end - start:.4f}")
print(f"Number of rows returned: {len(results)}")
print("First 5 rows:")
for row in results[:5]:
    print(row)

cursor.close()
conn.close()
