-- a script that creates the table unique_id on your MySQL server
USE your_database_name;
IF NOT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'unique_id' AND table_schema = DATABASE())
THEN
CREATE TABLE unique_id (
        id INT DEFAULT 1 UNIQUE,
        name VARCHAR(256),
        PRIMARY KEY (id)
    );
SELECT 'Table unique_id created.';
ELSE
SELECT 'Table unique_id already exists.';
END IF;
