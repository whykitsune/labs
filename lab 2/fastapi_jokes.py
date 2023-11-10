from fastapi import FastAPI
import pyjokes
app = FastAPI()
@app.get("/")
def joke():
    return pyjokes.get_joke()

@app.get("/{friend}")
def friends_joke(friend: str):
    return friend + " tells his joke:" + pyjokes.get_joke()

@app.get("/multi/{friend}")
def multi_friends_joke(friend: str, jokes_number: int):
    result = ""
    for i in range(jokes_number):
        result += friend + f" tells his joke #{i + 1}: " + pyjokes.get_joke() + " "
    return result

from pydantic import BaseModel
class Joke(BaseModel):
    friend: str
    joke: str
class JokeInput(BaseModel):
    friend: str
@app.post("/", response_model=Joke)
def create_joke(joke_input: JokeInput):
    """Создание шутки"""
    return Joke(friend=joke_input.friend, joke=pyjokes.get_joke())
