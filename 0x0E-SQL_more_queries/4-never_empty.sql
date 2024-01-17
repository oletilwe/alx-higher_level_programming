-- a script that creates the table id_not_null on your MySQL server
USE id_not_null;
IF NOT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'id_not_null' AND table_schema = DATABASE())
THEN
CREATE TABLE id_not_null (
        id INT DEFAULT 1,
        name VARCHAR(256),
        PRIMARY KEY (id)
    );
SELECT 'Table id_not_null created.';
ELSE
SELECT 'Table id_not_null already exists.';
END IF;
