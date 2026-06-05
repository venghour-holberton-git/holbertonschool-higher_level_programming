#!/usr/bin/python3
"""csv to json module"""


import csv
import json

def convert_csv_to_json(csv_file):
    with open(csv_file, mode='r', newline='', encoding="utf-8") as csv_file:
        data = list(csv.DictReader(csv_file))

    with open("data.json", mode='w', encoding="utf-8") as json_file:
        json.dump(data, json_file, indent = 4)

if __name__ == "__main__":
    convert_csv_to_json("data.csv")
