import time
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, not_
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DB_URL = os.environ['DB_URL']
engine = create_engine(DB_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)


class QuizQuestion(Base):
    __tablename__ = 'quiz_questions'

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
    question_creation_date = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)


def create_tables():
    Base.metadata.create_all(engine)


def form_object(object_dict: dict) -> QuizQuestion:
    question_object = QuizQuestion(id=object_dict['id'], question=object_dict['question'],
                                   answer=object_dict['answer'],
                                   question_creation_date=object_dict['created_at'])
    return question_object


def add_questions(
        question_objects: list[QuizQuestion]):
    with Session() as session:
        session.add_all(question_objects)
        session.commit()


def filter_uniques(questions: list) -> list[dict]:
    with Session() as session:
        all_ids = session.query(QuizQuestion.id).all()
        uniques = [question for question in questions if question['id'] not in all_ids]
        return uniques


def filter_add_uniques(questions: list[dict]) -> int:
    uniques_dicts = filter_uniques(questions)
    uniques_objects = [form_object(x) for x in uniques_dicts]

    if uniques_objects:
        add_questions(uniques_objects)
    return len(uniques_dicts)


def get_last_added():
    with Session() as session:
        last_added = session.query(QuizQuestion).order_by(QuizQuestion.created_at.desc()).first()
        if not last_added:
            return None
        return {"id": last_added.id, "question": last_added.question, "answer": last_added.answer,
                'created_at': last_added.created_at}


if __name__ == '__main__':

    repeats = 0
    while True:
        try:
            create_tables()
        except Exception as ex:
            if repeats >= 5:
                raise ex
            repeats += 1
            time.sleep(1)
