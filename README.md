# 🎬 CineMatch – Movie Recommender System

CineMatch is a content-based movie recommendation web application built using the TMDB dataset.  
It recommends 5 similar movies based on cosine similarity and displays movie posters and ratings using the TMDB API.

---

## 🚀 Features

- 🎯 Content-Based Recommendation System
- 📊 Cosine Similarity using Scikit-learn
- 🎬 TMDB API Integration (Posters + Ratings)
- 🌙 Clean Cinematic UI
- 🌐 Flask Web Application

---

## 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- HTML5
- CSS3
- TMDB API

---

## 📂 Project Structure

movie-recommender/
│
├── app.py
├── requirements.txt
├── model/
│   ├── movies.pkl
│   └── similarity.pkl
├── notebook/
│   └── model_building.ipynb
├── static/
│   └── style.css
├── templates/
│   └── index.html
└── README.md

---

## ▶️ Run Locally

1. Clone the repository

[git clone https://github.com/aYUSHpAAL/movie-recommender.git](https://github.com/aYUSHpAAL/movie-recommender.git)
cd movie-recommender

2. Install dependencies

pip install -r requirements.txt

3. Run the application

python app.py

4. Open in browser

http://127.0.0.1:5000

---

## 🔑 TMDB API Setup

This project requires a TMDB API key.

1. Create an account at https://www.themoviedb.org  
2. Generate your API key  
3. Add it inside app.py:

API_KEY = "your_api_key_here"

---

## ⚠️ Note

Model files (movies.pkl, similarity.pkl) are not included in this repository due to GitHub file size limits.

To generate them, run:

notebook/model_building.ipynb

---

## 🔮 Future Improvements

- Deploy to cloud (Render / Railway)
- Add collaborative filtering
- Add user authentication
- Add watchlist feature
- Add genre-based filtering

---

## 👨‍💻 Author

Ayush Pal  
Built as part of ML portfolio project.
