### Shoe Recommendation & Personalized Service System

This project implements a shoe recommendation engine and a personalized service module based on user interaction history, shoe metadata, and contextual weather data.

---

## 🔍 Overview

The system provides:

- **Shoe Recommendations** based on user preferences and past interactions
- **Personalized Services** like:
  - Care notifications for frequently worn shoes
  - Replacement suggestions based on usage patterns and weather

---

## 🧠 Approach

### Recommendation Logic
Implemented a hybrid approach combining:
- **Content-Based Filtering** (matching shoe attributes with user preferences)
- **Basic Collaborative Signals** (frequent purchases/views)

### Personalized Service Logic
Two key services were designed:
1. **Care Alerts**: If a user frequently wears a shoe type (e.g., white sneakers) and the weather is rainy or dusty, suggest cleaning/reminders.
2. **Replacement Suggestions**: If a shoe has been interacted with (viewed/purchased/cared) over 10 times in recent months, prompt potential replacement or upsell.

These rules are defined in `service_logic.py`.

---

## 📁 Project Structure

```

recommendation\_system/
│
├── app.py                    # Flask app with API endpoints
├── service\_logic.py          # Personalized service rules
├── recommend.py              # Recommendation logic
├── utils.py                  # Utility functions (e.g., filtering, scoring)
├── data/
│   ├── users.csv
│   ├── shoes.csv
│   ├── interactions.csv
│   └── weather.csv
├── schema.sql                # PostgreSQL schema
└── README.md


````
## ⚙️ How to Run

Make sure you have Python 3.x and `Flask`, `Pandas` installed.

```bash
cd recommendation_system
pip install flask pandas
python app.py
````

Then open your browser:

* To get recommendations:
  `http://127.0.0.1:5000/recommendations/U001`
* To get personalized alerts:
  `http://127.0.0.1:5000/alerts/U001`

Replace `U001` with any valid user ID from `users.csv`.

---

## 🗃️ PostgreSQL Schema

Although the project runs on local CSVs, the included `schema.sql` defines the ideal schema for a production database, covering:

* `users`: user profiles
* `shoes`: shoe attributes
* `interactions`: views, purchases, care actions
* `weather`: contextual data
* `recommendation_logs` (optional)
* `shoe_care_history` (optional)

---

## 🧪 Sample Data

Small synthetic datasets are created under the `data/` directory to simulate user behavior and system logic.

---

## 🛠️ Tech Stack

* **Python 3.10**
* **Flask** for the API
* **Pandas** for data handling
* **PostgreSQL** (schema only)

---

## ✅ Status

All core tasks have been implemented:

* Recommendation system
* Personalized service logic
* Simulated data
* PostgreSQL schema

---
