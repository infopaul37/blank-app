import streamlit as st
import pandas as pd
import requests

# endpoint est une variable qui contient le lien sans les parametres pour acceder à la météo depuis le fournisseur de service
ENDPOINT = "https://api.weatherbit.io/v2.0/current?"

st.title("Weather App ")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

def get_current_weather(city, country,api_key):
    global ENDPOINT
    query = {
        "city":'Paris', 
        "country":'France',
        "key": '32af0f6ca0b24b1793376130cc6b9b9b',
        "include": 'minutely'
    }
    response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
    print(response.json())
    return response.json()
    

df = pd.DataFrame(
    [
        {"City": "Paris", "Temperature": 15},
        {"City": "Londres", "Temperature": 15},
        {"City": "Tokyo", "Temperature": 15},
    ]
)

st.dataframe(df, use_container_width=True)
