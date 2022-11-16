DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS tables;
DROP TABLE IF EXISTS waters;
-- DROP TABLE IF EXISTS services;


CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255),
    number INT,
    -- time_slot TIME
   

);

CREATE TABLE waiters (
    id SERIAL PRIMARY KEY,
    f_name VARCHAR(255),
    l_name VARCHAR(255),
    table_capacity INT
    -- customer_id INT REFERENCES customers(id)   
    -- table_id INT REFERENCES table(id) -- is it many to many

);

CREATE TABLE tables (
    id SERIAL PRIMARY KEY,
    capacity INT,
    time_slot TIME,
    customer_id INT REFERENCES customers(id) ON DELETE CASCADE,
    waiter_id INT REFERENCES waiters(id) ON DELETE CASCADE
--  maybe time slot needs to be added 
);

-- CREATE TABLE services (
--     id SERIAL PRIMARY KEY, 
--     time_slot SMALLDATETIME,
--     customer_id INT REFERENCES customers(id),    
--     waiter_id INT REFERENCES waiters(id)
    

-- );