import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from genres.service import GenreService


def show_genres():
    genre_service = GenreService()
    genres = genre_service.get_genres()

    if genres:
        st.write('Genres list:')
        genres_df = pd.json_normalize(genres)
        AgGrid(
            data=genres_df,
            reload_data=True,
            columns_auto_size_mode=True,
            enableSorting=True,
            enableFilter=True,
            enableColResize=True,
            key='genres_grid',
        )
    else:
        st.warning('Genres was not found')

    st.title('Register new genre')
    name = st.text_input('Name of the genre')
    if st.button('Register'):
        if name:
            new_genre = genre_service.create_genre(
                name=name,
            )
            if new_genre:
                st.rerun()
            else:
                st.error('Error to register genres. Please check the fields')
        else:
            st.warning('Please dont leave the field empty')
