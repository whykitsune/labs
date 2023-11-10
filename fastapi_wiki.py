from fastapi import FastAPI
import wikipedia
from pydantic import BaseModel

app = FastAPI(title= 'Info from Wiki')


class Summary(BaseModel):
    word_summary: str

class Articles(BaseModel):
    word_articles: list


class WordInput(BaseModel):
    word: str


@app.get('/{word}', response_model=Summary)
def get_word(word: str):
    '''Роут с параметром path'''
    return Summary(word_summary=wikipedia.summary(word))


@app.get('/', response_model=Articles)
def get_articles(word: str, articles_results: int):
    '''Роут с параметром query'''
    return Articles(word_articles=wikipedia.search(word, results=articles_results))


@app.post('/3', response_model=Summary)
def get_summary(word_input: WordInput):
    '''Роут с передачей параметра в теле запроса'''
    return Summary(word_summary=wikipedia.summary(word_input))
