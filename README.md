# Care-Compass: An Integrated AI-Powered Health and Wellness Platform:

## Overview
**CareCompass** is an integrated healthcare and self-care platform built with **Streamlit** and **FastAPI**.  
It offers users a range of tools to promote physical and mental well-being, including symptom diagnosis, personalized nutrition recommendations, mental health support, and healthcare service discovery.

---

## Key Features
- **MediChat**: AI-driven symptom diagnosis assistant powered by Google's Gemini-Pro model.
- **PeacePal**: Mental health chatbot for emotional support conversations.
- **Meal-Maker**: Custom food recommendation system based on nutritional preferences.
- **Profile Tracker**: Calculates BMR, BMI, and daily calorie needs with visualization tools.
- **Near-Me**: Suggests nearby hospitals, clinics, and pharmacies based on user location.
- **Authentication System**: Secure signup and login using Firebase.

---

## Tech Stack
- **Frontend**: Streamlit
- **Backend**: FastAPI
- **Database**: Firebase Firestore (for storing user profiles)
- **Machine Learning**: Scikit-Learn (food recommender), Google Generative AI (Gemini-Pro API for chatbots)
- **Libraries/Frameworks**: Pandas, Matplotlib, Seaborn, Plotly, Geopy, Streamlit-Echarts, BeautifulSoup

---

## Project Structure
```
CareCompass-main/
│
├── backend/                 # FastAPI backend for meal recommendation system
│   ├── main.py
│   ├── model.py
│   └── description.txt
│
├── frontend/                # Streamlit frontend application
│   ├── custom_food_recommendation.py
│   ├── home_page.py
│   ├── ImageFinder.py
│   ├── mental_health.py
│   ├── nearby_places.py
│   ├── profile_page.py
│   ├── signin_signup.py
│   ├── symptom_diagnoser.py
│   └── description.txt
│
├── requirements.txt         # Python dependencies
└── README.md                 # Project overview (this file)
```

---

## How to Run the Application

### 1. Set up the Backend (FastAPI)
```bash
cd backend/
uvicorn main:app --reload
```

### 2. Set up the Frontend (Streamlit)
```bash
cd frontend/
streamlit run signin_signup.py
```

- Ensure your Firebase credentials (JSON) and Google Gemini-Pro API key are correctly configured.
- The Meal-Maker module will communicate with the FastAPI backend running locally.
