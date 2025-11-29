# NYC 311 Indexing & Query Performance - Assignment 5

## Overview
This project demonstrates how database indexing improves the performance of queries on a large real-world dataset: **NYC 311 Service Requests**.  
You will import the dataset, create indexes, measure execution times, run FULLTEXT search tests, and analyze the impact.

---

##  Dataset Download
Run this inside Codespace:

```bash
wget "https://data.cityofnewyork.us/api/views/erm2-nwe9/rows.csv?accessType=DOWNLOAD&bom=true" -O data/nyc_311.csv
```

---

## 1. Import CSV into MySQL

```bash
mysql -u root -p < schema.sql
```

Then load data:

```sql
LOAD DATA LOCAL INFILE 'data/nyc_311.csv'
INTO TABLE service_requests
FIELDS TERMINATED BY ','
IGNORE 1 LINES;
```

---

## 2. Baseline Queries (No Index)
Run:

- filter by date  
- filter by borough  
- group by complaint type  
- fulltext search on descriptor  

Capture timings using:

```sql
SET profiling = 1;
-- run query
SHOW PROFILES;
```

---

## 3. Create Indexes
Run:

```bash
mysql -u root -p < create-indexes.sql
```

Indexes added:
- `idx_created_date` — speeds up date range queries.  
- `idx_borough` — accelerates borough filtering.  
- `idx_complaint_type` — improves grouping/aggregation.  
- `idx_ft_descriptor` — FULLTEXT index for keyword search.

---

## 4. Rerun Queries (With Index)
Repeat the same queries.
Collect:
- execution times  
- profiling screenshot  
- EXPLAIN before/after  

---

## 5. FULLTEXT Query Tests
Test:

```sql
SELECT complaint_type, descriptor, created_date,
MATCH(descriptor) AGAINST ("Noise" IN NATURAL LANGUAGE MODE) AS relevance
FROM service_requests
WHERE MATCH(descriptor) AGAINST ("Noise" IN NATURAL LANGUAGE MODE)
ORDER BY relevance DESC
LIMIT 20;
```

Add relevance explanation:

> Before indexing, FULLTEXT searches were slower and produced inconsistent ranking. After adding the FULLTEXT index, results for the keyword **“Noise”** were more accurate and sorted using MySQL’s natural‑language scoring.

---


### **Users who benefit**
- **Data analysts:** faster reporting, better insights.  
- **Operations teams:** quicker trend detection and response prioritization.  
- **Management:** real-time dashboards load faster.  

### **Business value**
- Indexing eliminates full table scans.  
- Reduces CPU and memory usage.  
- Improves speed for citizen-response operations.

---
### Screenshots:
<img width="910" height="169" alt="Baseline FULLTEXT Query Results (Before FULLTEXT Index)" src="https://github.com/user-attachments/assets/efd245fe-a45a-49e3-9b5e-660427545656" />
<img width="910" height="189" alt="Baseline Scalar Query Results (Before Indexing)" src="https://github.com/user-attachments/assets/d4efa1e0-de47-42fe-85c9-8b94f326a031" />
<img width="910" height="187" alt="Data loaded successfully" src="https://github.com/user-attachments/assets/ac90f0cd-5102-4ac7-a4a7-212e6c71c097" />
<img width="910" height="326" alt="EXPLAIN Plan — Scalar Query (After B-tree Index)" src="https://github.com/user-attachments/assets/3267710f-afa7-43e8-a8d3-4169f4c08d29" />
<img width="910" height="378" alt="EXPLAIN Plan — Scalar Query (Before B-tree Index)" src="https://github.com/user-attachments/assets/6f1290cc-2e78-47b6-9ab5-e907acfc730a" />
<img width="910" height="169" alt="FULLTEXT Query — After FULLTEXT Index Applied" src="https://github.com/user-attachments/assets/c4118ec5-9ba0-45ea-b1f2-13621926225e" />
<img width="910" height="216" alt="FULLTEXT query EXPLAIN with FULLTEXT index" src="https://github.com/user-attachments/assets/bb87cfb1-b2fa-4099-ad48-cb3ea8d6fb54" />
<img width="910" height="164" alt="FULLTEXT query EXPLAIN without FULLTEXT index" src="https://github.com/user-attachments/assets/f3e164fb-bfc2-492c-bbc6-bbc89adc3188" />
<img width="910" height="227" alt="Scalar Queries — After B-tree Indexes Applied" src="https://github.com/user-attachments/assets/94f17daf-3a14-4045-abb5-009abf862be3" />





## 6. Folder Structure

```
project/
 ├── data/
 │    └── nyc_311.csv
 ├── schema.sql
 ├── create-indexes.sql
 ├── queries_before.sql
 ├── queries_after.sql
 ├── README.md
```

---


