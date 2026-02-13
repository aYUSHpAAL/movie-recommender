from flask import Flask, render_template, request
import pickle
import requests

app = Flask(__name__)

# ===============================
# LOAD PICKLE FILES
# ===============================
movies = pickle.load(open('model/movies.pkl', 'rb'))
similarity = pickle.load(open('model/similarity.pkl', 'rb'))

API_KEY = "4992b4be880c98bdec4ba37b41654822"


# ===============================
# FETCH POSTER
# ===============================
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    data = requests.get(url).json()

    if data.get("poster_path"):
        return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]
    else:
        return "https://via.placeholder.com/300x450?text=No+Image"


# ===============================
# FETCH RATING
# ===============================
def fetch_rating(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    data = requests.get(url).json()

    return round(data.get("vote_average", 0), 1)


# ===============================
# RECOMMEND FUNCTION
# ===============================
def recommend(movie):
    movie_index = movies[movies['title'].str.lower() == movie.lower()].index[0]

    distances = similarity[movie_index]
    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []
    recommended_ratings = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
        recommended_ratings.append(fetch_rating(movie_id))

    return recommended_movies, recommended_posters, recommended_ratings


# ===============================
# HOME ROUTE
# ===============================
@app.route('/')
def home():
    return render_template(
        'index.html',
        movies=movies['title'].values
    )


# ===============================
# RECOMMEND ROUTE
# ===============================
@app.route('/recommend', methods=['POST'])
def recommend_movie():
    movie = request.form.get('movie')

    recommended_movies, recommended_posters, recommended_ratings = recommend(movie)

    return render_template(
        'index.html',
        movies=movies['title'].values,
        recommended_movies=recommended_movies,
        recommended_posters=recommended_posters,
        recommended_ratings=recommended_ratings
    )


# ===============================
# RUN APP
# ===============================
if __name__ == '__main__':
    app.run(debug=True)
