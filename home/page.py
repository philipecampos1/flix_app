import streamlit as st
import plotly.express as px
from movies.service import MovieService


def show_home():
    movie_service = MovieService()
    movie_stats = movie_service.get_movie_stats()

    st.title('Movies stats')

    if len(movie_stats['movies_by_genre']) > 0:
        st.subheader('Movies by gender')
        fig = px.pie(
            movie_stats['movies_by_genre'],
            values='count',
            names='genre__name',
            title='Movies by genre',
        )
        st.plotly_chart(fig)

    st.subheader('Amount movies registred: ')
    st.write(movie_stats['total_movies'])

    st.subheader('Amount of movies by genre: ')
    for genre in movie_stats['movies_by_genre']:
        st.write(f'{genre["genre__name"]}: {genre["count"]}')

    st.subheader('Amout reviews registred: ')
    st.write(movie_stats['total_reviews'])

    st.subheader('Avarage of stars: ')
    st.write(movie_stats['avarage_stars'])
