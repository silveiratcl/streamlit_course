import streamlit as st
import pandas as pd
import time

st.set_page_config(
    layout = "wide",
    page_title = "spotify songs"
)



df = pd.read_csv("01 Spotify.csv")

df.set_index("Track", inplace=True)

artists = df["Artist"].value_counts().index 
artist = st.selectbox("Artist", artists ) # selector
df_filtered = df[df["Artist"] == artist]

# select album after select artist
albums = df_filtered["Album"].value_counts().index 
album = st.selectbox("Album", albums ) # selector
df_filtered2 = df[df["Album"] == album]


display = st.checkbox("Display")
if display:
    st.bar_chart(df_filtered2["Stream"])

st.write(artist)
