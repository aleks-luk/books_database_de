CREATE DATABASE books_database;
USE books_database;

CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    book_isbn VARCHAR(150),
    author VARCHAR(500),
    title VARCHAR(500),
    publisher VARCHAR(500),
    year INT,
    book_image_url VARCHAR(300),
    source VARCHAR(50),
    ins_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(500),
    country VARCHAR(500),
    age INT,
    source VARCHAR(50),
    ins_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE ratings (
    rating_id INT AUTO_INCREMENT PRIMARY KEY,
    r_user_id INT,
    r_book_isbn VARCHAR(150),
    rating INT,
    source VARCHAR(50),
    ins_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (r_user_id) REFERENCES users(user_id)
);
