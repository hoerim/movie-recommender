import streamlit as st
import requests

st.title("🎬 영화 추천 시스템")

genre = st.selectbox(
    "장르",
    ["SF", "Action", "Romance", "Drama"]
)

mood = st.selectbox(
    "분위기",
    ["감동", "흥미진진", "긴장감"]
)

rating = st.slider(
    "최소 평점",
    1,
    10,
    7
)

if st.button("추천받기"):

    response = requests.post(
        "http://backend:8000/recommend",
        json={
            "genre": genre,
            "mood": mood,
            "min_rating": rating
        }
    )

    movies = response.json()["recommendations"]

    st.subheader("추천 결과")

    for movie in movies:

        st.write(f"🎥 {movie['title']}")
        st.write(f"⭐ {movie['rating']}")
        st.write(movie["description"])
        st.divider()