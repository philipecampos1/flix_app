import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from actors.service import ActorService
from datetime import datetime


def show_actors():
    actor_service = ActorService()
    actors = actor_service.get_actors()

    if actors:
        st.write('Actors list:')
        actors_df = pd.json_normalize(actors)
        AgGrid(
            data=actors_df,
            reload_data=True,
            key='actors_grid'
        )
    else:
        st.warning('Actors was not found')

    st.title('Register new actors')
    name = st.text_input('Name of the actors')
    birthday = st.date_input(
        label='Actor birthday',
        value=datetime.today(),
        min_value=datetime(1800, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY',
    )
    nationality_drop_down = ['BRA', 'USA']
    nationality = st.selectbox(
        label='Nationality',
        options=nationality_drop_down,
    )

    if st.button('Register'):
        new_actor = actor_service.create_actor(name=name, birthday=birthday, nationality=nationality)
        if new_actor:
            st.rerun()
        else:
            st.error('Error to register actor please check fields')
