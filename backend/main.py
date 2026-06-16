from fastapi import FastAPI
from models import UserPreference
from movie_data import movies

app = FastAPI()

@app.post("/recommend")
def recommend(pref: UserPreference):

    result = []

    for movie in movies:

        score = 0

        if movie["genre"] == pref.genre:
            score += 1

        if movie["mood"] == pref.mood:
            score += 1

        if movie["rating"] >= pref.min_rating:
            score += 1

        movie_copy = movie.copy()
        movie_copy["score"] = score

        result.append(movie_copy)

    result.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return {
        "recommendations": result[:3]
    }