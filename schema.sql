-- 1. Users table
CREATE TABLE users (
    user_id VARCHAR(10) PRIMARY KEY,
    age INT CHECK (age > 0),
    gender VARCHAR(10) CHECK (gender IN ('Male', 'Female', 'Other')),
    usage_preference VARCHAR(50)  -- e.g., "daily wear", "sports", "formal"
);

-- 2. Shoes table
CREATE TABLE shoes (
    shoe_id VARCHAR(10) PRIMARY KEY,
    brand VARCHAR(50),
    model VARCHAR(50),
    type VARCHAR(30),         -- e.g., "sneakers", "boots"
    material VARCHAR(30),
    color VARCHAR(20),
    size FLOAT,
    care_requirements TEXT    -- e.g., "wipe with damp cloth"
);

-- 3. Interactions table
CREATE TABLE interactions (
    interaction_id SERIAL PRIMARY KEY,
    user_id VARCHAR(10) REFERENCES users(user_id) ON DELETE CASCADE,
    shoe_id VARCHAR(10) REFERENCES shoes(shoe_id) ON DELETE CASCADE,
    action_type VARCHAR(20) CHECK (action_type IN ('viewed', 'purchased', 'wishlist', 'cared')),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. Weather data table
CREATE TABLE weather (
    date DATE PRIMARY KEY,
    temperature FLOAT,
    condition VARCHAR(30),   -- e.g., "Rainy", "Sunny", "Snow"
    humidity INT CHECK (humidity BETWEEN 0 AND 100)
);

-- 5. Recommendation logs (optional but useful)
CREATE TABLE recommendation_logs (
    log_id SERIAL PRIMARY KEY,
    user_id VARCHAR(10) REFERENCES users(user_id) ON DELETE CASCADE,
    recommended_shoes TEXT,  -- e.g., JSON or comma-separated IDs
    generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 6. Shoe care history (optional)
CREATE TABLE shoe_care_history (
    care_id SERIAL PRIMARY KEY,
    user_id VARCHAR(10) REFERENCES users(user_id) ON DELETE CASCADE,
    shoe_id VARCHAR(10) REFERENCES shoes(shoe_id) ON DELETE CASCADE,
    care_mode VARCHAR(30),   -- e.g., "standard wash", "deep clean"
    cared_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
