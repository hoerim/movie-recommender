import streamlit as st
import requests

st.title("🎬 영화 추천 시스템")

genre = st.selectbox(
    "장르",
    ["SF", "액션", "로맨스", "드라마", "코미디", "역사", "스릴러", "호러", "미스테리"]
)

mood = st.selectbox(
    "분위기",
    ["감동", "흥미진진", "긴장감", "유쾌", "어두움", "무서움"]
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
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(movie["poster"], width=250)
            
        with col2:
            st.subheader(movie["title"])
            st.write(movie["description"])
            st.write(f"⭐ 평점: {movie['rating']}")
            st.write(f"🎭 장르: {movie['genre']}")

        st.divider()