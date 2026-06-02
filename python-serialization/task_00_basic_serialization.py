#!/usr/bin/python3
"""serialization module"""
import pickle


def serialize_and_save_to_file(data, filename):
    with open(filename, "wb") as file:
        pickle.dump(data, filename)

def load_and_deserialize(filename):
    with open(filename, "rb") as file:
        return pickle.load(file)
