CREATE DATABASE electronics_store;

USE electronics_store;

CREATE TABLE users(
   user_id VARCHAR(50) PRIMARY KEY,
   name VARCHAR(50),
   email_id VARCHAR(50) CHECK (email_id LIKE '%@%.%'),
   phone_number VARCHAR(50) CHECK (LENGTH(phone_number) = 10),
   dob DATE,
   user_since DATE,
   address VARCHAR(100),
   city VARCHAR(50),
   state VARCHAR(50),
   pincode INT
);

CREATE TABLE manufacturer(
   mf_id VARCHAR(50) PRIMARY KEY,
   name VARCHAR(50) NOT NULL,
   description VARCHAR(100),
   location VARCHAR(50)
);

CREATE TABLE components(
   comp_id INT PRIMARY KEY,
   description VARCHAR(50),
   part_no VARCHAR(50) NOT NULL,
   mf_id VARCHAR(50),
   name VARCHAR(50) NOT NULL,
   lifecycle VARCHAR(50),
   category VARCHAR(50),
   datasheet VARCHAR(100),
   rohs VARCHAR(50),
   mount_type VARCHAR(50),
   FOREIGN KEY(mf_id) REFERENCES manufacturer(mf_id)
);

CREATE TABLE description(
   comp_id INT,
   param VARCHAR(50),
   value VARCHAR(50),
   FOREIGN KEY(comp_id) REFERENCES components(comp_id),
   PRIMARY KEY(comp_id, param)
);

CREATE TABLE stock(
   comp_id INT,
   in_stock INT,
   lead_time INT,
   normally_stocking VARCHAR(5),
   FOREIGN KEY(comp_id) REFERENCES components(comp_id),
   PRIMARY KEY(comp_id)
);

CREATE TABLE price_slabs(
   comp_id INT,
   min_qty INT,
   price DECIMAL(6,2) NOT NULL,
   FOREIGN KEY(comp_id) REFERENCES components(comp_id),
   PRIMARY KEY(comp_id, min_qty)
);

CREATE TABLE orders(
   order_id INT PRIMARY KEY,
   user_id VARCHAR(50),
   date_time DATETIME,
   order_type VARCHAR(50),
   status VARCHAR(50),
   FOREIGN KEY(user_id) REFERENCES users(user_id)
);

CREATE TABLE order_comp(
   order_id INT,
   comp_id INT,
   qty INT,
   FOREIGN KEY(order_id) REFERENCES orders(order_id),
   FOREIGN KEY(comp_id) REFERENCES components(comp_id),
   PRIMARY KEY(order_id, comp_id)
);

CREATE TABLE payments(
   payment_id INT PRIMARY KEY,
   order_id INT,
   trnx_no VARCHAR(50),
   amount INT,
   method VARCHAR(50),
   FOREIGN KEY(order_id) REFERENCES orders(order_id)
);

-- Create a user view with age 
CREATE VIEW user_age AS
SELECT user_id, name, email_id, phone_number, dob, TIMESTAMPDIFF(YEAR, dob, CURDATE()) AS age, user_since, address, city, state, pincode
FROM users;

-- payment_backup Table for trigger demo
CREATE TABLE payments_backup(
   payment_id INT PRIMARY KEY,
   order_id INT,
   trnx_no VARCHAR(50),
   amount INT,
   method VARCHAR(50),
   deleted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
   FOREIGN KEY(order_id) REFERENCES orders(order_id)
);

-- Trigger to backup deleted payments
DELIMITER $$
CREATE TRIGGER backup_payments
AFTER DELETE ON payments
FOR EACH ROW
BEGIN
   INSERT INTO payments_backup(payment_id, order_id, trnx_no, amount, method)
   VALUES (OLD.payment_id, OLD.order_id, OLD.trnx_no, OLD.amount, OLD.method);
END $$
DELIMITER ;

-- Create a function to check if a user is prime
DELIMITER $$
CREATE FUNCTION is_prime_user(user_id VARCHAR(50)) RETURNS VARCHAR(5)
BEGIN
   DECLARE user_since DATE;
   DECLARE is_prime VARCHAR(5);
   
   SELECT users.user_since INTO user_since
   FROM users
   WHERE users.user_id = user_id;

   IF TIMESTAMPDIFF(YEAR, user_since, CURDATE()) > 4 THEN
      SET is_prime = 'True';
   ELSE
      SET is_prime = 'False';
   END IF;

   RETURN is_prime;
END $$
DELIMITER ;

-- Create procedure to restore deleted payments and delete from backup
DELIMITER $$
CREATE PROCEDURE restore_payment(IN payment_id1 INT)
BEGIN
   INSERT INTO payments(payment_id, order_id, trnx_no, amount, method)
   SELECT payment_id, order_id, trnx_no, amount, method
   FROM payments_backup
   WHERE payment_id = payment_id1;

   DELETE FROM payments_backup
   WHERE payment_id = payment_id1;
END $$
DELIMITER ;


-- Function to find best price for a component and quantity
DELIMITER $$
CREATE FUNCTION best_price(comp_id INT, qty INT) RETURNS DECIMAL(6,2)
BEGIN
   DECLARE price DECIMAL(6,2);
   SELECT price_slabs.price INTO price
   FROM price_slabs 
   WHERE price_slabs.comp_id=comp_id AND price_slabs.min_qty<qty 
   ORDER BY price_slabs.min_qty DESC
   LIMIT 1;

   RETURN price;
END $$
DELIMITER ;

-- Create a view to get bill for an order
CREATE VIEW bill_view AS
SELECT
   order_id,
   comp_id,
   NAME AS comp_name,
   qty,
   best_price(comp_id, qty) AS price,
   qty * best_price(comp_id, qty) AS amount
FROM order_comp
NATURAL JOIN components;
