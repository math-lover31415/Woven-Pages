DROP TABLE IF EXISTS authors;
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS book_genre;
DROP TABLE IF EXISTS editions;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS reviews;

CREATE TABLE authors(
    authorID integer PRIMARY KEY,
    first_name varchar(50),
    last_name varchar(50),
    about varchar(1000)
);

CREATE TABLE books(
    bookID integer PRIMARY KEY,
    title varchar(100) NOT NULL,
    author INT,
    FOREIGN KEY (author) REFERENCES authors(AuthorID)
);

CREATE TABLE book_genre(
    book integer NOT NULL,
    genre varchar(30) NOT NULL,
    FOREIGN KEY (book) REFERENCES books(BookID)
);

CREATE TABLE editions(
    ISBN varchar(20) PRIMARY KEY,
    book integer NOT NULL,
    format varchar(15) NOT NULL,
    pages integer,
    publisher varchar(50),
    publish_date DATE,
    lang varchar(20),
    FOREIGN KEY (book) REFERENCES books(BookID)
);

CREATE TABLE users(
    userID integer PRIMARY KEY,
    name_ varchar(50),
    dob DATE,
    username varchar(32) UNIQUE NOT NULL,
    password_hash BINARY(60) NOT NULL,
    isAdmin BOOLEAN DEFAULT FALSE
);

CREATE TABLE reviews(
    reviewID integer PRIMARY KEY,
    read_status varchar(10) DEFAULT 'To Read',
    rating integer DEFAULT 0,
    reviewer integer NOT NULL,
    book integer NOT NULL,
    user_Review varchar(1000),
    start_read Date,
    finish_read Date,
    CHECK (read_status IN ('To Read','Reading','Read')),
    CHECK (finish_read IS NULL OR read_status='Read'),
    CHECK (Rating>=0 AND Rating<=5),
    UNIQUE (reviewer,book),
    FOREIGN KEY (book) REFERENCES books(BookID),
    FOREIGN KEY (reviewer) REFERENCES users(UserID)
);