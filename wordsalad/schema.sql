CREATE TABLE users (
  user_id SERIAL PRIMARY KEY,
  name VARCHAR ( 50 ) NOT NULL,
  email VARCHAR ( 50 ) NOT NULL,
  username VARCHAR ( 50 ) UNIQUE NOT NULL,
  password VARCHAR ( 50 ) NOT NULL
);

CREATE TABLE decks (
  deck_id SERIAL PRIMARY KEY,
  owner_id INT NOT NULL, 
  title VARCHAR ( 100 ) NOT NULL,
  category VARCHAR ( 100 ) NOT NULL,
  description VARCHAR ( 255 ),
  public BOOLEAN NOT NULL, 
  FOREIGN KEY (owner_id) 
    REFERENCES users (user_id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);

CREATE TABLE cards (
  card_id SERIAL PRIMARY KEY,
  deck_id INT NOT NULL, 
  front VARCHAR ( 255 ) NOT NULL,
  back VARCHAR ( 255 ) NOT NULL,
  notes VARCHAR ( 255 ),
  FOREIGN KEY (deck_id) 
    REFERENCES decks (deck_id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
); 
