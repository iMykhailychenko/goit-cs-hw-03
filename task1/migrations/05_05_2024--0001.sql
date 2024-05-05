-- Table Users
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table Status
CREATE TABLE IF NOT EXISTS status (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE
);

-- Insert statuses if they don't exist
INSERT INTO status (name) VALUES ('new'),('in progress'),('completed')
ON CONFLICT (name) DO NOTHING;

-- Table Tasks
CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    description TEXT,
    status_id INTEGER,
    user_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (status_id) REFERENCES status (id)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
