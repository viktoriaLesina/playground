import os
import json
from datetime import datetime, date

file_path = "persons.json"
today = date.today()

if os.path.exists(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)

for person in data:
    birth_date = person["birth_date"]
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")

    age = today.year - birth_date.year

    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    if age < 18:
        print(
            f"Name: {person['name']}, "
            f"Birth_date: {person['birth_date']}, "
            f"Gender: {person['gender']}"
        )
