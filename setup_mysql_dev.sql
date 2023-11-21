-- A a script that prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- creates a new database
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- A new user hbnb_dev (in localhost)
-- The password of hbnb_dev should be set to hbnb_dev_pwd
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
-- User has all privileges on the database
-- user has SELECT privilege on the database performance_schema
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
