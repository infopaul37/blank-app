import streamlit as st

st.title("Weather App ")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st
import pandas as pd

df = pd.DataFrame(
    [
        {"temperature": "st.selectbox", "place": "paris"},
        {"temperature": "st.balloons", "place": "tokyo"},
        {"temperature": "st.time_input", "place": "Londres"}
    ]
)

st.dataframe(df, use_container_width=True)
lien_api = "https://api.weatherbit.io/v2.0/current" 
+"&city=Paris&country=France"
+ "&key=32af0f6ca0b24b1793376130cc6b9b9b" 
+ "&include=minutely"