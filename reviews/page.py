import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from reviews.service import ReviewService
from movies.service import MovieService


def show_reviews():
    review_service = ReviewService()
    reviews = review_service.get_reviews()
    if reviews:
        st.write('reviews list:')
        AgGrid(
            data=pd.DataFrame(reviews),
            reload_data=True,
            key='reviews_grid'
        )
    else:
        st.warning('Reviews was not found')

    st.title('Register new review')
    movie_service = MovieService()
    movies = movie_service.get_movies()
    movie_titles = {movie['title']: movie['id'] for movie in movies}
    selected_movie_title = st.selectbox('Movies', list(movie_titles.keys()))

    stars = st.number_input(
        label='Stars',
        min_value=0,
        max_value=5,
        step=1
    )

    comment = st.text_area('Comment')

    if st.button('Review'):
        new_review = review_service.create_review(
            movie=movie_titles[selected_movie_title],
            stars=stars,
            comment=comment,
        )
        if new_review:
            st.rerun()
        else:
            st.error('Error to register actor please check fields')
