-- Adding database (hbnb_test_db) for project
-- Adding a new user called hbnb_test (in localhost)
-- The password of hbnb_test should be set to hbnb_test_pwd
-- hbnb_test with all privileges on the database hbnb_test_db
-- The user hbnb_test has a SELECT privilege on the database performance_schema
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
