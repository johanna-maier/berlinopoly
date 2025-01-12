-- Create database: berlinopoly_db (SQLite does not use a specific command for database creation)

-- Drop existing tables
DROP TABLE IF EXISTS Game_Event_Deck;
DROP TABLE IF EXISTS Event_Cards;
DROP TABLE IF EXISTS Game_Property;
DROP TABLE IF EXISTS Field;
DROP TABLE IF EXISTS Users_Games;
DROP TABLE IF EXISTS Games;
DROP TABLE IF EXISTS Users;

-- Table: Users
CREATE TABLE Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    icon TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table: Games
CREATE TABLE Games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_name TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    finished_at TIMESTAMP,
    status TEXT CHECK(status IN ('ongoing', 'complete')) NOT NULL,
    winner_user_id INTEGER,
    FOREIGN KEY (winner_user_id) REFERENCES Users(id)
);

-- Table: Users_Games (Many-to-Many relationship)
CREATE TABLE Users_Games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    game_id INTEGER,
    current_balance DECIMAL(10, 2) NOT NULL,
    current_position TEXT NOT NULL,
    properties_owned JSON,
    next_player BOOLEAN NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (game_id) REFERENCES Games(id)
);

-- Table: Field
CREATE TABLE Field (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT CHECK(type IN ('property', 'event', 'start', 'prison')) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    rent_base DECIMAL(10, 2) NOT NULL,
    rent_with_house DECIMAL(10, 2) NOT NULL
);

-- Table: Game_Property
CREATE TABLE Game_Property (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_id INTEGER NOT NULL,
    property_id INTEGER NOT NULL,
    user_id INTEGER,
    status TEXT CHECK(status IN ('free', 'purchased', 'house_built')) NOT NULL,
    current_rent DECIMAL(10, 2),
    FOREIGN KEY (game_id) REFERENCES Users_Games(id),
    FOREIGN KEY (property_id) REFERENCES Field(id),
    FOREIGN KEY (user_id) REFERENCES Users(id)
);

-- Table: Event_Cards
CREATE TABLE Event_Cards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT CHECK(type IN ('Positive', 'Negative', 'Neutral')) NOT NULL,
    title TEXT NOT NULL,
    text TEXT NOT NULL,
    balance_change DECIMAL(10, 2) NOT NULL
);

-- Table: Game_Event_Deck
CREATE TABLE Game_Event_Deck (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_id INTEGER,
    event_card_id INTEGER,
    position_in_queue INTEGER,
    is_drawn BOOLEAN DEFAULT 0,
    drawn_at TIMESTAMP,
    FOREIGN KEY (game_id) REFERENCES Games(id),
    FOREIGN KEY (event_card_id) REFERENCES Event_Cards(id)
);