# 🎬 AI-Powered Movie Recommendation System

A full-stack Movie Recommendation System that uses **Natural Language Processing (NLP)** to recommend similar movies based on their content. The application integrates the **TMDB API** to fetch real-time movie details and is built with **FastAPI** and **Streamlit**.

## 🚀 Live Demo

- **Frontend:** https://movies-recmd.streamlit.app/
- **Backend API:** https://movies-rec-832v.onrender.com/docs

---

## 📌 Features

- Content-based movie recommendations using NLP
- Smart movie search
- Genre-based recommendations
- Movie details including:
  - Poster
  - Ratings
  - Overview
  - Runtime
  - Cast
  - Release Date
- Fast REST API with FastAPI
- Responsive Streamlit UI
- Fully deployed on the cloud

---

## 🛠 Tech Stack

### Machine Learning & NLP
- Python
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity
- Pandas
- NumPy

### Backend
- FastAPI
- Requests
- TMDB API

### Frontend
- Streamlit

### Deployment
- Render
- Streamlit Community Cloud
- Git & GitHub

---

## 🏗️ Project Architecture

```text
                +----------------------+
                |   Streamlit Frontend |
                +----------+-----------+
                           |
                     HTTP Requests
                           |
                           ▼
                +----------------------+
                |    FastAPI Backend   |
                +----------+-----------+
                           |
          +----------------+----------------+
          |                                 |
          ▼                                 ▼
 Recommendation Engine                TMDB API
(TF-IDF + Cosine Similarity)      (Movie Metadata)
```

---

## 📂 Project Structure

```text
movie-recommendation/
│
├── backend/
│   ├── main.py
│   ├── recommendation.py
│   ├── requirements.txt
│   └── models/
│
├── frontend/
│   ├── app.py
│   ├── utils.py
│   └── assets/
│
├── data/
│   ├── movies.csv
│   ├── tfidf.pkl
│   ├── tfidf_matrix.pkl
│   ├── indices.pkl
│   └── df.pkl
│
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/movie-recommendation.git
cd movie-recommendation
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the FastAPI backend

```bash
uvicorn main:app --reload
```

Backend will run on:

```
http://127.0.0.1:8000
```

### Run the Streamlit frontend

```bash
streamlit run app.py
```

---

## 🔍 How It Works

1. User searches for a movie.
2. The backend processes the request.
3. TF-IDF converts movie descriptions into numerical vectors.
4. Cosine Similarity finds movies with similar content.
5. TMDB API enriches results with posters, ratings, cast, and other metadata.
6. Recommendations are displayed through the Streamlit interface.

---

## 📖 Future Improvements

- Hybrid Recommendation System (Content + Collaborative Filtering)
- User Authentication
- Watchlist & Favorites
- Personalized Recommendations
- AI-powered Movie Chatbot
- Semantic Search using Sentence Transformers
- Docker Support
- CI/CD Pipeline

---

## 📸 Screenshots

### Home Page

<img width="1919" height="876" alt="image" src="https://github.com/user-attachments/assets/627f1c1d-fd01-4bd8-af36-c8954182a1b2" />


### Recommendations

<img width="1919" height="873" alt="image" src="https://github.com/user-attachments/assets/3fb593f8-6069-4d2a-8893-3ddaac8ac965" />


### Movie Details

<img width="1918" height="849" alt="image" src="https://github.com/user-attachments/assets/e298b1f9-9b2f-4110-9c0c-027976158dae" />


---

## 🧠 Key Learnings

- Building end-to-end ML applications
- NLP-based recommendation systems
- FastAPI backend development
- REST API integration
- Cloud deployment with Render & Streamlit
- Git & GitHub workflow

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

⭐ If you found this project useful, consider giving it a star!
