DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;
-- DROP TABLE IF EXISTS destinations;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

-- CREATE TABLE destinations (
--     id SERIAL PRIMARY KEY,
--     country VARCHAR(255),
--     user_id INT NOT NULL REFERENCES users(id)
-- );

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    visited BOOLEAN,
    country_id INT NOT NULL REFERENCES countries(id)
);