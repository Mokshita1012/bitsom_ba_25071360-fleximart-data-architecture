-- Task 3.2: Warehouse Dummy Data
-- This file inserts minimum required dummy data into the star schema
-- Data strictly follows assignment requirements

-- =============================
-- DIMENSION: dim_date (30 dates: Jan–Feb 2024)
-- =============================
INSERT IGNORE INTO dim_date
(date_key, full_date, day_of_week, month, month_name, quarter, year, is_weekend)
VALUES
(20240101,'2024-01-01','Monday',1,'January',1,2024,0),
(20240102,'2024-01-02','Tuesday',1,'January',1,2024,0),
(20240103,'2024-01-03','Wednesday',1,'January',1,2024,0),
(20240104,'2024-01-04','Thursday',1,'January',1,2024,0),
(20240105,'2024-01-05','Friday',1,'January',1,2024,0),
(20240106,'2024-01-06','Saturday',1,'January',1,2024,1),
(20240107,'2024-01-07','Sunday',1,'January',1,2024,1),
(20240108,'2024-01-08','Monday',1,'January',1,2024,0),
(20240109,'2024-01-09','Tuesday',1,'January',1,2024,0),
(20240110,'2024-01-10','Wednesday',1,'January',1,2024,0),
(20240111,'2024-01-11','Thursday',1,'January',1,2024,0),
(20240112,'2024-01-12','Friday',1,'January',1,2024,0),
(20240113,'2024-01-13','Saturday',1,'January',1,2024,1),
(20240114,'2024-01-14','Sunday',1,'January',1,2024,1),
(20240115,'2024-01-15','Monday',1,'January',1,2024,0),

(20240201,'2024-02-01','Thursday',2,'February',1,2024,0),
(20240202,'2024-02-02','Friday',2,'February',1,2024,0),
(20240203,'2024-02-03','Saturday',2,'February',1,2024,1),
(20240204,'2024-02-04','Sunday',2,'February',1,2024,1),
(20240205,'2024-02-05','Monday',2,'February',1,2024,0),
(20240206,'2024-02-06','Tuesday',2,'February',1,2024,0),
(20240207,'2024-02-07','Wednesday',2,'February',1,2024,0),
(20240208,'2024-02-08','Thursday',2,'February',1,2024,0),
(20240209,'2024-02-09','Friday',2,'February',1,2024,0),
(20240210,'2024-02-10','Saturday',2,'February',1,2024,1),
(20240211,'2024-02-11','Sunday',2,'February',1,2024,1),
(20240212,'2024-02-12','Monday',2,'February',1,2024,0),
(20240213,'2024-02-13','Tuesday',2,'February',1,2024,0),
(20240214,'2024-02-14','Wednesday',2,'February',1,2024,0),
(20240215,'2024-02-15','Thursday',2,'February',1,2024,0);


-- =============================
-- DIMENSION: dim_product (15 products, 3 categories)
-- =============================
INSERT IGNORE INTO dim_product
(product_key, product_name, category)
VALUES
(1,'Smartphone A','Electronics'),
(2,'Laptop Pro','Electronics'),
(3,'Bluetooth Headphones','Electronics'),
(4,'Smart TV','Electronics'),
(5,'Washing Machine','Electronics'),
(6,'Office Chair','Furniture'),
(7,'Wooden Table','Furniture'),
(8,'Sofa Set','Furniture'),
(9,'Bookshelf','Furniture'),
(10,'Bed Frame','Furniture'),
(11,'Notebook Pack','Stationery'),
(12,'Pen Set','Stationery'),
(13,'Office Files','Stationery'),
(14,'Desk Organizer','Stationery'),
(15,'Printer Paper','Stationery');


-- =============================
-- DIMENSION: dim_customer (12 customers, 4 cities)
-- =============================
INSERT IGNORE INTO dim_customer
(customer_key, customer_name, city, state)
VALUES
(1,'Rahul Sharma','Delhi','Delhi'),
(2,'Ananya Gupta','Mumbai','Maharashtra'),
(3,'Amit Verma','Bengaluru','Karnataka'),
(4,'Sneha Iyer','Chennai','Tamil Nadu'),
(5,'Rohit Mehta','Delhi','Delhi'),
(6,'Kavya Nair','Mumbai','Maharashtra'),
(7,'Suresh Reddy','Bengaluru','Karnataka'),
(8,'Pooja Singh','Chennai','Tamil Nadu'),
(9,'Arjun Malhotra','Delhi','Delhi'),
(10,'Neha Jain','Mumbai','Maharashtra'),
(11,'Vikram Rao','Bengaluru','Karnataka'),
(12,'Meenal Kapoor','Chennai','Tamil Nadu');

-- =============================
-- FACT TABLE: fact_sales (40 transactions)
-- =============================
INSERT INTO fact_sales
(date_key, product_key, customer_key, quantity_sold, unit_price, discount_amount, total_amount)
VALUES

(20240106,1,1,3,15000,1000,44000),
(20240107,2,2,2,75000,5000,145000),
(20240113,3,3,4,2500,0,10000),
(20240114,4,4,2,55000,4000,106000),
(20240203,5,5,3,30000,3000,87000),
(20240204,6,6,5,8000,0,40000),
(20240210,7,7,3,12000,0,36000),
(20240211,8,8,2,45000,5000,85000),
(20240101,9,9,1,6000,0,6000),
(20240102,10,10,1,18000,2000,16000),
(20240103,11,11,4,200,0,800),
(20240104,12,12,3,500,0,1500),
(20240105,13,1,2,1500,0,3000),
(20240108,14,2,1,2500,0,2500),
(20240109,15,3,5,100,0,500),
(20240110,1,4,1,15000,0,15000),
(20240111,2,5,1,75000,4000,71000),
(20240112,3,6,2,2500,0,5000),
(20240115,4,7,1,55000,3000,52000),
(20240201,5,8,1,30000,0,30000),
(20240202,6,9,2,8000,0,16000),
(20240205,7,10,1,12000,0,12000),
(20240206,8,11,1,45000,3000,42000),
(20240207,9,12,2,6000,0,12000),
(20240208,10,1,1,18000,2000,16000),
(20240209,11,2,3,200,0,600),
(20240212,12,3,4,500,0,2000),
(20240213,13,4,2,1500,0,3000),
(20240214,14,5,1,2500,0,2500),
(20240215,15,6,6,100,0,600),
(20240106,6,7,2,8000,0,16000),
(20240107,7,8,1,12000,0,12000),
(20240113,8,9,2,45000,3000,87000),
(20240114,9,10,3,6000,0,18000),
(20240203,10,11,1,18000,2000,16000),
(20240204,11,12,5,200,0,1000),
(20240108,12,8,2,500,0,1000),
(20240109,13,9,1,1500,0,1500),
(20240205,14,10,2,2500,0,5000),
(20240206,15,11,4,100,0,400);

