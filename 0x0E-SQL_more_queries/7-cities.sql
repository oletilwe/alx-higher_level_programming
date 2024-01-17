-- a script that creates the database hbtn_0d_usa and the table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
IF NOT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'states' AND table_schema = DATABASE())
THEN
CREATE TABLE states (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(256) NOT NULL
    );
SELECT 'Table states created.';
ELSE
	SELECT 'Table states already exists.';
END IF;
IF NOT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'cities' AND table_schema = DATABASE())
THEN
CREATE TABLE cities (
        id INT AUTO_INCREMENT PRIMARY KEY,
        state_id INT NOT NULL,
        name VARCHAR(256) NOT NULL,
        FOREIGN KEY (state_id) REFERENCES states(id)
    );
SELECT 'Table cities created.';
ELSE
	SELECT 'Table cities already exists.';
END IF;
