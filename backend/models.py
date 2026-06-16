from pydantic import BaseModel

class UserPreference(BaseModel):
    genre: str
    mood: str
    min_rating: int