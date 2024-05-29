import streamlit as st
from genres.page import show_genres
from actors.page import show_actors
from movies.page import show_movies
from reviews.page import show_reviews
from home.page import show_home
from login.page import show_login


def main():
    if 'token' not in st.session_state:
        show_login()
    else:
        st.title('Flix App')
        menu_option = st.sidebar.selectbox(
            'Select one option',
            ['Home', 'Genre', 'Actors', 'Movies', 'Reviews']
        )

        if menu_option == 'Home':
            show_home()

        if menu_option == 'Genre':
            show_genres()

        if menu_option == 'Actors':
            show_actors()

        if menu_option == 'Movies':
            show_movies()

        if menu_option == 'Reviews':
            show_reviews()


if __name__ == '__main__':
    main()
