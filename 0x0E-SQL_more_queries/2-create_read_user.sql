-- a script that creates the database
SELECT SCHEMA_NAME FROM information_schema.SCHEMATA WHERE SCHEMA_NAME = 'hbtn_0d_2';
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
SELECT user FROM mysql.user WHERE user = 'user_0d_2';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
