CREATE DATABASE IF NOT EXISTS blogdatabase;

USE blogdatabase;

CREATE TABLE user (
        id INTEGER NOT NULL, 
        email VARCHAR(150), 
        username VARCHAR(150), 
        password VARCHAR(150), 
        date_created DATETIME, 
        PRIMARY KEY (id), 
        UNIQUE (email), 
        UNIQUE (username)
);
CREATE TABLE post (
        id INTEGER NOT NULL, 
        text TEXT NOT NULL, 
        date_created DATETIME, 
        author INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        FOREIGN KEY(author) REFERENCES user (id) ON DELETE CASCADE
);
