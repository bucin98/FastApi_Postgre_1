from fastapi import FastAPI
import requests
from pydantic import BaseModel
from database import filter_add_uniques, get_last_added, create_tables
from utils import validate_response

app = FastAPI()


class Question(BaseModel):
    questions_num: int


@app.post("/api/v1/questions")
def get_questions(request_data: Question):
    last_added = get_last_added()
    added_num = 0

    while added_num < request_data.questions_num:
        response = requests.get(
            f"https://jservice.io/api/random?count={request_data.questions_num - added_num}").json()

        if not validate_response(response):
            return {'result': 'error'}

        added_num_in = filter_add_uniques(response)
        added_num += added_num_in

    return {'result': 'success', 'data': last_added}


@app.on_event("startup")
async def startup_event():
    create_tables()
