import json
from csv import reader


def open_csv(path_to_file: str) -> list:
    with open(path_to_file) as f:
        csv_list = []
        csv_reader = reader(f)
        header = next(csv_reader)
        for row in csv_reader:
            csv_list.append(dict(zip(header, row)))
        return csv_list


def open_json(path_to_file: str) -> list:
    with open(path_to_file) as f:
        json_list = json.load(f)
    return json_list


result_list = []
csv_file = open_csv(path_to_file="homework_3/books.csv")
json_file = open_json(path_to_file="homework_3/users.json")

for user in json_file:
    result_list.append({
        "name": user["name"],
        "gender": user["gender"],
        "address": user["address"],
        "age": user["age"],
    })

iter_user = iter(result_list)
for book in csv_file:
    try:
        current_user = next(iter_user)
    except StopIteration:
        iter_user = iter(result_list)
        current_user = next(iter_user)
    if "books" not in current_user.keys():
        current_user["books"] = []
    current_user["books"].append({
        "title": book["Title"],
        "author": book["Author"],
        "pages": int(book["Pages"]),
        "genre": book["Genre"]
    })

with open("homework_3/result.json", "w") as f:
    json.dump(result_list, f, indent=4)
