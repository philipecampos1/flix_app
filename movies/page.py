import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from movies.service import MovieService
from datetime import datetime
from genres.service import GenreService
from actors.service import ActorService


def show_movies():
    movie_service = MovieService()
    movies = movie_service.get_movies()

    if movies:
        st.write('Movies list:')
        movies_df = pd.json_normalize(movies)
        movies_df = movies_df.drop(columns=['actor', 'genre.id'])
        AgGrid(
            data=movies_df,
            reload_data=True,
            key='movies_gird'
        )
    else:
        st.warning('Movies not found')

    st.title('Register a new movie')

    title = st.text_input('Title')

    date_release = st.date_input(
        label='Release date',
        value=datetime.today(),
        min_value=datetime(1800, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY'
    )
    genre_service = GenreService()
    genres = genre_service.get_genres()
    genre_names = {genre["name"]: genre['id'] for genre in genres}
    selected_genre_name = st.selectbox('Genre', list(genre_names.keys()))

    actor_service = ActorService()
    actors = actor_service.get_actors()
    actor_names = {actor['name']: actor['id'] for actor in actors}
    selected_actors_names = st.multiselect('Actors', list(actor_names.keys()))
    selected_actors_ids = [actor_names[name] for name in selected_actors_names]

    resume = st.text_area('Resume')

    if st.button('Register'):
        new_movie = movie_service.create_movie(
            title=title,
            date_release=date_release,
            genre=genre_names[selected_genre_name],
            actor=selected_actors_ids,
            resume=resume,
        )
        if new_movie:
            st.rerun()
        else:
            st.error('Error to register actor please check fields')
