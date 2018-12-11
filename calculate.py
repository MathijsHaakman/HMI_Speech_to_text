import os
import requests
import re


def calculate_precision_and_recall(reference: str, guess: str):
    regex = re.compile('\.')
    reference_list = regex.sub('', reference.lower()).split(' ')
    guess_list = regex.sub('', guess.lower()).split(' ')
    unique_list = set(reference_list)
    for word in list:
        print(word)


def get_precision(value: str, reference: list, guess: list):
    correct = 0
    total = 0
    for index, word in enumerate(guess):
        if word == value:
            total += 1
            if index < len(reference) & reference[index] == value:
                correct += 1


def get_recall(value: str, reference: list, guess: list):
    correct = 0
    total = 0
    for index, word in enumerate(reference):
        if word == value:
            total += 1
            if index < len(guess) & guess[index] == value:
                correct += 1


with open(os.path.join("Results", "results.csv"), 'r') as list:
    list.readline()
    line = list.readline()
    print("number;wrr,wer")
    while line:
        data = line.split(";")
        reference = data[1]
        guess = data[3]

        r = requests.post(
            "http://api.robbit.me",
            json={
                "guess": guess,
                "reference": reference
            }
        ).json()

        print("{};{};{}".format(data[0], r["wrr"], r["wer"]))



        line = list.readline()