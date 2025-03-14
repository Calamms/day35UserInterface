import streamlit as st
import requests

import numpy as np
import pandas as pd

st.markdown("""# This is a header
## This is a sub header
This is text""")

df = pd.DataFrame({
    'first column': list(range(1, 11)),
    'second column': np.arange(10, 101, 10)
})

# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider('Select a line count', 1, 10, 3)

# and used to select the displayed lines
head_df = df.head(line_count)

head_df

x = st.text_input("Enter day_of_week (X)", value="2")
y = st.text_input("Enter time (Y)", value="3")

# Bouton pour lancer la prédiction
if st.button("Predict"):
    # Construction dynamique de l'URL
    url = f"https://api-866662164769.europe-west1.run.app/predict?day_of_week={x}&time={y}"

    try:
        # Requête vers l'API
        response = requests.get(url).json()
        st.text_area("API Response", value=str(response), height=150)
    except Exception as e:
        st.error(f"Error: {e}")
