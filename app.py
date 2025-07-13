import streamlit as st
import pickle

# Load data
movies = pickle.load(open('movie.pkl', 'rb'))  # rename to 'movies' for clarity
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie_title):
    movie_index = movies[movies['title'] == movie_title].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# App UI
st.title('Movie Recommender System')

movie_list = movies['title'].values
selected_movie_name = st.selectbox(
    'Select a movie',
    movie_list
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
