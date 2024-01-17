-- a script that creates the table force_name
USE force_name;
IF NOT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'force_name' AND table_schema = DATABASE())
THEN
CREATE TABLE force_name (
        id INT,
        name VARCHAR(256) NOT NULL,
        PRIMARY KEY (id)
    );
SELECT 'Table force_name created.';
ELSE
SELECT 'Table force_name already exists.';
END IF;
