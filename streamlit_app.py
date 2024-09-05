import streamlit as st
import pandas as pd
import requests

# endpoint est une variable qui contient le lien sans les parametres pour acceder à la météo depuis le fournisseur de service
ENDPOINT = "https://api.weatherbit.io/v2.0/current"

st.title("Weather App ")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

def get_current_weather(city, api_key = "32af0f6ca0b24b1793376130cc6b9b9b", country ='FR'):
    global ENDPOINT
    query = {
        "city": city, 
        "country": country,
        "key": api_key,
    }

    response = requests.get(ENDPOINT, params=query)
    response = response.json()
    print(response)
    return response
    
get_current_weather('Paris', api_key='32af0f6ca0b24b1793376130cc6b9b9b')

df = pd.DataFrame(
        {
        "Countries": ["FR", "UK", "Japan" ],
        "Cities": ["Paris","avignon", "dijon",],
        "Temperatures": [-99,-99,-99],
        }
)
resultat = df.Cities.apply(get_current_weather)
print(resultat)

st.dataframe(df, use_container_width=True)
