USE nyc311;

-- B-tree indexes
CREATE INDEX idx_created_date ON service_requests (created_date);
CREATE INDEX idx_complaint_type ON service_requests (complaint_type(100));
CREATE INDEX idx_incident_zip ON service_requests (incident_zip);

-- FULLTEXT index
ALTER TABLE service_requests ADD FULLTEXT idx_ft_descriptor (descriptor);
