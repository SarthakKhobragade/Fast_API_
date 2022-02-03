from pydantic import BaseModel


class Info(BaseModel):
    number1: int
    number2: int
    answer: int


class Payload(BaseModel):
    number1: int
    number2: int
    unique_identifier: str
