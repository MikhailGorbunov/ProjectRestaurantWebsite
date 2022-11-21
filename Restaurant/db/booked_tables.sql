DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS tables;
DROP TABLE IF EXISTS stuff;
DROP TABLE IF EXISTS bookings;
-- DROP TABLE IF EXISTS services;


CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255),
    phone_number VARCHAR(255)       -- problem with phone number with both data types: INT and VARCHAR(255)

);


CREATE TABLE stuff (
    id SERIAL PRIMARY KEY,
    f_name VARCHAR(255),
    l_name VARCHAR(255),
    table_capacity INT,
    role VARCHAR(255)

);


CREATE TABLE tables (
    id SERIAL PRIMARY KEY,
    table_capacity INT
    
);


CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    booking_capacity INT,
    time TIME,
    booked BOOLEAN, 
    table_id INT REFERENCES tables(id) ON DELETE CASCADE,
    customer_id INT REFERENCES customers(id) ON DELETE CASCADE,
    stuff_id INT REFERENCES stuff(id) ON DELETE CASCADE

);


-- ALTER TABLE bookings
-- ALTER COLUMN booked
-- SET DEFAULT FALSE