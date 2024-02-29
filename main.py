from datetime import datetime
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel, model_validator

app = FastAPI()


class Sleep(BaseModel):
    start: datetime
    end: datetime | None = None
    sleep_id: int = None

    @model_validator(mode="before")
    def generate_field_two(self):
        if not self.sleep_id:
            self.sleep_id = int(self.start.timestamp())
        return self


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/sleeps")
def list_sleeps(q: Union[str, None] = None):
    return {"sleeps": [{"sleep_id": "123"}, {"sleep_id": "456"}], "q": q}


@app.get("/sleeps/{sleep_id}")
def get_sleep(sleep_id: str):
    return {
        "sleep_id": sleep_id,
        "start": datetime.fromisoformat("2023-01-01 00:00:00"),
        "end": datetime.fromisoformat("2023-01-01 01:30:00")
    }


@app.post("/sleeps")
def create_sleep(sleep: Sleep) -> Sleep:
    return sleep
