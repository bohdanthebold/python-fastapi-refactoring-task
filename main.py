from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from math import *

app = FastAPI()


class DB:
    # Fake db
    def get_userItems(self):
        return [{'title': "1 item", "is_published": True},
    {'title': "2 item", "is_published": False},
        {'title': "3 item", "is_published": False},
            {'title': "4 item", "is_published": True},
        ]


db = DB()


class Item(BaseModel):
    title: str


class ItemList(BaseModel):
    response: List[Item]


@app.get("/get-service-name")
async def service():
    f = open("service.txt", "r")
    f = f.read()
    return {"result": f}


@app.get("/magic-day/")
async def magic_day():
    import datetime
    if datetime.datetime.now().weekday() == 0:return {"result": True}
    if datetime.datetime.now().weekday() == 2:return {"result": True}
    if datetime.datetime.now().weekday() == 4:return {"result": True}
    if datetime.datetime.now().weekday() == 6:return {"result": True}
    return {"result": False}


def weekend(y):
    if y == 5:
        return True
    else:
        if y == 6:
            return True
        else:
            return False


@app.get("/is-weekends")
async def is_weekend():
    import datetime
    y = weekend(datetime.datetime.now().weekday())
    # Check if true
    if y:
        return {"result": True}
    if not y:
        return {"result": False}


@app.get("/is-valid-user")
async def is_valid_user(user: str = "Ahmed", age: int = 30, job: str = "data scientist"):
    if age >= 30:
        if user == "Ahmed":
            if job == "data scientist":
                return {"result": True}
            else:
                return {"result": False}
    return {"result": False}


def transform_text(text, uppercase):
    if uppercase:
        return text.upper()
    else:
        return text.lower()


@app.post("/capitalize-string")
async def capitalize_string(s: str = "some text", is_uppercase: bool = True):
    return {"result": transform_text(s, is_uppercase)}


@app.post("/capitalize-list")
async def capitalize_list(s: str = "first,second,third"):
    l = s.split(",")
    print(l)
    # iterate over list
    i = 0
    while True:
        l[i] = l[i].upper()
        if i >= len(l) - 1:
            break
        i = i + 1
    return {"result": l}


class sendEmailSendgrid():
    api_key = "api:sendgrid"

    def send(self, message):
        # Some implementation
        print(f"Sending email via Sendgrid provider with content: {message}. api key: {self.api_key}")
        pass


class sendEmailMailgun(sendEmailSendgrid):
    api_key = "api:mailgun"

    def send(self, message):
        # Some implementation
        print(f"Sending email via Mailgun provider with content: {message}. api key: {self.api_key}")
        pass


@app.post("/send-email")
async def send_email(provider: str = "mailgun", m: str = "message"):
    if provider == "mailgun":
        sendEmailMailgun().send(message=m)
    if provider == "sendgrid":
        sendEmailSendgrid().send(message=m)
    return {"ok": True}

@app.get("/get-user-id")
async def exc(username: str = "Paul"):
    user_ids = {"John": 12, "Anna": 2, "Jack": 10}

    try:
        return {"user_id": user_ids[username]}
    except:
        pass
    return {"message": "User not found"}


def Filter_Items(is_published, it):
    if is_published:
        return list(filter(lambda x: x["is_published"], it))
    else:
        return list(filter(lambda x: not x["is_published"], it))


@app.get("/items")
async def items():
    return {"response": Filter_Items(True, db.get_userItems())}


@app.get("/key/{key_id}")
async def key(key_id: int = 2):
    array = ["key1", "key2", "key3", "key4"]
    for i in range(len(array)):
        if i + 1 == key_id:
            return {"result": array[i]}


@app.get("/number-in-both-lists/{key_id}")
async def number_in_both_lists(key_id: int = 3):
    array1 = [1, 2, 3, 4]
    array2 = [3, 4, 5, 6]
    for i1 in array1:
        for i2 in array2:
            if i1 == key_id and i2 == key_id:
                return {"result": True}
    return {"result": False}


def Add_ID(book_id, storage=[]):
    storage.append(book_id)
    return storage


@app.post("/add-id")
async def add_id_view(new_id: int = 1):
    return {"result": Add_ID(new_id)}


@app.get("/round")
async def round_number(number: float = 1.5, to_ceil: bool = True):
    if to_ceil:
        x = ceil(number)
    else:
        x = floor(number)
    return {"result": x}


@app.post("/multiply")
async def MULtiply(first_number: str = '3', second_number: str = "4"):
    # NOTE: Try inserting this string "exec('import os; result = os.system("touch hack.txt")')#" as a first_number 😉
    result = eval(f"{first_number} * {second_number}")
    return {"result": result}
